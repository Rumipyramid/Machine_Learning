---
name: lapuerta
description: >-
  Genera y consulta usuarios (personas) sintéticos de consumidores de seguros del
  Perú, calibrados con datos reales (SBS 2023, APESEG, APEIM y economía conductual).
  Invócalo con /lapuerta o úsalo cuando se pidan perfiles sintéticos de asegurados
  peruanos, simular o "entrevistar" consumidores de seguros, muestrear poblaciones para
  prototipado, encuestas sintéticas o pruebas de mensajes/segmentos. Variables: generación,
  NSE, región, educación financiera, sesgo del presente, canal, exposición sísmica,
  apertura a datos/IA, confianza, tenencia, seguro de desastres y disposición a pagar (WTP).
---

# lapuerta · Usuarios sintéticos de seguros (Perú)

> Invocación: **`/lapuerta`**. Abre la "puerta" a una población sintética de consumidores
> de seguros peruanos.

Skill autocontenido para **generar poblaciones sintéticas** de consumidores de seguros
peruanos y **simular sus respuestas**. Las distribuciones están calibradas con datos
reales y validadas (marginales del modelo ≈ realidad).

## Cuándo usarlo
- "Genera N usuarios/personas sintéticas de seguros (Perú)."
- "Hazle una pregunta a un grupo de consumidores simulados / a un segmento (NSE A, Gen Z…)."
- "Necesito una muestra para prototipar, balancear clases o probar un mensaje."
- "¿Qué proporción desconfía / tiene seguro / pagaría más en tal segmento?"

## Cómo generar usuarios

El generador usa **solo la librería estándar** de Python (no requiere instalar nada).

```bash
# N perfiles a consola (CSV)
python scripts/generate_synthetic_users.py --n 20 --seed 42

# N perfiles a archivo, reproducible
python scripts/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42
```

Banderas: `--n` (cantidad), `--out` (ruta CSV; si se omite, imprime), `--seed`
(semilla para reproducibilidad), `--schema` (ruta a otro esquema).

**Semilla:** misma semilla → exactamente las mismas personas (experimento reproducible).

### Filtrar por segmento
El generador muestrea la población completa. Para un segmento (p. ej. solo NSE A,
o Gen Z de Lima), genera un lote grande y filtra por el campo correspondiente. Patrón:

```python
import importlib.util, random, csv, os
spec = importlib.util.spec_from_file_location("g", "scripts/generate_synthetic_users.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
rng = random.Random(101); schema = g.load_schema()
grupo, i = [], 0
while len(grupo) < 30:                 # 30 usuarios NSE A
    u = g.generate_user(rng, schema, i); i += 1
    if u["nse"] == "A":
        u["id"] = f"A_{len(grupo):02d}"; grupo.append(u)
```

Campos para filtrar: `generacion`, `nse`, `region`, `canal_preferido`, etc.

## Las 17 variables (qué significa cada una)
| Variable | Significado |
|---|---|
| `generacion` | Cohorte de edad: `Gen_Z_18_27`, `Millennial_28_43`, `Gen_X_44_59`, `Boomer_60_mas`. |
| `nse` | Nivel socioeconómico A (alto) … E (bajo). Principal driver de tenencia. |
| `region` | `Lima_Metropolitana`, `Resto_Costa`, `Sierra`, `Selva`. Define exposición sísmica. |
| `educacion_financiera` | `baja` / `media` / `alta`. |
| `sesgo_presente` | Tendencia a postergar la decisión (`alto`/`medio`/`bajo`); frena la compra. |
| `canal_preferido` | `directo_digital`, `bancaseguros`, `broker_corredor`, `ninguno`. |
| `situacion_laboral` | `formal_dependiente` / `independiente_microemprendedor` / `informal` (depende de NSE). Formal → Vida Ley. |
| `cobertura_previsional` | `AFP` / `ONP` / `ninguna` (depende de situación laboral). `ninguna` → brecha en la vejez. |
| `tenencia_vehiculo` | `ninguno` / `auto` / `moto_mototaxi` (depende de región). Base de SOAT y su cumplimiento. |
| `acceso_digital` | `alta` / `media` / `baja` (región+NSE+generación). Billetera móvil / uso digital. |
| `bancarizado` | `True`/`False`. Pertenece al sistema financiero (≈59%); habilita bancaseguros. |
| `exposicion_riesgo_sismico` | `alta` / `media` / `baja` (depende de la región). |
| `apertura_datos_ia` | Disposición a compartir datos y confiar en IA (mayor en jóvenes). |
| `confianza_aseguradora` | `confia_plena` / `neutral` / `desconfia`. |
| `tenencia_seguro` | `voluntario` / `solo_obligatorio` (SOAT/Vida Ley) / `ninguno`. |
| `seguro_desastres_naturales` | `True`/`False` (cobertura ante sismos). |
| `wtp_ratio` | Disposición a pagar como fracción del precio justo (1.0 = precio técnico). |

## Cómo simular respuestas (dos motores)
A partir del perfil de cada persona se construye su respuesta:

1. **Por reglas (listo para usar):** `scripts/simulate_rules.py`. Cada rasgo suma o resta
   y decide la postura; las direcciones vienen de los datos (`desconfia` −, `nse` alto +,
   `sesgo_presente` alto −, `educacion alta` +, `canal broker` +). Para preguntas cerradas
   y porcentajes reproducibles.
   ```bash
   python scripts/simulate_rules.py --list                      # preguntas disponibles
   python scripts/simulate_rules.py --question confianza --n 1000 --seed 42
   python scripts/simulate_rules.py --question contratar --n 1000 --by nse
   python scripts/simulate_rules.py --question marca --brand "RIMAC" --filter nse=A --by generacion
   ```
   Preguntas: `confianza`, `contratar`, `tenencia`, `marca` (`--brand`), `datos_ia`.
   Banderas: `--n`, `--seed`, `--filter campo=valor` (repetible), `--by <dimensión>`.
2. **Con un LLM (Claude):** dale al modelo el perfil + el codebook de arriba y pídele
   responder en primera persona, coherente con los atributos, devolviendo `quote` +
   `sentiment` (favorable/neutral/desfavorable). Útil para preguntas abiertas.

Para clasificar/agregar: cuenta por `sentiment` o por categoría y reporta porcentajes y
diferencias por segmento (NSE, generación, canal).

## De dónde sale cada parámetro (trazabilidad)
- Confianza (confía/desconfía) → **SBS 2023** (encuesta de conocimiento y percepción).
- Tenencia y penetración → **APESEG**.
- Segmentación NSE (A–E) → **APEIM**.
- Sesgo del presente y WTP → **economía conductual**.
- Penetración macro (% PBI) → **MAPFRE Economics / OECD**.

## Validación (evidencia de que reproduce la realidad)
Re-muestreo de n=5 000: las marginales simuladas ≈ las reales →
tiene seguro 43% vs 40%, desconfía 45% vs 48%, seguro de desastres 2.9% vs 3.3%.

**Harness automático** (`scripts/validate.py`): mide los tres ejes de calidad —
marginales vs objetivo con tolerancia, asociaciones por pares (monotonía + Cramér's V),
intervalos bootstrap y curva de estabilidad (varianza vs n):
```bash
python scripts/validate.py                 # reporte completo
python scripts/validate.py --check         # pass/fail para CI (exit 1 si falla)
python scripts/validate.py --stability     # incluye varianza vs n
python scripts/validate.py --joint fitted.csv   # validar sembrando desde IPF/ENAHO
```
El motor de reglas reporta incertidumbre con `--bootstrap B` (IC 95% por categoría):
```bash
python scripts/simulate_rules.py --question contratar --filter nse=A --bootstrap 1000
```

## Ajustar / recalibrar
Edita `scripts/synthetic_user_schema.json`: marginales, tablas condicionales
(`exposicion`, `apertura`), pesos del modelo logístico de tenencia (`drivers`),
y la WTP. Cada variable marca su `origen` (`dato` vs `supuesto`). Recalibra con
micro-datos locales (p. ej. ENAHO) antes de usar en decisiones reales.

## Límites
Datos **sintéticos**: no representan personas reales. Aptos para prototipado,
exploración de hipótesis y diseño de mensajes; **no** sustituyen una encuesta de
mercado ni prueban relaciones causales.

## Archivos del skill
- `scripts/generate_synthetic_users.py` — generador (stdlib).
- `scripts/simulate_rules.py` — motor de respuestas por reglas (stdlib): distribución + desglose.
- `scripts/synthetic_user_schema.json` — distribuciones calibradas (editable).
- `references/matriz_usuarios_sinteticos.md` — matriz completa, grafo de dependencias y arquetipos.
- `SKILL.en.md` — guía equivalente en inglés (para compartir).

## Instalación (para compartir)
Copia la carpeta `lapuerta/` a `.claude/skills/` (proyecto) o `~/.claude/skills/`
(personal). Reinicia la sesión y se invoca con **`/lapuerta`**.
