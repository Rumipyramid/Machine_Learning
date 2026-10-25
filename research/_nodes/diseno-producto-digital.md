# Diseño de producto digital: confrontaciones de hipótesis y evidencia de conversión

> Nodo de dominio del diseño, separado de [[tendencias-diseno-innovacion]] el 2026-10-25 sin cambiar su contenido.
> Fecha de elaboración: 2026-07-29 (como secciones del nodo principal) · Última actualización: 2026-10-25 · Versión: **v1.0 (separación)**
> Contiene las secciones §10, §11, §13, §14 y §15 del nodo principal, con su numeración original para que las referencias como "§11.3" sigan valiendo. Dominio: producto digital e interfaces (iteraciones 2, 3, 5, 6 y 7).
> La escala de madurez (§5), el tablero de hipótesis (§6), las reglas (§7) y la bitácora (§8) siguen en el nodo principal.

## 10. 🔁 Iteración 2 (2026-07-29) — confrontación de las hipótesis heredadas

Corrida de `/trinidad` con mandato explícito de **confrontar antes que buscar novedad**. Los cinco
pendientes que dejó la iteración 1 se atacaron uno por uno. Las tres pistas se mantienen separadas.

**Resumen de la corrida en una frase por pista:**

- 🔬 **Empírica**: la evidencia de generative UI **por fin llegó**, y dice exactamente lo que la
  teoría de 2004 predecía — gusta en la primera sesión y falla en todo lo que sostiene el uso
  repetido.
- 📱 **Social**: la hipótesis del desfase latinoamericano **era falsa**, y su refutación vino de
  conducta corporativa, no de conversación.
- 📈 **Negocio**: el ROI del diseño **no se corrigió, se recicló** — cayó el 671% y ocupó su lugar
  un 135% igual de modelado.

### 10.1 🔬 Generative UI: la evidencia llegó y se partió en dos mitades limpias

La iteración 1 clasificó la generative UI como 🔴 *propuesta sin respaldo independiente* y lo fundó
en literatura de hace 20 años (Findlater & McGrenere, F-247). En estos meses aparecieron **siete
piezas nuevas**, y el resultado no es que la clasificación estuviera mal: es que ahora se puede
partir el claim en dos, y cada mitad tiene un veredicto distinto.

**Mitad que gana — "gusta más":**

- El paper insignia (F-380, Leviathan/Valevski, Google) muestra preferencia humana abrumadora frente
  a la salida markdown de un LLM. ⚠️ Tres descuentos que el titular no lleva: es **preprint sin
  revisión por pares**, la línea base es **texto plano** (un rival deliberadamente débil), y **sus
  propios autores admiten que los resultados son peores que los de expertos humanos**, "al menos
  comparables en el 50% de los casos". Un 50% de empate contra un humano se está comunicando como
  una victoria.
- La versión peer-reviewed existe y es más seria: hasta **72% de preferencia** sobre interfaces
  conversacionales en tareas densas en información (F-381, Findings of ACL 2026). Sigue siendo
  **preferencia declarada en sesión única**.

**Mitad que pierde — "funciona mejor":**

- **138 pantallas** generadas por Figma, Banani y Stitch, evaluadas contra las 10 heurísticas de
  Nielsen (F-382, CHI 2026): baja tasa de soporte justo en **H5 prevención de errores, H7 eficiencia
  de uso, H9 recuperación de errores y H10 ayuda/documentación**. Es decir, **falla precisamente en
  los atributos que solo importan cuando el usuario vuelve** — y brilla en los que se juzgan de un
  vistazo. Esa es la firma exacta de un artefacto optimizado para la primera impresión.
- Una revisión sistemática (F-384) mide el defecto de base: **prompts idénticos producen interfaces
  sustancialmente distintas, incluso entre ejecuciones repetidas de la misma herramienta**. La
  inconsistencia **no es inmadurez del modelo: es una propiedad del paradigma**.
- La comunidad HCI produjo contrapeso publicado, no solo tuits: un position paper explícito
  *Against Generative UI* (F-383), el traslado del marco de deuda técnica oculta a las interfaces
  maleables (F-385), y un reencuadre útil de Microsoft Research (F-386): con generative UI **el
  objeto de usabilidad deja de ser la interfaz y pasa a ser el generador**.

⭐ **Lo que esto le hace a H3.** La hipótesis predecía: *gana en preferencia en la sesión 1, pierde
en tiempo de tarea y aprendibilidad a lo largo de ≥5 sesiones.* La primera mitad está **confirmada**.
La segunda no está confirmada — pero sus dos precondiciones causales (inconsistencia entre
ejecuciones, ausencia de andamiaje de error y ayuda) **ya están medidas**. H3 pasa a `parcial`.

⚠️ **Y el hallazgo negativo que vale tanto como los positivos:** tras dos iteraciones buscándolo,
**sigue sin existir un solo estudio longitudinal independiente de generative UI**. Toda la evidencia
favorable la producen los fabricantes y mide una sola sesión. Los autores de F-382 lo declaran ellos
mismos como limitación. **Un paradigma se está adoptando con evidencia que, por construcción, no
puede detectar su modo de falla principal.**

### 10.2 🔬📱 Service design: no está en silencio, está en otra tribuna — y en crisis según los suyos

La iteración 1 registró un hallazgo negativo (🧊: el service design no aparece en la conversación
social) y lo dejó como H18 con una lectura optimista: *silencio = madurez*. La pasada propia
encuentra las dos mitades, y la optimista **no gana**.

**A favor de "existe y está institucionalizado":**

- El gobierno británico comisionó y publicó una **revisión de evidencia sobre diseño público**
  (PDER, F-387): tres revisiones de literatura por un equipo académico interdisciplinario más un
  banco de casos, con evidencia sobre outcomes (efectividad, innovación, eficiencia) y sobre
  barreras institucionales (liderazgo, capacidad, financiamiento, oportunidad de iterar). ⚠️ Con un
  detalle que la vuelve menos útil de lo que parece: **se redactó entre sept-2023 y mar-2024 y se
  publicó en jul-2025** — su corpus es **anterior a la IA generativa**.
- La infraestructura sigue viva: SDN (2004), conferencia global 2026, y una edición de *Touchpoint*
  titulada precisamente "From AI to Synthetic Services" (F-395).
- **Y hay tribuna local**: existe una comunidad de service design en **Lima desde junio de 2017**,
  activa en 2026 con su Jam de 48 horas (dentro del Global Service Jam simultáneo en 85 ciudades) y
  sesiones periódicas (F-394). Directamente relevante para el proyecto: **el service design en Perú
  no hay que fundarlo, hay que encontrarlo.**

**En contra de "es madurez":**

- Búsqueda adversarial explícita: una figura reconocida *dentro* de la disciplina describe el campo
  en "una verdadera **crisis de la práctica**" (F-393), atribuida a que las organizaciones
  invirtieron en diseño durante el crecimiento **sin posicionar los equipos ni demostrar valor**, y
  a que el design thinking no cumplió su promesa. Es el mismo diagnóstico que la pista de negocio de
  la iteración 1 encontró en las consultoras (IDEO −67%, Veryday cerrada, R/GA a PE).
- **No existen métricas públicas de membresía de SDN** ni de presupuesto de service design en
  organizaciones. Se buscaron y no aparecieron: H18 **no se puede cerrar con dato duro en ninguna
  dirección**.

⭐ **Veredicto honesto:** *silencio social ≠ irrelevancia* queda **respaldado**. *Silencio social =
madurez* queda **sin respaldo, y con contraevidencia interna**. La lectura que sobrevive es la
tercera: el service design tiene instituciones, evidencia y comunidad, pero **no tiene un relato con
el que participar de la conversación identitaria del gremio** — y por eso es invisible justo en el
momento en que el gremio decide quién es. H18 → `parcial`.

### 10.3 📈 Design systems y productividad: una cifra reciclada y un mecanismo que reconcilia

**Lo que no apareció (y se buscó):** ninguna replicación independiente del efecto de un design
system sobre el tiempo de desarrollo. **H6 sigue abierta tras dos iteraciones de búsqueda.**

**Lo que sí apareció:**

- **Quinta cadena de eco de cita.** El "**135% de ROI**" que circula en 2026 no es un estudio: es una
  **calculadora** publicada en 2022 (F-397) que modela US$646.000 → US$1.517.400 de ahorro estimado
  a cinco años, alimentada con cifras autorreportadas por la industria. Nadie ejecutó y midió.
  ⭐ **El patrón importa más que la cifra**: cuando el 671% se desmontó, la industria **no dejó de
  citar cifras — cambió de cifra**. De ahí sale H22 y la regla C17.
- **Dato de supervivencia**, que es más informativo que cualquier ROI: la satisfacción con el buy-in
  deja insatisfecho a ~40% de los equipos (la caída de 42% a 32% solo circula en un blog de terceros; corregido 2026-10-12) y **solo ~40% de los design systems sigue activo pasados 18 meses**
  (F-396). ⚠️ Fuente con interés del emisor directo (vende la herramienta) — lo que hace *más*
  creíble el dato negativo, no menos.
- ⭐ **El hallazgo más valioso de la corrida para el resto del proyecto: el impuesto de
  verificación.** La iteración 1 dejó abierta la divergencia ⚔️ entre METR (−19% de velocidad real
  en devs expertos) y el preprint de IA alineada a design system (−46/−69% de time-to-delivery), y
  aventuró a mano que la diferencia estaba en la madurez del código base. Ahora eso tiene nombre y
  cifras (F-388): **~4,3 minutos de verificación por sugerencia para un senior vs. ~1,2 para un
  junior, escalando con la madurez del código base hasta exceder el ahorro de generación**; juniors
  ganan 30-40% pero con atrofia de habilidad. **Los dos estudios no se contradicen: miden extremos
  opuestos de la misma curva.** ⚠️ Preprint sin revisión por pares — es la mejor explicación
  disponible, no un hecho establecido (H19).

### 10.4 📱 El barrido en español y portugués: H17 refutada, y lo que quedó vale más

La iteración 1 declaró su sesgo anglosajón como limitación crítica y apostó a H17: *el ciclo
identitario del gremio llega a LatAm desfasado, atenuado, o el mercado local ni participa.*
**Es falso en las tres formas.**

- **Adopción: LatAm va por delante, no por detrás.** El estudio brasileño (F-389, Môre + IBPAD,
  **N=823 profesionales**, nov-2025) reporta **94% de adopción de IA** entre diseñadores brasileños
  y 66% de uso diario — **por encima del 89% anglosajón** (F-280). Es, además, **la única evidencia
  local con muestra propia** hallada en toda la corrida.
- **Conducta: la compresión del rol ya se ejecutó en la región.** MercadoLibre —la empresa
  latinoamericana más valiosa en bolsa— desvinculó **119 personas del área de UX** (32 en Argentina)
  en una reestructuración que **integra explícitamente los roles de diseño y contenido** apoyándose
  en IA; los perfiles más golpeados fueron **UX writers y especialistas de contenido** (F-391).
  ⭐ Aplicando C6 (contar conducta, no volumen): esto pesa más que todo el discurso anglosajón sobre
  "el fin del UX designer" junto, porque **es una decisión corporativa fechada y documentada, no una
  queja de LinkedIn**.
  ⚠️ **Corregido en la iteración 3 — leer junto con §11.6 y C21.** MercadoLibre **desmintió
  oficialmente** la atribución a IA: declaró que fue una "reorganización interna para integrar
  Diseño y Contenido" y que representó "menos del 0,09% de su plantilla de más de 125.000
  empleados" (F-419), mientras ex-empleados sostienen que parte de su trabajo era entrenar los
  sistemas que los reemplazaron. **El despido es un hecho; la causa está en disputa.** Deja de ser
  "conducta corporativa limpia" y pasa a ser **caso contestado**, con el mismo descuento por
  *scapegoating* que la iteración 1 aplicó al mercado anglosajón (F-282). **La refutación de H17 se
  sostiene igual**, pero sobre otras patas: el estudio brasileño con muestra propia (F-389) y ahora
  también Livspace en India (F-416). La ironía es que la iteración 1 registró que el daño se concentraba en
  juniors; aquí el rol eliminado es **una especialización entera**.
- **Discurso: existe, y es traducción.** El vocabulario anti-slop, la "fatiga visual post-IA" y el
  neo-brutalismo circulan en medios masivos en español (F-390), y el debate identitario tiene sus
  propios podcasts en español. Pero el material **cita cifras anglosajonas de emisores interesados**
  —el 89% de Figma reaparece en prensa argentina y en escuelas españolas— **sin el descuento que la
  propia fuente exige** (C4).

⭐ **Lo que quedó vivo es mejor que la hipótesis refutada.** La distinción útil no es *anglosajón vs.
LatAm* sino **conducta local vs. marco importado** (H20): la región **genera datos y decisiones
propias** y **consume interpretación traducida**. Y de ahí sale el hallazgo más accionable para el
proyecto: en Brasil, **60% de los diseñadores usa IA en cuentas personales sin lineamiento
corporativo y solo 14% recibió capacitación de la empresa** (F-389). **El problema no es adopción,
es gobernanza** (H21) — lo cual, en un negocio asegurador donde el dato del cliente es sensible por
definición, no es un detalle de RRHH.

⚠️ **Nota de honestidad sobre este barrido:** el dato duro local es **brasileño y argentino**. Para
**Perú** solo se hallaron portales de empleo y una comunidad de service design (F-394): **no se
encontró ningún estudio peruano con muestra propia** sobre diseñadores e IA. El sesgo geográfico se
redujo, no se eliminó.

### 10.5 📈 Figma antes del 5 de agosto: H13 sigue en pie y se resuelve en una semana

Al 13-jul-2026 FIG cotizaba ~**US$23,57**, con rango de 52 semanas de **US$16,60 a US$142,92** —
**~−83/−84% desde el pico y todavía bajo el precio de IPO (US$33)** — mientras el consenso de
analistas apunta a US$30,56 a 12 meses, con 5 compras y **0 ventas** (F-398). El desacople que la
iteración 1 identificó **se mantiene intacto**: 46% de crecimiento interanual y NDR de 139% (el más
alto en más de dos años) conviviendo con una acción por debajo de su precio de salida.

**H13 se resuelve el 5 de agosto de 2026** (reporte Q2) y en los 90 días siguientes. La condición
está fijada de antemano: *si Figma reporta ≥40% de crecimiento y la acción no recupera sobre US$33,
el mercado descuenta disrupción por IA, no ejecución.* La iteración 3 debe leerlo y cerrarla.

### 10.6 Limitaciones de la iteración 2

- ⚠️ **Ninguna de las 19 fuentes nuevas se leyó en texto completo.** El proxy devolvió **403 en
  todos los intentos de lectura directa**: arXiv, ACM Digital Library, MDPI, gov.uk, IBPAD, Xataka.
  Todo el §10 está construido sobre **abstracts y snippets de búsqueda**. Consecuencias concretas:
  no se verificaron tamaños de muestra ni métodos línea por línea; **las cifras del PDER, del estudio
  brasileño y de la revisión sistemática de consistencia deben revalidarse antes de publicarse en un
  entregable**. Es la misma limitación de la iteración 1 y **no mejoró**: asumirla como estructural
  del entorno, no como mala suerte.
- **Autoría no verificada** en 6 de las 19 fuentes nuevas (F-381 a F-386, F-388): citadas por título,
  venue y URL, sin inventar nombres.
- **El barrido hispanohablante no alcanzó a Perú con dato propio** (ver §10.4).
- **H18 quedó sin dato duro**: no hay métricas públicas de membresía ni de presupuesto de service
  design. Se buscaron.
- **La pista social sigue midiéndose por frecuencia y no por validación**: sin acceso a X ni Reddit,
  no se pudieron contar reacciones ni leer hilos de primera mano. La compensación deliberada de esta
  iteración fue **apoyarse en conducta observable** (despidos de MercadoLibre, eventos con fecha de
  Service Design Lima, control de transparencia de Apple en la iteración 1) en vez de en volumen —
  lo cual es más sólido, pero mide otra cosa.
- **H16 (degradación del reporting) no se pudo avanzar** en esta corrida.

---

## 11. 🔁 Iteración 3 (2026-08-02) — la iteración en que el node se auditó a sí mismo

Corrida de `/trinidad` con el mismo mandato de **confrontar antes que buscar novedad**. Las tres
pistas se mantienen separadas. La corrida terminó siendo, sobre todo, un ejercicio de honestidad
hacia adentro: el mejor hallazgo de la iteración anterior no sobrevivió a la regla que el propio
node aplica a los demás.

**Resumen de la corrida en una frase por pista:**

- 🔬 **Empírica**: el mecanismo que la iteración 2 celebró **no tiene fuente** — y las dos ausencias
  que el node arrastra (longitudinal de generative UI, replicación de design systems) llegaron a su
  tercera confirmación consecutiva.
- 📱 **Social**: la sospecha sobre el corpus hispanohablante era correcta y **se quedó corta** — no
  solo cita lo anglosajón interesado, cita autoridades que no dijeron lo que se les atribuye.
- 📈 **Negocio**: el ROI del diseño **no rota, acumula** — las cinco cifras desmontadas siguen vivas
  en paralelo, ninguna retirada; y H13 llega a su fecha de vencimiento con la condición más limpia
  que ha tenido.

### 11.1 🔬 Tercera ausencia consecutiva: H3 y H6

**Generative UI (H3).** Tres búsquedas dirigidas ("longitudinal", "multi-session", "between-subjects
≥5 sesiones") y ningún estudio que califique. Lo más cercano: F-399, que compara cuatro condiciones
en horizonte corto (no repite tarea con la misma persona), y F-400 (ACM DIS 2025, N=37, journaling
de una semana), que es **formativo y cualitativo** — produce datos ricos sobre cómo los
profesionales usan la herramienta, pero **no compara generative UI contra UI estática en tiempo de
tarea ni en aprendibilidad**, que es lo único que movería la hipótesis.

**Design systems (H6).** Ninguna replicación independiente, por tercera vez. Lo que sí cambió es el
estatus del estudio existente: **F-259 dejó de ser preprint y fue aceptado en SBES 2026** (venue con
arbitraje por pares de la SBC). Sube el rigor del estudio; **no sube su generalizabilidad** — misma
muestra, misma empresa, sin devs externos. ⭐ *El campo institucionaliza el mismo estudio en vez de
replicarlo*, mientras sigue publicando calculadoras: F-425 usa el 135% de 2022 como método vigente
para "medir el ROI de un design system en 2026".

⚠️ **Lo que estas dos ausencias ya son.** Tres barridos independientes, con términos distintos, en
tres momentos distintos, y cero resultados en ambos casos. Eso deja de ser azar de búsqueda y pasa a
ser una **propiedad del campo**: se están adoptando dos paradigmas (interfaces generadas, design
systems como palanca de productividad) con una base de evidencia que, por construcción, no puede
detectar su modo de falla principal. Aplicando C7, la ausencia es el hallazgo — y a la tercera, es
un hallazgo sólido.

### 11.2 🔬⚠️ El impuesto de verificación: el node se desmonta a sí mismo

**Este es el hallazgo central de la iteración 3, y es una corrección.**

La iteración 2 cerró celebrando que la divergencia ⚔️ de productividad con IA —METR (−19% de
velocidad real en devs expertos) vs. preprint DS-aware (−46/−69% de time-to-delivery)— por fin tenía
un mecanismo reconciliador con nombre y cifras: el **impuesto de verificación**, ~4,3 min por
sugerencia para seniors vs. ~1,2 para juniors, escalando con la madurez del código base.

**Esa cifra no tiene fuente primaria rastreable.** El rastreo la encuentra repetida casi palabra por
palabra en Sonar, Faros AI, Augment Code, Entrepreneur y mariothomas.com; el punto más profundo
alcanzable es un artículo de **DZone** (F-404) que dice literalmente *"in a recent study of 250
developers across five organizations…"* **sin nombrar autor, institución ni enlazar el estudio**. No
existe paper, preprint ni informe con ese N y esas cifras. Y el preprint que el node citaba como
mecanismo (F-388) resultó ser de **autor único** y de naturaleza **sintética** — un marco teórico
que cita cifras de terceros, **no un experimento propio con muestra declarada**.

⭐ **Por qué importa más que la cifra.** Es la **sexta cadena de eco de cita** del node (§2.5) y la
primera que estaba *adentro*. Las cinco anteriores eran ajenas: el node las cazó aplicando C3 y C17.
Esta entró sin resistencia, y la razón es específica y generalizable: **cerraba una herida abierta**.
Resolvía una contradicción que el node arrastraba desde la iteración 1, y esa condición —no lo
espectacular de la cifra— es lo que bajó la guardia. De ahí sale **C20** y la hipótesis **H24**, que
predice que los próximos errores del node volverán a concentrarse en hallazgos reconciliadores.

**Qué queda en pie y qué se cae.**

| Afirmación | Estado tras la iteración 3 |
|---|---|
| La IA desplaza esfuerzo de generación hacia verificación | ✅ **Se sostiene** — telemetría independiente con N grande: **+98% de PRs y +91% de tiempo de revisión** (F-406) |
| La magnitud es 4,3 min (senior) vs. 1,2 min (junior) | ❌ **Se cae** — sin fuente primaria (F-404) |
| El impuesto crece monótonamente con la seniority | ❌ **Se rompe** — F-407 (400 revisores, 11.429 revisiones): la aprobación **sube +14,5 pp** a través de deciles de exposición; **más experiencia acumulada → menos escrutinio**, no más |
| Existe un experimento que manipule madurez del código base como factor | ❌ **No existe** — todo lo disponible es yuxtaposición narrativa post-hoc de estudios distintos |

⚠️ **Alerta de blindaje.** Existe un preprint riguroso titulado *The Verification Tax: Fundamental
Limits of AI Auditing in the Rare-Error Regime* (F-405), que es un **paper teórico-estadístico sobre
límites de auditoría de calibración de modelos** y **no tiene ninguna relación** con tiempos de
revisión de código. Se registra explícitamente porque una búsqueda futura por "verification tax"
lo devolverá y **podría prestarle su autoridad a una cifra que no la tiene** — que es exactamente el
mecanismo de C19.

De la inversión del signo (más exposición → menos escrutinio) sale **H26**, que si se sostiene
cambia el diseño de cualquier control de calidad sobre trabajo asistido por IA: **el riesgo no está
en el novato que no sabe revisar, sino en el veterano que ya se acostumbró.**

### 11.3 🔬 H5: llegó el estudio que pedía, y la hipótesis acierta el signo pero falla la escala

H5 predecía que en cualquier estudio que midiera **a la vez** desempeño objetivo y percibido, la
mejora subjetiva excedería a la objetiva en **≥20 pp**. Era "la hipótesis de mayor valor
destructivo" del node.

Apareció el estudio del tipo exacto que pedía, y es la mejor fuente nueva de esta iteración:
**F-401** (*Computers in Human Behavior*, vol. 175, peer-reviewed, Study 1 + réplica interna,
**N=452**). Con asistencia de IA, el desempeño objetivo en razonamiento lógico sube **~3 puntos**
sobre la norma poblacional y la auto-estimación sube **~4 puntos**. **La brecha existe y va en la
dirección predicha, pero es de un solo dígito — no de ≥20 pp.** Hallazgo adicional notable: el
efecto Dunning-Kruger **desaparece** con uso de IA — la herramienta nivela el desempeño real sin
corregir la sobreestimación.

**F-402** replica el diseño ideal (objetivo + percibido + fisiológico: rúbrica, NASA-TLX, EEG,
eye-tracking, EDA, HRV) en dominio de código, multisitio: con IA, razón θ/α de EEG más baja y
parpadeo más alto, consistente con **menor compromiso cognitivo al delegar**.

⭐ **Lo honesto es decir que el node se pasó de rosca.** El umbral de ≥20 pp era una apuesta, no una
predicción fundada, y venía de la brecha de ~39 puntos del RCT de METR (C11) — un caso extremo
tratado como si fuera el caso típico. **C11 sigue en pie** (desconfiar del autorreporte de
productividad), pero su magnitud debe leerse como techo, no como norma. H5 pasa a `parcial` con el
umbral marcado para reformulación. Sigue sin existir la medición en el dominio propio: **ningún
estudio mide objetivo y percibido en design systems o madurez de diseño**.

### 11.4 🔬 H7: la dicotomía puede estar mal planteada

**F-403** (CHI 2026, peer-reviewed, N=48, 10 apps, Material 3 vs. Material 3 Expressive) encuentra
fijación visual correcta **33% más rápida**, tarea **20% más rápida** **y** calificaciones más
positivas. Es decir: el rediseño mejoró **fluidez y estética a la vez**.

No es el experimento que H7 pide (aislar las dos variables), pero es informativo de otro modo:
sugiere que en sistemas de diseño maduros **fluidez y atractivo no suelen ser un trade-off**. La
formulación "fluidez *contra* ornamento" describe bien un caso de falla conocido (Liquid Glass,
F-272, donde el ornamento se comió el contraste) y mal el caso general. **C12 no se toca** —la
evidencia de que buena parte del "efecto estética" es fluidez de procesamiento sigue firme (F-249)—
pero **H7 necesita reformularse antes de seguir buscándola**: la pregunta útil no es *¿cuál gana?*
sino *¿en qué condiciones se sacrifica una por la otra?*

### 11.5 📱 La auditoría hispanohablante: H20 al 100%, y algo peor que el sesgo del emisor

La iteración 2 dejó H20 como su hipótesis más prometedora: *la conducta es local, el marco es
importado*, con la predicción de que **>70%** de las cifras citadas en piezas hispanohablantes de
tendencias 2026 vendrían de emisores anglosajones con interés comercial.

**Auditoría de ~20 piezas en español y portugués. Resultado: 13/13 cifras con atribución (100%)
provienen de emisores anglosajones con interés comercial directo** — Gartner, Forrester, Baymard,
Google, Designer Fund, Adobe, Canva, Pinterest. **Cero** piezas citaron un estudio, encuesta o dato
con muestra propia en español o portugués. **H20 pasa a `respaldada`, con la predicción superada.**

| Cifra citada | Emisor atribuido | Interés comercial | Nota |
|---|---|---|---|
| "+60% de tareas de diseño con IA para 2026" | Gartner | vende investigación | ⚠️ **no rastreable** (F-418) |
| "+80% de productos con IA generativa en la capa de interfaz" | Gartner | ídem | ⚠️ **no rastreable** |
| "68% de empresas con design systems asistidos por IA" | Gartner | ídem | ⚠️ **no rastreable** |
| "$1 en UX devuelve $100" | Forrester | reporte tras paywall | ya desmontada en iter. 1 (F-268) |
| "~70% de abandono de carrito por usabilidad" | Baymard | vende informes por suscripción | — |
| Adopción de IA 54% (2025) → 91% (2026) | Designer Fund (VC) | tesis de inversión | F-410 |
| Claude 78% vs. ChatGPT 65% entre diseñadores | Designer Fund | ídem | F-410 |
| "Cansancio de la perfección IA" como tendencia | Pinterest, Canva, Adobe | venden generación con IA | F-411 |
| "+30% de búsquedas de texturas realistas" | Canva | sobre su propia base | no auditable |

⭐ **Y el hallazgo que no estaba en la hipótesis: tres de esas cifras se atribuyen a un Gartner que
nunca las publicó.** La búsqueda del reporte primario (F-418) encontró predicciones reales de
Gartner con "60%", pero sobre **temas distintos** (abandono de proyectos de IA, equipos de
ingeniería más pequeños, adopción de agentes) — **ninguna sobre tareas de diseño**. Esto es un fallo
de un orden peor que el sesgo del emisor: contra el emisor interesado sirve descontar (C4); contra
la **autoridad prestada** descontar no alcanza, porque no hay nada que descontar. De ahí salen
**C19** y **H23**.

⚠️ **Matiz honesto que corrige el titular hacia abajo.** De las ~20 piezas, **solo 5 anclan sus
afirmaciones a alguna cifra con fuente nombrada**. Las otras **15 (75%) no citan absolutamente
nada** — ni bueno ni malo: afirman tendencias ("el minimalismo sigue ganando fuerza", "la tipografía
audaz rompe normas") sin ningún aparato de evidencia. **El problema del corpus regional no es solo
importar el marco: es que tres cuartas partes no fingen siquiera tener una fuente.** De ahí sale
**H25**, que probablemente determina más el nivel de la conversación regional que H20 misma.

### 11.6 📱 El eje se normaliza — y el caso testigo se disputa

**Lo que cambió en el eje dominante.** La iteración 2 encontró el gremio en modo ansioso-defensivo.
La iteración 3 encuentra el mismo eje 🔥 pero con dos movimientos:

1. **Normalización institucional.** Figma Config 2026 (23-25 jun, +8.000 asistentes) integró la IA
   como *default*, no como amenaza: **Figma Make** (con Claude), **Figma Motion**, 20+ herramientas
   de imagen (F-412). El registro pasó de *"¿nos va a reemplazar?"* a *"así se trabaja ahora"*. Es
   un eje nuevo en la tabla de §3.
2. **Anticuerpo del propio ciclo.** El discurso "el diseño ha muerto" sigue caliente, pero **ya
   genera su propia refutación desde adentro**: múltiples piezas de 2026 lo llaman "el truco de
   engagement más viejo del mundo" y documentan que se repite cada pocos años (F-415). La
   iteración 1 estableció que el ciclo es **estacional** (C5); la iteración 3 muestra que **la
   comunidad lo nombra activamente como manipulación retórica**, no solo que se repita.

**Y la corrección adversarial más importante de la pista social: MercadoLibre desmintió.** La
iteración 2 usó los 119 despidos de UX como **el ejemplo más limpio de C6** ("contar conducta, no
volumen") para refutar H17. La búsqueda adversarial de esta iteración encontró el desmentido
oficial: la empresa declara que fue una "**reorganización interna para integrar Diseño y
Contenido**" y que representó "**menos del 0,09% de su plantilla** de más de 125.000 empleados"
(F-419); ex-empleados sostienen que parte de su trabajo era entrenar los sistemas que los
reemplazaron.

⭐ **El despido es un hecho; la causa está en disputa — y era la causa la que hacía el argumento.**
Es el mismo patrón de *scapegoating* que Gallup documentó en el mercado anglosajón (F-282), ahora en
español y en la dirección opuesta: allá las empresas **atribuían** despidos a la IA para justificarse,
aquí la empresa **niega** la atribución para no cargar con el costo reputacional. En ambos casos la
declaración corporativa está interesada. De ahí sale **C21**.

**La refutación de H17 se sostiene igual**, pero sobre otras patas: el estudio brasileño con muestra
propia (F-389, N=823) y ahora también **Livspace en India** (~1.000 despidos, ~12% de la plantilla,
funciones de diseño incluidas — F-416), que amplía el patrón de compresión del rol a un tercer
mercado emergente. ⚠️ Con una ironía que refuerza H20: **la conducta es india, la cobertura es solo
en inglés.**

### 11.7 📱 Seniority, y el negocio de los dos bandos

**H10 pasa a `parcial`** con la primera evidencia segmentada por seniority en tres iteraciones. No es
cuantitativa, pero viene de una plataforma con **verificación de identidad corporativa** (Blind,
F-414), lo que la hace más creíble que un hilo anónimo: seniors describen el mercado como *"pésimo
si eres junior o recién graduado; si eres senior o superior, no es ideal pero está cerca de lo
normal"*. Consistente con F-280/F-301, ahora con testimonio por nivel en vez de encuesta agregada.
Sigue sin existir la encuesta segmentada por años de experiencia **con N reportado**.

**H11 pasa a `parcial`, y se amplía.** Auditoría de n≈8 piezas del ciclo "UX is dead": **~60-70%
tiene incentivo comercial identificable** en el formato o el publisher — bootcamp, Substack de pago,
YouTube monetizado, agencia de contenido (F-415). Proporción aproximada sobre muestra de
conveniencia, declarada como tal.

⭐ **Lo que no estaba en la hipótesis: el discurso que *corrige* el pánico también tiene modelo de
negocio.** Varias de las piezas que dicen "dejen de decir que el diseño murió" son ellas mismas
newsletters o bootcamps que necesitan tráfico. **El descuento por incentivo (C4) aplica a los dos
bandos, no solo al alarmista** — y eso significa que el volumen del debate identitario, en cualquier
dirección, es una medida pobre del estado real del oficio.

**H9 sigue `abierta`.** No apareció medición nueva específica de diseñadores. Sí un patrón análogo en
población general española que refuerza el mecanismo: **49% rechaza o expresa preocupación** por la
IA a inicios de 2026 mientras **82% ya la usa** para trabajar mejor (F-417). Es analogía de refuerzo,
no confirmación: mide otra población.

**H21 sigue `abierta`, y por tercera vez en blanco.** No existe (o no es alcanzable) un estudio
peruano ni hispanoamericano con muestra propia sobre *shadow AI* en diseño/producto. Lo más cercano:
EY reporta que 70% de grandes empresas peruanas subirá presupuesto de IA (n=250 directivos) — pero
eso mide **adopción organizacional, no uso sin lineamiento**. ⭐ **Recomendación operativa: dejar de
barrer genéricamente.** Tres iteraciones con términos distintos y cero resultados no distinguen "no
existe" de "existe tras un muro que el proxy no cruza". Para moverla hace falta una fuente primaria
distinta: contacto con una asociación de diseño peruana, o que el propio proyecto corra la medición
interna. **Sigue siendo la hipótesis más accionable para el contexto Rimac** — un negocio asegurador
donde el dato del cliente es sensible por definición no puede tener 60% de uso de IA en cuentas
personales sin saberlo.

### 11.8 📈 Figma en la víspera: H13 llega a su fecha con la condición más limpia que ha tenido

**H13 se resuelve el 5 de agosto de 2026** — tres días después de esta corrida. Estado al corte:

| Dato | Valor | Corte |
|---|---|---|
| Precio de cierre FIG | **US$24,30** (bajo el IPO de $33) | 31-jul-2026 (viernes) |
| Precio objetivo promedio | **~$40 (mar) → $31-33 (fin de jul)** ⚠️ dispersión real entre compiladores ($30,56 / $32,67 / $36,11) | jul-2026 |
| Recomendaciones | **Primera venta** entre 16 casas (antes 0 ventas) | 19-jul-2026 |
| Guidance oficial Q2'26 | **$348-350M, ~40% YoY** | dado en el call de Q1 |
| Paid customers Q1'26 | ~690.000, **+54% YoY** | 31-mar-2026 |

⭐ **Con el guidance oficial en la mano la prueba queda perfectamente limpia**: *si el reporte del
5-ago cumple o supera $348-350M (~40% de crecimiento) y la acción aun así no recupera sobre US$33,
el mercado descuenta disrupción por IA, no ejecución.* La iteración 4 debe leerlo y cerrarla — es la
única hipótesis del tablero con fecha de vencimiento, y ya venció.

**Señal nueva y más fuerte que en la iteración 2**: la aparición de la primera recomendación de venta
y la caída sostenida del precio objetivo indican que el consenso se está moviendo de "comprar con
cautela" a un reparto más poblado de *holds*. Movimiento en ambas direcciones: BofA reinstauró Buy
$30 (tesis: "la IA es más *tailwind* que *headwind*"), **RBC cortó a $22** tras Config 2026
cuestionando el margen operativo no-GAAP guiado de solo **~9% por gasto en cómputo de IA** — es
decir, el escepticismo ya no es solo sobre la demanda, es sobre **la economía unitaria de responder
con IA** (F-421).

⭐ **Y el evento corporativo que le da cuerpo al descuento**: el CPO de Anthropic **renunció a la
junta de Figma el 16-abr-2026**, el mismo día en que trascendió que el siguiente modelo incluiría
herramientas de diseño competidoras; al día siguiente se lanzó **Claude Design**, con **+1M de
usuarios en su primera semana** (F-429). La caída de 6-7,7% que el node ya tenía registrada (F-318)
tiene detrás un hecho fechado y divulgado a la SEC, no solo un sentimiento de mercado.

**H16 sigue `parcial`, sin movimiento nuevo en Figma**: el Q1'26 reportó NDR (139%) y todos los
tramos de paid customers. Pero la tendencia gana un tercer caso fuera de Figma: **Accenture no
reporta Song como segmento SEC** (F-428), lo que vuelve "¿Song crece?" **estructuralmente no
respondible con datos públicos** — el mismo mecanismo que la fusión de segmentos de Adobe. Y Webflow
sumó un **segundo layoff (~20% de la plantilla, may-2026)** sin publicar ARR desde 2023.

### 11.9 📈 El ROI del diseño no rota: acumula. Y H15 recibe su primer contraejemplo

**H22 predecía que esta iteración encontraría una cifra nueva ocupando el lugar del "ROI del
diseño". No la encontró — y lo que encontró es peor.** Las cinco cifras ya desmontadas **siguen
todas vivas, circulando en paralelo**, cada una en su nicho de contenido, sin corrección alguna:

- **"$1 → $100" de Forrester (2016, tras paywall)**: descrito textualmente en 2026 como **"el
  benchmark estándar para justificar presupuestos de diseño"** (F-423).
- **Nueva capa de conflación**: el "83% de aumento de conversión por 10% de inversión en UX"
  atribuido a Nielsen y el "$1 ahorra $10 en desarrollo y $100 en mantenimiento" atribuido a
  Clare-Marie Karat — **ambas de origen anterior al año 2000**, recirculando sin fecha en contenido
  de 2026 (F-424). **Confirma la sospecha de la iteración 1**: el "100x de UX" conflaciona una regla
  de ingeniería de software con un ROI de inversión en diseño.
- **McKinsey +32/+56 pp (2018)**: sigue siendo la cifra, y en al menos un caso aparece **mal fechada
  como "McKinsey 2026"** — la cadena de eco no se corrige, **empeora en precisión**.
- **DMI Design Value Index**: circulan **228% y 211% mezclados como si fueran el mismo estudio**
  (son ediciones distintas, 2013 y 2016); **no existe edición posterior a 2016**. Diez años citando
  un índice que dejó de publicarse.
- **135% de design systems**: la calculadora de 2022 (F-397) sigue siendo la cifra que un vendor usa
  para "medir el ROI de un design system en 2026" (F-425).

⭐ **Ningún divulgador retiró ninguna cifra tras el cuestionamiento.** Eso reformula H22 y corrige
**C17**: la hipótesis de la *rotación* era demasiado generosa con el campo — suponía que responde a
la refutación cambiando de argumento. **No responde en absoluto: acumula.** (Nota metodológica
honesta: la rotación 671%→135% fue un evento de *años*; cuatro días entre corridas no dan margen
temporal para observar una nueva. La reformulación propone medir **semestre a semestre**.)

**H15 pasa a `parcial` con su primer contraejemplo en tres iteraciones**: **R/GA reporta +30% H2'25
vs. H1'25 y +25% YoY en Q1 2026** (F-422) — el único crecimiento de doble dígito hallado en el
universo de consultoras/agencias de diseño desde que existe el node. ⚠️ Con tres descuentos que lo
dejan **dentro de la cláusula de escape que la propia hipótesis preveía**: es autorreportado (empresa
privada, sin filing auditable), R/GA **nunca fue consultora de diseño puro** (agencia
digital/publicitaria con práctica de diseño), y la propia nota enmarca el giro como **pivote a IA y
consolidación**, no como recuperación del modelo. La predicción central sigue sin refutarse: **tras
tres iteraciones no ha aparecido ninguna consultora de diseño pura con crecimiento auditado**.

**H14 sigue `abierta`, con la evidencia adversarial más fuerte de la corrida.** La ronda de Lovable a
$13,2B **seguía sin cerrar** al 2-ago-2026 (F-426); el ARR autorreportado subió de ~$400M a ~$500M
con 146 empleados. Pero lo más informativo es una **conducta, no una cifra**: preguntada de forma
directa, **Lovable se negó a compartir su tasa de churn y su split mensual/anual** (F-427). No es que
el dato no exista — la empresa decidió no publicarlo. Barclays estima **tráfico −40% desde el pico** y
una valuación implícita de **$1,8B**, entre 3x y 7x por debajo de la narrativa de ronda. La compañía
sostiene NDR >100%, y un analista independiente señala la falla que el node ya anticipó: **NDR >100%
es compatible con churn masivo si los que quedan gastan mucho más.**

### 11.10 Limitaciones de la iteración 3

- ⚠️ **Tercera iteración consecutiva sin leer un solo texto completo.** El proxy devolvió **403 en
  todos los intentos** de lectura directa, en las tres pistas: arXiv, ACM DL, ScienceDirect,
  gartner.com, sec.gov, x.com, reddit.com y la mayoría de los sitios hispanohablantes auditados.
  Todo el §11 está construido sobre **abstracts y snippets de búsqueda**. ⭐ **Conclusión operativa
  que la iteración 4 debe asumir: esto es estructural del entorno, no mala suerte.** Deja de tener
  sentido declararlo como limitación cada corrida; hay que **diseñar el barrido asumiéndolo** —
  priorizar hallazgos negativos y rastreos de cadena de cita (que sí funcionan con snippets) sobre
  verificaciones de método que exigen el PDF.
- **Autoría no verificada** en F-399, F-400 y F-404 (DZone no declara autor). Las cifras de F-420,
  F-421 y F-428 se recuperaron **indirectamente vía prensa financiera**, no leyendo el filing:
  **revalidar contra EDGAR antes de publicarlas en un entregable**, igual que en las iteraciones 1
  y 2.
- **No se confirmó contra el programa oficial** que SBES 2026 haya aceptado y publicado el estudio de
  design systems (F-259): la evidencia es un resumen de búsqueda, no el *proceedings*.
- **Muestra de conveniencia en las dos auditorías clave**: H20 (N≈20 piezas, 13 cifras) y H11 (n≈8
  amplificadores) se recogieron por búsqueda, no por muestreo sistemático. El 100% y el ~60-70% son
  válidos **para el corpus auditado**, no generalizables sin sesgo de qué indexa el buscador.
- **No se pudo cerrar el rastreo de la cifra 4,3/1,2 min hasta el fondo absoluto**: sin leer el PDF
  de F-388 y el de DZone en texto completo, no se puede descartar que ambos compartan una fuente
  común más arriba en la cadena. Se reporta el límite alcanzable, no se cierra la pregunta — pero el
  límite alcanzable ya es suficiente para no usar la cifra.
- **H21 sigue sin resolverse por ausencia, no por negación** — tercera vez.
- **La pista social sigue midiéndose por frecuencia y no por validación**: sin acceso a X ni Reddit
  no se pudieron contar reacciones. La compensación deliberada de esta iteración fue apoyarse en
  **conducta observable** (Config 2026, despidos de Livspace, la negativa de Lovable a publicar
  churn) y en **plataformas con identidad verificada** (Blind) en vez de en volumen.

---

## 13. 🔁 Iteración 5 (2026-10-02) — confrontación de vencimientos

*Mandato: confrontar, no buscar novedad. Lectura vía `WebSearch` de resúmenes y snippets; **ningún documento primario se abrió íntegro** (los 8-K, el blog de METR y los arXiv aparecen en resultados, pero las cifras proceden de resúmenes que los citan).*

### 13.1 📈 H13: se cumplió la condición, pero por una razón distinta
- **Negocio.** Figma reportó el 5-ago-2026 ingresos de US$370,1M (**+48%**, tercer trimestre acelerando), NDR 136% y guía anual elevada a US$1.463-1.467M (F-469). La acción cayó ~17% tras el reporte y cerró a US$24,99 el 13-ago (F-470): **no** recuperó los US$33.
- **Lectura.** La letra de H13 queda `respaldada`. Pero la prensa atribuye la caída al **costo de IA sobre el margen bruto** (primer trimestre completo de créditos de IA), que no es el "descuento por disrupción de la demanda" que H13 predecía. Por eso se abre **H32** (impuesto de margen) en vez de cerrar la discusión.
- **Cautela.** El cierre del 13-ago viene de un agregador; no se verificó el precio de hoy.

### 13.2 📈📱 H14: señales cruzadas
- **Negocio.** Ronda de US$400M a US$13,3B (12-ago; F-471). ARR autorreportado ~US$500M (jun) y ~US$600M (24-sep; F-472): crecimiento sostenido. Pero tráfico −40% desde el pico, sin churn ni cohortes, NDR >100% alegado sin desglose.
- **Social (débil).** Un hilo de analista en X insiste en que el churn no publicado es la cifra clave (F-473, 🔴E). Es conversación, no evidencia.
- **Veredicto.** `abierta`. La prueba real (ARR a 12 meses de la ronda) no vence antes de ago-2027.

### 13.3 🔬 H19/METR: sigue sin resolverse
METR estima −18% (IC −38% a +9%) en devs que repiten y −4% (IC −15% a +9%) en devs nuevos, y **cambia el diseño del estudio porque el sesgo de selección vuelve difíciles de interpretar los datos** (F-474). Ambos intervalos incluyen el cero: el −19% de 2025 ya no es una cifra que se pueda citar sola. El conflicto con el estudio de design systems (−46% a −69%) queda **abierto**.

### 13.4 🔬 Generative UI (H3, H6, H33)
- F-476 (Google, 72 participantes): SUS 84 vs. 54 a favor de la interfaz adaptativa. **No mide uso repetido** y el control sale 'Pobre', lo que sugiere una línea base débil; el emisor tiene interés. Es la mitad "gusta más", ya documentada en §5.
- F-475 (*Design Theater*, preprint): ~25% de las justificaciones de diseño no se implementan, 34% en lo funcional. Refuerza que la interfaz generada y su discurso de diseño pueden divergir.
- **H3 y H6** no se mueven: nadie publicó el estudio de uso repetido ni la replicación independiente de design systems.

### 13.5 📈 H15 (consultoras de diseño): sin novedad verificable
La búsqueda devolvió solo notas de 2023 sobre IDEO. **No hay evidencia nueva** en esta iteración: el estado se conserva y se declara el hueco.

### 13.6 🔬 Auditoría hacia adentro (C20): F-442 se sostiene, con un matiz
- **Verificado:** es un RCT preregistrado (NCT06101251), N=1.449, publicado en *Accident Analysis & Prevention* (feb-2026), con reducciones relativas de 11-13% en exceso de velocidad, 16-21% en frenadas bruscas y 16-25% en aceleraciones, mantenidas en el seguimiento.
- **Matiz que el node sobreestimaba:** es un programa de UBI **simulado** (mensajes semanales e incentivo de hasta US$100, reclutamiento por redes sociales), no un seguro con prima real. La fila de §5 que dice "cambia la conducta **real** de manejo" debe leerse como **conducta de manejo medida por telemática**, no como efecto sobre siniestros ni sobre precio. Esto pesa para cualquier argumento de pricing con UBI en seguros peruanos.

### 13.7 Limitaciones de la iteración 5
- Cifras bursátiles y de ARR vienen de resúmenes y de prensa/blogs; el 8-K, el blog de METR y los arXiv no se abrieron íntegros.
- **La pista social es la más débil**: no se leyeron foros de diseñadores ni X/Reddit con volumen; solo un hilo (F-473) y cobertura de prensa.
- H15 quedó sin evidencia nueva y H3/H6 sin movimiento; no se buscó contraevidencia adicional sobre H32 más allá de la prensa.

### 13.8 🔁 Addendum 5b (2026-10-02) — H29 confrontada con el 2T de Lemonade
*Lectura vía `WebSearch` de resúmenes; la carta a accionistas no se abrió íntegra.* El 2T 2026 de Lemonade muestra un **loss ratio bruto de 60%** (con 7 pp de desarrollo favorable; ≈67% subyacente) frente al ~139% de combined ratio con el que el node la comparó en la iteración 4, prima en vigor **+32,5%** y **pérdida neta de US$43 M** (F-509); la acción cayó 24% el día del reporte (F-510). Root, en cambio, es rentable (combined ratio de 92,1%) pero sin crecimiento (F-481). **Lectura:** la hipótesis sale parcialmente respaldada —la siniestralidad es mejorable con disciplina— y parcialmente matizada: ninguna de las dos empresas combina rentabilidad y crecimiento; "disciplina de suscripción" explica la brecha de siniestralidad, no la de rentabilidad total.

---

### 13.9 ⚔️ Addendum 5i (2026-10-03) — confrontar hipótesis abiertas con su propio criterio de refutación
*Objetivo declarado: cerrar la brecha de autocorrección (6%, umbral de N5 = 20%). Para no convertir la
meta en sesgo, la regla de la corrida fue: **solo se confrontan hipótesis cuyo criterio de refutación ya
estaba escrito en la fila, y se registra el resultado sea cual sea.** Lectura vía resúmenes de
`WebSearch`; Wiley, Gestión, hubo-home y replicationindex bloqueados por la red.*

- **H22 → `refutada` (corrección contable, no evidencia nueva).** En la iter. 3 la predicción literal
  (la industria *sustituye* la cifra desmontada por otra) no se cumplió y la fila quedó en
  "🔄 Reformulada", un estado fuera del vocabulario del tablero que la sacaba de la cuenta de refutadas.
  Lo correcto es declararla refutada y abrir la reformulación como hipótesis propia: **H35** ("el campo
  no corrige: acumula"), con una prueba semestral que la vuelva falsable.
- **H30 → `refutada`.** El criterio de la fila era "se refuta si la mayoría reporta". En 5 metas
  públicas de innovación, **las 5 reportan**: Credicorp/BCP cada trimestre (8,1% en el 4T25, meta
  10% hacia 2026; F-529), DSM (meta 20%, reportó 21%; F-530), Croda (NPP 35% en 2024; F-531),
  Henkel (F-532, débil) y 3M (F-454). ⚠️ **El caso testigo peruano estaba mal:** F-460 decía que no
  había verificación pública del avance de BCP, y la hay en sus reportes a la SEC. La meta, además,
  figura como 2026 y no como 2025. ⚠️ **Sesgo de la prueba:** la muestra es de empresas que ya se sabía
  que publican la métrica. Una muestra aleatoria de metas anunciadas en prensa podría dar otro
  resultado, y esa sería la forma de reabrirla.
- **H23 → `parcial` (resiste).** Se rastrearon 9 cifras atribuidas a autoridades en listas de
  estadísticas UX 2026 (F-535). De las 6 rastreables, **4 no existen como se citan** y 2 sí
  (F-533, F-536). El hallazgo más útil es el mecanismo: no domina la invención pura sino la
  **mala atribución de cifras reales**. El "+83% de conversión" es de NN/g (F-534) y circula como
  de la IDF; el "80% de productos con personalización IA" mezcla dos predicciones reales de Gartner.
  Refuerza C19 sin ascenderla todavía (N=6).

- **H27 → `refutada`.** El criterio de la fila era "se refuta si ambas familias tienen la misma tasa
  de trazabilidad". En una muestra nueva de 5 cifras de fracaso muy citadas, **las 5 llegan a un
  documento identificable** (F-537 a F-541), igual que las 5 de éxito. El huérfano queda en 3 de 8
  (38%) contando los de F-444: no es el modo dominante. El hallazgo que queda es más incómodo y más
  general: **las cifras de fracaso colapsan en una fuente única mala igual que las de éxito**. El "70%
  del cambio" es Beer & Nohria sin datos (desmontado por Hughes, F-540). El "85% de la IA" es una
  predicción de sesgo de Gartner leída como medición de fracaso (F-538). El "90% de startups" es la
  premisa, no el hallazgo, del Startup Genome Report (F-541). El eco de cita no distingue el signo.
  ⚠️ **Juicio declarado:** la muestra es por notoriedad, no aleatoria. Si se suma la muestra original
  y se exige igualdad estricta de tasas (62% vs. 100%), quedaría `parcial`.

**Saldo:** 3 refutaciones (H22, H30, H27), 1 hipótesis que resiste (H23) y 1 nueva (H35). La
autocorrección del tablero pasa de 1/17 a **4/20 (20%)**, justo en el umbral de N5. **Advertencia
contra leer esto como logro:** una de las refutaciones es contable (H22) y dos dependen de muestras
no aleatorias (H30, H27). El umbral se cruzó con evidencia real pero delgada. Una réplica con muestra
aleatoria de cualquiera de las dos lo devolvería a 16%, y así debe registrarse si ocurre.

---

### 13.10 🧭 Addendum 5j (2026-10-11) — El recorrido del cliente se dibuja en órbitas, no en embudo
*Aporte del usuario: el gráfico "Representative orbital booking journey" del informe de McKinsey y Skift sobre viajes (sep-2026), leído completo (F-880); el resto del informe solo por resumen y prensa (F-876).*

**Qué muestra.** El recorrido de compra ya no baja en línea recta de la inspiración a la compra. Avanza en órbitas: en cada etapa la persona da vueltas, vuelve atrás y sigue buscando, incluso después de confirmar la reserva. El gráfico distingue cuatro etapas (inspiración, investigación, reserva y post-reserva) y la plataforma que predomina en cada una:

| Etapa | Plataforma predominante |
|---|---|
| Inspiración | Redes sociales, búsqueda con IA y buscador web, sin una dominante |
| Investigación | Buscador web |
| Reserva | Sitio directo del proveedor |
| Post-reserva | Búsqueda con IA |

Dos datos del mismo informe le dan escala: unos 65 puntos de contacto antes de reservar (frente a unos 45 en 2018) y un 78% que sigue investigando después de reservar (F-876).

**Qué tan sólido es.** 🟡 *Plausible, mal probado* en la escala de §5. El gráfico sale de un estudio de diario de Skift Research: 211 sesiones de planificación, registradas por 26 viajeros de EE.UU. según el resumen del informe (F-876). El propio informe lo llama "representativo", así que es una ilustración bien fundada, no una medición. Es evidencia cualitativa de un solo sector.

**Qué cambia para el diseño (deducción, no hallazgo).**
- **El mapa de recorrido debería dibujar bucles, no una línea.** Un mapa lineal esconde los momentos de reingreso, que es donde se pierde al cliente.
- **La post-compra es una etapa a diseñar, no un cierre.** Si el 78% sigue buscando después de comprar, la confirmación no termina la relación.
- **Cada etapa tiene su canal.** El canal de la compra (el sitio del proveedor) no es el de la inspiración (redes sociales e IA). Diseñar un solo canal para todo el recorrido deja huecos.
- **La memoria entre canales es la palanca principal.** McKinsey llama "impuesto de reinicio" a obligar al cliente a empezar de nuevo cuando un sistema no lo recuerda (F-876; ver [[conducta-humano-ia]] §2.11).

**Para seguros (inferencia).** La compra de un seguro es más rara y más larga que la de un viaje. Si el patrón se sostiene, las órbitas serían menos frecuentes pero más largas, y el asesor sería quien guarda la memoria entre canales. Queda como idea en prueba (H36). Toca de cerca el frente de service design (H18, §10.2) y la venta de seguros de vida ([[proyecto-back-to-basics-ffvv-vida]]).

---

## 14. 🔁 Iteración 6 (2026-10-12) — ¿qué es lo más relevante hoy en diseño de producto digital y de servicios?
*Origen: una pregunta del usuario a Mu ("¿Qué es lo más relevante hoy en diseño?") que el Criterio respondió solo en parte; propuso acotarla e investigarla con `/trinidad`. Las tres pistas se leyeron por resumen y resultados de búsqueda: el entorno no abre páginas web. Fuentes F-881 a F-909.*

**En pocas palabras.** Lo más relevante hoy no es lo más ruidoso. El gremio habla sobre todo de la IA en el proceso de diseño y del cambio de rol del diseñador. En cambio, la evidencia más sólida está en dos temas menos vistosos: la estructura de las decisiones (patrones oscuros y fricción) y la calibración de la confianza en interfaces con IA. El negocio crece, pero el costo de servir IA ya le pasa factura al margen.

### 14.1 🔬 Pista empírica — lo que tiene impacto medido
1. **Los patrones oscuros mueven decisiones, y la transparencia no basta para revertirlos.** Un experimento publicado en 2026 encontró que tres patrones oscuros subieron entre 6 y 12 puntos la inconsistencia de las elecciones de privacidad, y que un aviso de transparencia no la corrigió (F-881). En compras, aumentaron la compra impulsiva en todos los diseños probados (F-882). Es evidencia experimental revisada por pares.
2. **Lo que mueve la elección es la estructura, no el aspecto.** En el consentimiento de cookies, esconder opciones detrás de clics cambia la decisión; los retoques visuales casi no la cambian (F-883, experimento de campo aún sin arbitraje). Coincide con estudios previos sobre la fuerza de la fricción (§2.1) y con la revisión sistemática de 2026 (F-884).
3. **Más señales de incertidumbre no calibran mejor la confianza en la IA.** Es el experimento de 2026 que el Criterio pidió leer a fondo, hecho por Ojewale y colegas, preregistrado y con 495 personas (F-520). Las señales visuales hicieron a la gente más sensible a la precisión en lo que declaraba, pero también más dispuesta a aceptar respuestas equivocadas. Las advertencias verbales bajaron el acuerdo sin mejorar la discriminación entre respuestas buenas y malas. Las dos juntas produjeron la mayor sobreconfianza y la menor verificación. Dos estudios de 2026 van en la misma dirección: la incertidumbre por palabra sube el acuerdo con la IA (F-885) y el consenso de varias IA empuja a la sobredependencia (F-886). No son réplicas: son tareas distintas que convergen. Los tamaños de efecto de F-520 no se vieron.
4. **La IA en el servicio mejora la velocidad, no siempre la calidad, y no a todos por igual.** En un experimento de campo con unos 6.000 agentes de Alibaba, el asistente de IA mejoró tiempos y calificaciones sin cambiar la calidad objetiva; ganaron los agentes más débiles y empeoraron los mejores (F-888, preprint). Otro experimento de campo, publicado, encontró un efecto mixto (F-889).
5. **La IA en el proceso de diseño sube la novedad, no la utilidad.** Los anuncios hechos con IA se juzgaron más creativos, pero no más útiles ni más alineados con la marca (F-887, preprint con 36 personas).

**Contraevidencia que importa.** Un metaanálisis de 106 experimentos publicado en *Nature Human Behaviour* muestra que, en decisiones, la combinación humano-IA rinde en promedio peor que el mejor de los dos por separado; en tareas de creación, en cambio, gana (F-516). Las explicaciones de la IA suman poco (F-498), y el efecto promedio de los nudges se diluye al corregir el sesgo de publicación (F-16, F-17). En personalización hay fatiga: la respuesta cae con la exposición repetida (F-890). Cumplir el estándar de accesibilidad no siempre mejora las medidas de usabilidad. El service design sigue sin estudios cuasi-experimentales recientes: la revisión de 2021 halló resultados evaluados en menos de la mitad de los estudios (F-252), y en 2025-2026 no apareció ninguno nuevo.

### 14.2 📱 Pista social — de qué se habla
- 🔥 **La IA en el proceso y el prototipado con IA ("vibe coding")** dominan la conversación, con entusiasmo práctico y reservas de calidad: sirve para prototipar, no para producción. La encuesta de Figma muestra a los diseñadores menos convencidos que los desarrolladores (satisfacción 69% frente a 83%; solo 27% cree que la IA moverá las metas de la empresa este año) (F-892). La UX Tools Survey 2026 dice que la herramienta más usada después de Figma ya es una IA (F-895).
- 🔥 **El cambio de rol** ("builder", "design engineer") se discute con réplica. La tesis de que "el proceso de diseño murió" (F-897) tuvo respuestas de matiz (F-898). Las cifras que circulan (91% de uso semanal de IA) vienen de un solo informe de un fondo, repetido por la prensa (F-899, eco de F-410).
- 🌡️ **UX agéntica** (cómo diseñar el control y el consentimiento de los agentes): hay un marco de seis patrones muy reciclado (F-891), pero nadie lo ha validado empíricamente.
- 🌡️ **Homogeneización ("AI slop")**: la queja de que las interfaces generadas se parecen todas tiene respaldo académico incipiente (F-894).
- 🌡️ **Accesibilidad**: empeoró. El 95,9% de las portadas principales de la web tiene fallas detectables, contra 94,8% en 2025 (WebAIM 2026, vía F-896).
- 💬 **Backlash a rediseños** sin opción de volver atrás, con caídas de calificación en las tiendas de apps (F-900; cifras secundarias).
- **Ecos detectados:** el "32% de diseñadores confía en la IA" no coincide con la fuente que se le atribuye (F-893). Reddit, X y LinkedIn no se pudieron medir con la herramienta disponible.

### 14.3 📈 Pista de negocio — qué rinde
- **Lo más sólido son las empresas que cotizan.** Adobe reporta ingresos +13% en su último trimestre, aunque no publica cuánto factura su negocio de IA (F-901, documento ante la SEC). Figma mantiene una retención neta de 136% (ya en el registro). Wix crece 15% (F-902).
- **El costo de servir IA presiona el margen en tres empresas distintas.** Canva recortó su crecimiento esperado de 30% a ~20% por ese costo (F-903). El creador de apps con IA de Wix arrancó con margen bruto cercano a cero (F-902). Figma ya lo había mostrado. Esto **suma apoyo a H32**, la idea de que la IA no destruye la demanda de las herramientas de diseño sino que les cobra un impuesto de margen.
- **Los creadores de apps con IA crecen rápido, pero con cifras privadas o estimadas.** Replit vale US$9.000 millones sin publicar sus ingresos (F-904, F-905); Vercel tiene ~US$340 millones anualizados según una estimación de analista (F-906, F-907); Framer, ~US$50 millones (F-908). Ninguna publica su tasa de abandono de clientes.
- **El retorno del diseño sigue sin medición independiente reciente.** Las cifras de ROI que circulan vienen de estudios pagados por el proveedor. Los despidos de diseño en 2026 existen, pero la relación con la IA está en disputa (F-909).

### 14.4 ⚖️ Síntesis
- **Divergencia principal.** Lo que más se discute (la IA en el proceso, el nuevo rol del diseñador) es lo que tiene menos evidencia de impacto en el usuario final. Lo que tiene evidencia sólida (la estructura de las decisiones, la calibración de la confianza) casi no aparece en la conversación.
- **Convergencia.** Las tres pistas coinciden en un mensaje de cautela: "más" no es mejor. Más señales de incertidumbre no calibran mejor, más opciones generadas no son más útiles y más IA en el producto cuesta margen.
- **Respuesta prudente a la pregunta original.** Hoy, lo más relevante con impacto demostrado en diseño de producto digital es:
  1. Diseñar bien la estructura de cada decisión: dónde está la fricción y qué opción viene por defecto.
  2. Diseñar cómo se calibra la confianza en las interfaces con IA, sin depender de señales visuales.

  La IA en el proceso de diseño es lo más relevante por adopción, pero todavía no por impacto medido.

### 14.5 Limitaciones
- Todo se leyó por resúmenes: varios tamaños de efecto y tamaños de muestra quedaron sin ver, empezando por los de F-520.
- La pista social no pudo medir la validación en Reddit, X ni LinkedIn.
- Las cifras de negocio de las empresas privadas son órdenes de magnitud.
- La evidencia de service design sigue siendo la más delgada.

## 15. 🔁 Iteración 7 (2026-10-12) — ¿qué tendencia de diseño tiene efecto medido en conversión o retención?
*Origen: el Criterio de Mu propuso acotar la pregunta sobre qué priorizar en diseño y leer a fondo el metaanálisis de personalización que el cerebro ya tenía (F-519). Corrida de `/trinidad` con tres pistas en paralelo. Todo se leyó por resúmenes y fichas de revista: el entorno no abre páginas web. Fuentes F-910 a F-935.*

**En pocas palabras.** Muy pocas prácticas de diseño tienen efecto medido sobre conversión o retención real. Las más sólidas son tres: la opción que viene por defecto, la velocidad de la página y los rankings o recomendaciones personalizados. Casi todo lo demás mide intención declarada, viene de proveedores o no se replicó con muestras grandes. Además, los efectos de una prueba corta no predicen bien lo que pasa a largo plazo, que es justo lo que importa para la retención.

### 15.1 🔬 Pista empírica — qué tiene efecto medido
1. **La opción por defecto es la palanca más fuerte, pero su cifra está inflada.** Un metaanálisis de 58 estudios y más de 73.000 personas encontró un efecto grande sobre la elección (F-910). Sin embargo, muchos estudios son de laboratorio, y en los programas reales los nudges rinden cerca de un cuarto de lo que reportan los artículos académicos (F-21). Conviene esperar un efecto real, pero mucho menor.
2. **La velocidad de carga mueve ventas, y el paso de pago es el más sensible.** Un estudio con datos de transacciones de un minorista en línea mostró que las demoras reducen las ventas, con más fuerza en el pago (F-914). Es un estudio observacional con un método casi experimental. La cifra que circula ("10% más lento, 4,2% menos ventas") no se verificó en el artículo.
3. **Personalizar el orden de los productos funciona; personalizar el mensaje según la personalidad, no.** Un experimento aleatorizado con un minorista encontró más búsqueda y más compras con rankings personalizados que con el de más vendidos (F-915). En cambio, un metaanálisis de 41 estudios halló que adaptar mensajes a la personalidad tiene un efecto sobre la conducta casi nulo (F-911).
4. **La prueba social ayuda solo cuando hay suficientes reseñas.** En un experimento de campo, mostrar comentarios de clientes subió la conversión cuando había muchos y la bajó cuando había pocos (F-913). Mostrar prueba social sin volumen puede restar.
5. **La escasez y la gamificación suben la intención, no necesariamente la conducta.** Un metaanálisis de 131 estudios encontró que las señales de escasez aumentan la intención de compra (F-912). La gamificación en educación tiene un efecto pequeño sobre la conducta, y se vuelve inestable en los estudios más rigurosos (F-916).

**Lectura a fondo del metaanálisis de personalización (F-519).** Yeo, Chu y Li revisaron 53 experimentos con casi 12.000 personas y lo publicaron en el *Journal of Advertising Research* en 2025. Encontraron que la publicidad personalizada persuade más que la genérica, aunque con un efecto pequeño. El efecto pasa por la relevancia percibida: el anuncio parece más pertinente. La sensación de intrusión, en cambio, no tuvo un efecto detectable. Lo decisivo para esta pregunta es que el estudio mide actitudes e intenciones, no clics ni compras observadas. Por eso no prueba un efecto sobre conversión ni retención. La ficha del registro dice que la ruta por intrusión es "menor"; en realidad no fue significativa, y la ficha omite las intenciones y la magnitud. La ficha se corrigió el mismo día con autorización del usuario.

**Contraevidencia que importa.**
- Solo una de cada ocho pruebas A/B gana en su métrica principal, según 127.000 experimentos de Optimizely (F-922).
- Cerca de tres de cada cuatro experimentadores detienen la prueba en cuanto ven un resultado favorable, lo que infla los aciertos (F-918).
- Unas pocas ideas excepcionales generan casi toda la ganancia (F-917). Sumar muchos pequeños lifts no da lo que promete.
- El famoso "+55% de clics por redondear botones" se probó con muestras dos mil veces mayores: el efecto fue unas cien veces menor y compatible con cero (F-919).
- En Google, las pruebas cortas no predijeron el efecto a largo plazo cuando los usuarios aprendían a ignorar algo (F-934). Kohavi y colegas resumen: mover clics es fácil, reducir el abandono es difícil (F-933, F-923).

**Vacíos.** No apareció ningún estudio revisado por pares sobre simplificar formularios o el checkout, sobre el onboarding ni sobre el efecto de las rachas en la retención.

### 15.2 📱 Pista social — qué se repite
- 🔥 **"El 70% abandona el carrito"** es la cifra más repetida. Baymard la compila de 50 estudios, pero advierte que buena parte es navegación normal, no pérdida por mal diseño (F-920).
- 🔥 **"La personalización da 40% más ingresos"** circula en dos versiones. La original de McKinsey compara empresas que crecen rápido con las lentas; no mide un efecto causal (F-921).
- 🔥 **"El chat con IA multiplica por cuatro la conversión"** compara a quienes eligieron usar el chat con quienes no. Esa diferencia refleja sobre todo la intención previa de comprar (F-924). El tráfico que llega desde ChatGPT convierte algo más, pero con pocas sesiones y atribución dudosa (F-925).
- 🌡️ **El escepticismo sobre los A/B** gana terreno entre los propios practicantes: la mayoría de las pruebas no gana y muchas victorias publicadas no se repiten (F-922, F-923).
- 💬 **Patrones oscuros en la cancelación.** Una encuesta con escenarios mostró menos confianza y usabilidad declaradas (F-926). Nadie midió si retienen o espantan clientes en la realidad.
- 🌡️ **Duolingo y sus rachas** es el caso más admirado. Lo cuentan sus propios ejecutivos, con interés en el relato (F-927).

### 15.3 📈 Pista de negocio — qué resultados publican las empresas
- **Duolingo es el mejor caso público, pero no aísla el diseño.** Sus usuarios activos diarios crecieron 30% en 2025, y la empresa lo atribuye sobre todo a mejor retención (F-928, documento ante la SEC sin auditoría de esa métrica). Que la mayoría de sus usuarios tenga una racha larga es correlación: los leales acumulan racha (F-929). Su prueba interna más citada, separar la meta diaria de la racha, subió más de 40% la cantidad de usuarios con rachas de una semana (F-930, blog de la empresa). El crecimiento se frenó tras su anuncio de "primero la IA", sin datos que separen las causas (F-931).
- **Netflix estima que sus recomendaciones valen unos US$1.000 millones al año**, sobre todo porque reducen las cancelaciones. Las recomendaciones personalizadas se eligen tres a cuatro veces más que la lista de populares. Es una estimación de la propia empresa (F-935).
- **Booking.com corre más de mil experimentos a la vez**, pero no publica cuánto le suman (F-932).
- Las cifras más espectaculares (el "un clic" de Amazon, el +50% de Shop Pay) no tienen autor ni método. Los casos con nombre muestran efectos diez a cuarenta veces menores.

### 15.4 ⚖️ Síntesis
- **Convergencia.** Las tres pistas coinciden: los efectos reales de diseño sobre conversión son pequeños, dependen del contexto y se inflan al publicarse. Las prácticas con efecto medido sobre conducta real son pocas: la opción por defecto, la velocidad, los rankings personalizados y la prueba social con volumen suficiente.
- **Divergencia.** Lo que más se repite (checkout corto, personalización "+40%", chat con IA "x4") es justo lo que tiene menos evidencia causal. Esta brecha entre ruido y prueba es la misma de la iteración 6 (§14.4).
- **Respuesta prudente: qué priorizar.**
  1. Diseñar la estructura de la decisión: qué viene por defecto y dónde está la fricción.
  2. Cuidar la velocidad, sobre todo en el paso de pago.
  3. Personalizar el orden y las recomendaciones, no el tono del mensaje.

  Y medir la retención con pruebas largas o con grupos de control que se mantengan, no con lifts de una semana.
- **Para Rimac.** Ninguna de estas fuentes es de seguros. Las de mayor transferencia son la de opciones por defecto y la de velocidad; la de rachas y gamificación es la de menor transferencia, porque un seguro no se usa todos los días.

### 15.5 Limitaciones
- No se leyó ningún texto completo. Faltan los tamaños de efecto de varios estudios (rankings, prueba social, escasez y velocidad).
- La pista social no pudo medir Reddit ni LinkedIn.
- Las cifras de Duolingo y Netflix las reporta la propia empresa.
- Ninguna fuente estudia seguros ni Perú.

## Actualización 2026-10-25: las acusaciones de "AI slop" ya son vigilancia de pertenencia

Un análisis de 25 millones de comentarios de Hacker News y Reddit (2023-2026) encontró que las acusaciones peyorativas de
uso de IA crecieron más de diez veces, mientras insultos de control como "troll" no subieron; "slop" es 94% de esas
menciones [F-1059] (preprint, B). Los autores las leen como forma de marcar quién pertenece, no como detección de IA: no
verifican si el contenido acusado era de IA. Para producto: que te acusen de "slop" no prueba que tu contenido sea de IA.

## Conexiones

- [[rentabilidad-modelos-seguros|Modelos de seguros rentables: qué está medido]] — qué modelos de seguros son rentables y con qué evidencia (telemática, paramétricos, reaseguro), rescatado del registro de fuentes el 2026-10-25.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación: qué tiene impacto real y qué es propuesta]] — índice y criterio común: escala de madurez, hipótesis y reglas que estas iteraciones confrontan.
- [[conducta-humano-ia|Conducta humano-IA: cómo la IA cambia lo que la gente decide, cree y deja de pensar]] — la iteración 5 cruza sus hallazgos de confianza y adulación de la IA.
- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual (RIMAC): conocimiento construido]] — la iteración 5 corrige cifras que ese proyecto usaba para su piloto.
- [[diseno-servicios-politicas-salud|Diseño de servicios, políticas públicas y salud: qué impacto está medido]] — el recorrido del cliente (§13.10) continúa en el dominio de servicios.
