# Cómo funciona "la puerta" — mecánica interna, validez y confiabilidad

> Guía explicativa del generador de usuarios sintéticos (`lapuerta`). Sencilla pero
> detallada: cómo se fabrica cada persona, por qué creemos que se parece a la realidad
> (validez) y por qué los resultados son estables y auditables (confiabilidad).
>
> Código fuente: `research/personas/generador/` · Skill: `.claude/skills/lapuerta/`

---

## 1. Qué es (y qué no es)

"La puerta" es una **fábrica de personas sintéticas**: produce miles de perfiles ficticios de
consumidores de seguros peruanos, cada uno con 17 características, muestreados de
distribuciones de probabilidad calibradas con datos reales.

- **Sirve para:** prototipar, explorar hipótesis, segmentar, probar mensajes, balancear
  datasets y "entrevistar" grupos simulados a bajo costo y en minutos.
- **No sirve para:** reemplazar una encuesta de mercado, ni para probar relaciones causales,
  ni para representar personas reales. Es un laboratorio barato para **afinar preguntas**,
  no para cerrar decisiones de inversión sin validación de campo.

Pensalo como un simulador de vuelo: no es un avión real, pero reproduce su comportamiento lo
bastante bien como para entrenar y probar ideas antes de gastar en lo real.

---

## 2. La mecánica interna

### 2.1 La idea central: muestrear de distribuciones

Una persona no se "inventa": se **muestrea**. Para cada variable hay una distribución de
probabilidad (qué proporción de la población cae en cada categoría) y el generador "tira los
dados" respetando esas proporciones. Si el 34% de la población es NSE E, entonces ~34% de las
personas generadas saldrán NSE E.

### 2.2 Tres tipos de variables

El modelo (17 variables, esquema `synthetic_user_schema.json` v1.2) las organiza en tres clases
según **cómo** se generan:

**a) Independientes (marginales).** Se muestrean directamente de su distribución, sin depender
de nada. Ej.: `generacion`, `nse`, `region`, `educacion_financiera`, `sesgo_presente`,
`canal_preferido`.

**b) Condicionales (tablas).** Su distribución **depende** del valor de otra variable. Ej.:
`exposicion_riesgo_sismico` depende de `region` (Lima/Costa → mayoritariamente alta exposición;
Selva → baja). Es una tabla "si region = X, entonces estas probabilidades".

**c) Derivadas (modeladas).** Se calculan con un pequeño modelo que combina varias variables.
Ej.: `tenencia_seguro` se decide con un **modelo logístico** (ver 2.4).

> Cada celda del esquema lleva una etiqueta de origen: **`dato`** (anclado a una fuente real)
> o **`supuesto`** (estimación ilustrativa, ajustable). Esto hace explícito qué está respaldado
> y qué es un supuesto a refinar.

### 2.3 El grafo de dependencias (quién depende de quién)

```
region ───────────────▶ exposicion_riesgo_sismico ─┐
generacion ───────────▶ apertura_datos_ia          │
canal_preferido ──────▶ confianza_aseguradora ──┐   │
nse ─────────────────┐                          │   │
educacion_financiera ┼─▶ tenencia_seguro ◀───────┘   │
sesgo_presente ──────┘          │                     │
situacion_laboral ───┘          ▼                     ▼
                     seguro_desastres_naturales ◀─────┘
                                │
                                ▼
                            wtp_ratio  (◀ tenencia)
```

El orden de generación respeta este grafo: primero las independientes, luego las condicionales,
al final las derivadas (que necesitan a las anteriores ya definidas).

### 2.4 El corazón: el modelo de tenencia de seguro

`tenencia_seguro` (¿tiene seguro?) es la variable más importante y se decide en dos pasos:

**Paso 1 — ¿tiene algún seguro?** Se suma un "puntaje" (score) con los empujes de cada rasgo:

```
score = intercepto
      + peso_nse[nse]                     (A: +1.6 … E: −0.9)
      + peso_educacion[educacion]         (alta: +0.9 … baja: −0.5)
      + peso_sesgo[sesgo_presente]        (alto: −0.7 … bajo: +0.5)
      + peso_confianza[confianza]         (confía: +0.6 … desconfía: −0.5)
      + peso_situacion_laboral[...]       (formal: +0.5 … informal: −0.5)
      + peso_bancarizado[...]             (sí: +0.4 … no: −0.2)
      + peso_vehiculo[...]                (auto: +0.5 …)
      + peso_cobertura_previsional[...]   (AFP: +0.2 … ninguna: −0.2)
```

Ese score se pasa por la función **sigmoide**, que lo convierte en una probabilidad entre 0 y 1:

```
probabilidad = 1 / (1 + e^(−score))
```

Se tira un dado: si cae por debajo de esa probabilidad, la persona tiene seguro. Así, un NSE A
con educación alta y baja procrastinación tiene **mucha** más probabilidad que un NSE E informal
con sesgo del presente alto — exactamente como en la realidad.

**Paso 2 — ¿voluntario u obligatorio?** Si tiene seguro, otro sorteo decide si es voluntario o
solo obligatorio (SOAT/Vida Ley). Ser formal o tener auto inclina la balanza hacia **obligatorio**.

Las otras variables derivadas siguen la misma lógica:
- `confianza_aseguradora`: parte de una marginal y el **broker la desplaza hacia "confía"**.
- `seguro_desastres_naturales`: base ~3.3% multiplicada por NSE, exposición y tenencia.
- `wtp_ratio` (disposición a pagar): gaussiana; el asegurado paga ~1.05 del precio justo, el no
  asegurado solo ~0.66.

### 2.5 La semilla: por qué los resultados se pueden repetir

El generador usa un **generador de números aleatorios con semilla** (`--seed`). Misma semilla →
**exactamente las mismas personas**. Esto hace que cualquier resultado sea **reproducible y
auditable**: otra persona corre el mismo comando y obtiene lo mismo, bit a bit.

### 2.6 Calibrar con dato real: la ruta ENAHO → IPF

Por defecto las variables base se muestrean **independientes**. Pero las características reales
están **correlacionadas** (NSE, región, educación y edad no son independientes). Para capturar
eso existe una ruta de calibración con microdato oficial:

```
ENAHO (INEI)  ──enaho_loader.py──▶  tabla conjunta ponderada
                                          │
                                     ipf.py (raking)  ──▶  conjunta ajustada (fitted.csv)
                                          │
              generate_synthetic_users.py --joint fitted.csv
                                          │
                                     validate.py  (¿mejoró?)
```

- **`enaho_loader.py`** lee los módulos de ENAHO (CSV), los cruza por hogar/persona y aplica el
  **factor de expansión** (los pesos muestrales; sin ellos las cifras se sesgan).
- **`ipf.py`** (Iterative Proportional Fitting / *raking*) ajusta esa tabla a las marginales que
  queremos, **conservando la estructura de asociación** real (los "odds-ratios").
- El generador, con `--joint`, muestrea las variables base de esa conjunta real en vez de
  hacerlo independientes.

> Ya aplicado: con la **ENAHO 2025 (módulo 200, 115k personas)** se recalibraron `generacion` y
> `region`. Reveló que el modelo asumía una población más joven de la real (Gen Z 0.22→0.197,
> Boomer 0.20→0.254); su origen pasó de `supuesto` a `dato`.

---

## 3. Mecanismos de VALIDEZ (¿se parece a la realidad?)

La validez responde: *¿lo que produce el modelo coincide con el mundo real?* Tres capas:

### 3.1 Calibración a marginales reales
Las distribuciones están ajustadas para que las proporciones del modelo igualen cifras reales
(SBS, APESEG, APEIM, BCRP/INEI). Objetivos clave que el modelo reproduce:

| Indicador | Objetivo (real) | Fuente |
|---|---|---|
| Tiene algún seguro | ≈ 40% | SBS |
| Desconfía de aseguradoras | ≈ 48% | SBS/APESEG |
| Seguro de desastres | ≈ 3.3% | APESEG |
| Bancarizado | ≈ 59% | BCRP/INEI |
| Sin cobertura previsional | ≈ 60% | informalidad ~70% |

### 3.2 Asociaciones "por diseño" (que las relaciones tengan sentido)
No basta con que cada variable suelta cuadre; las **relaciones entre variables** deben cumplirse.
El modelo verifica, por ejemplo:
- Tenencia **sube** con NSE (A ≈ 85% → E ≈ 21%) y con educación; **baja** con el sesgo del presente.
- El **broker reduce la desconfianza** (≈34% vs ≈45% global).
- Los desastres se aseguran más donde hay **alta exposición** sísmica.
- El asegurado tiene **mayor disposición a pagar** que el no asegurado.

Además se reporta la **fuerza** de asociación con *Cramér's V* (0 = sin relación, 1 = relación
total): NSE × tenencia ≈ 0.30, región × exposición ≈ 0.35.

### 3.3 Calibración con dato real (ENAHO)
La ruta de la sección 2.6 ancla variables a microdato oficial. Es el salto que convierte un
modelo "plausible" en uno "calibrado": en vez de suponer, se mide.

### 3.4 Límites de validez (honestidad)
- Varios pesos del modelo son **juicio de experto** (`supuesto`), no estimados por regresión.
- Algunos son **proxies**: `educacion_financiera` ≈ nivel educativo; `nse_proxy` (de ENAHO) ≈
  quintiles de gasto, que **no es APEIM**.
- El marco es **urbano-céntrico** (APEIM); rural/lengua materna quedan subrepresentados.
- Falta un **benchmark de criterio**: comparar una pregunta real de distribución conocida contra
  la simulación. Es el siguiente paso natural de validez.

---

## 4. Mecanismos de CONFIABILIDAD (¿es estable y auditable?)

La confiabilidad responde: *¿puedo confiar en que el número no es ruido y se puede repetir?*

### 4.1 Reproducibilidad por semilla
Misma semilla → mismas personas (sección 2.5). Cualquier cifra es **re-ejecutable** por terceros.

### 4.2 Intervalos de confianza (bootstrap)
Un "42% desconfía" tiene **ruido de muestreo**. El motor de reglas (`--bootstrap`) y el harness
re-muestrean la población muchas veces y reportan el **IC 95%**: p. ej. *"42% (IC 38–46%)"*. Así
se distingue una diferencia real de una casualidad de la muestra.

### 4.3 Curva de estabilidad (cuánta gente hace falta)
A más usuarios, menos varía el resultado. Medido:

| n | desviación de "tiene seguro" |
|---|---|
| 100 | ±0.061 (inestable) |
| 1 000 | ±0.019 |
| 5 000 | ±0.008 (estable) |

Esto da una **guía de n mínimo por segmento**: cuidado con conclusiones sobre NSE A (≈2% de la
población → muestras chicas → mucho ruido si no se genera suficiente.)

### 4.4 Golden test en CI (un guardián automático)
`validate.py --check` corre como **GitHub Action** (`validar-modelo.yml`) en cada push/PR que
toque el modelo. Si alguien edita el esquema y rompe una marginal (sale de tolerancia) o una
asociación, **el PR se marca en rojo** antes de mergear. El control de calidad dejó de depender
de que alguien se acuerde de correrlo.

---

## 5. Los motores de uso

| Motor | Archivo | Para qué |
|---|---|---|
| **Generación** | `generate_synthetic_users.py` | Fabricar N perfiles (CSV); `--joint` para sembrar con ENAHO. |
| **Respuestas por reglas** | `simulate_rules.py` (skill) | Preguntas cerradas con % por segmento + IC bootstrap. |
| **Conjoint de atributos** | `conjoint_atributos.py` | Importancia relativa de atributos del seguro por segmento. |
| **Respuestas con LLM** | (en sesión) | Preguntas abiertas: el modelo responde en 1ª persona por perfil. |
| **Validación** | `validate.py` | Mide validez y confiabilidad; `--check` para CI. |

---

## 6. Glosario en una línea

- **Semilla:** el "número de partida" del azar; fija la semilla y obtienes siempre la misma gente.
- **Marginal:** la proporción de cada categoría en el total (p. ej. NSE E = 34%).
- **Variable condicional:** su distribución depende de otra (exposición depende de región).
- **Modelo logístico / sigmoide:** convierte una suma de empujes en una probabilidad 0–1.
- **Factor de expansión:** peso muestral de ENAHO; cuántas personas reales "representa" cada fila.
- **IPF / raking:** ajusta una tabla a las marginales objetivo sin perder las correlaciones.
- **Bootstrap:** re-muestrear para estimar el margen de error (intervalo de confianza).
- **Cramér's V:** mide la fuerza de relación entre dos variables categóricas (0 a 1).
- **Golden test:** prueba automática que falla si el modelo se sale de sus rangos esperados.

---

## 7. En una frase

La puerta **fabrica personas muestreando distribuciones calibradas con dato real**, encadena sus
variables con una lógica explícita y trazable, y se somete a un **guardián automático** que mide
si sigue pareciéndose a la realidad (validez) y si sus números son estables y repetibles
(confiabilidad). Es transparente a propósito: cada supuesto está marcado y cada cifra es auditable.

---

*Documento explicativo del sistema `lapuerta`. Fuente de verdad del código: `research/personas/generador/`.*
