---
tipo: tablero
titulo: "Tablero de hipótesis"
tags:
  - tablero
---

# Tablero de hipótesis

Las **31 hipótesis vivas** del proyecto, con la evidencia que cada una tiene
enganchada. Abre cualquiera para ver sus fuentes ordenadas por rigurosidad, o su grafo local
para ver con qué más se cruza.

| Estado | Hipótesis |
|---|---|
| refutada | 1 |
| parcial | 9 |
| abierta | 19 |
| respaldada | 1 |
| sin estado | 1 |

## Con Dataview

```dataview
TABLE WITHOUT ID file.link AS "Hipótesis", estado AS "Estado",
  fuentes AS "Fuentes", titulo AS "Enunciado"
FROM #hipotesis
SORT estado ASC
```

## Instantánea estática

| Hipótesis | Estado | Fuentes | Enunciado |
|---|---|---|---|
| [[H17]] | refutada | 2 | Desfase geográfico: el ciclo identitario del gremio llega a Perú/LatAm desfasado, atenuado, o el |
| [[H03]] | parcial | 6 | En tarea repetida a lo largo de ≥5 sesiones, la generative UI dará peor tiempo de tarea y peor a |
| [[H04]] | parcial | 2 | Añadir explicación ("¿por qué veo esto?") no mejora precisión ni calibración en decisiones de ba |
| [[H05]] | parcial | 2 | En cualquier estudio que mida a la vez desempeño objetivo y percibido, la mejora subjetiva exced |
| [[H10]] | parcial | 1 | La ansiedad gremial es un fenómeno de seniority, no de gremio: el daño está concentrado en junio |
| [[H11]] | parcial | 2 | El doom tiene modelo de negocio: la proporción de amplificadores del discurso "la IA mata al dis |
| [[H12]] | parcial | 2 | El backlash estético es señalización de estatus profesional, no preferencia de usuario |
| [[H15]] | parcial | 5 | La consultora de diseño pura no vuelve: ninguna de las cuatro publicará crecimiento de dos dígit |
| [[H16]] | parcial | 3 | El estándar de reporting se degrada donde hay presión de IA: si Figma deja de reportar NDR o pai |
| [[H18]] | parcial | 5 | El silencio del service design es señal de madurez (absorbido en operaciones), no de irrelevanci |
| [[H01]] | abierta | 1 | Un índice de empresas "design-centric" definido ex ante tendrá exceso de retorno sobre el S&P in |
| [[H02]] | abierta | 1 | El reporte de Forrester (2016) no contiene la afirmación "$1 → $100" en la forma en que circula |
| [[H06]] | abierta | 2 | El efecto de un design system sobre el tiempo de desarrollo será <20% (no 47%, no 69%) con contr |
| [[H07]] | abierta | 2 | En un A/B real, las variantes que aumentan fluidez (contraste, jerarquía, menos elementos) super |
| [[H08]] | abierta | 2 | En Perú, donde la causa #1 de desconfianza en seguros es la falta de información, la exposición  |
| [[H09]] | abierta | 2 | Brecha actitud-conducta en diseñadores: el discurso público es anti-IA/anti-slop pero la adopció |
| [[H13]] | abierta | 5 | Desacople valuación/desempeño: si Figma reporta ≥40% de crecimiento en Q2 2026 y la acción no re |
| [[H14]] | abierta | 4 | El ARR de vibe coding no retiene: si Lovable cierra a $12-13,2B, su ARR a 12 meses crecerá <50%  |
| [[H19]] | abierta | 2 | El impuesto de verificación es la variable moderadora: el efecto de la IA sobre la velocidad de  |
| [[H21]] | abierta | 0 | Brecha de gobernanza, no de adopción: en mercados emergentes el problema real no es que los dise |
| [[H23]] | abierta | 2 | Autoridad prestada: en el contenido de tendencias de diseño, una fracción no trivial de las cifr |
| [[H24]] | abierta | 0 | El hallazgo satisfactorio no se audita: los errores de este node se concentrarán en los hallazgo |
| [[H25]] | abierta | 0 | El corpus hispanohablante de tendencias no cita nada: más del 70% de las piezas en español/portu |
| [[H26]] | abierta | 1 | El escrutinio decae con la exposición, no crece con la seniority: frente a salidas de IA, lo que |
| [[H27]] | abierta | 1 | El huérfano de cita es el modo dominante de las cifras de fracaso, así como el eco de cita lo es |
| [[H28]] | abierta | 0 | La crisis le ocurre al eslabón que no puede fusionarse. En diseño colapsó el proveedor externo ( |
| [[H29]] | abierta | 1 | En insurtech el signo no es la pregunta: la condición lo es. Con la misma clase de evidencia aud |
| [[H30]] | abierta | 1 | Las metas de innovación se anuncian y no se reportan. Predicción: la mayoría de las metas públic |
| [[H31]] | abierta | 1 | En innovación lo importado es el marco, no la cifra. A diferencia del corpus hispanohablante de  |
| [[H20]] | respaldada | 2 | La conducta es local, el discurso es importado: LatAm/España generan evidencia y decisiones prop |
| [[H22]] | — | 1 | El ROI del diseño se cita por rotación, no por evidencia: cuando una cifra estrella se desmonta  |

## Reglas de criterio

| Regla | Título |
|---|---|
| [[C01]] | Argumentar por mecanismo, nunca por multiplicador |
| [[C02]] | Prometer acumulación, no transformación |
| [[C03]] | Cuando una cifra sea espectacular, rastrear la fuente primaria antes de usarla |
| [[C04]] | Descontar por incentivo del emisor, siempre |
| [[C05]] | Distinguir pico de tendencia |
| [[C06]] | Contar conducta, no volumen |
| [[C07]] | El hallazgo negativo es un hallazgo |
| [[C08]] | La explicabilidad genérica no calibra la confianza; la verificabilidad sí |
| [[C09]] | Sospechar de la interfaz que se reconfigura sola |
| [[C10]] | Más personalización no es mejor cuando la privacidad está saliente |
| [[C11]] | Desconfiar de toda métrica de productividad autorreportada |
| [[C12]] | Claridad antes que ornamento, con evidencia |
| [[C13]] | El anti-diseño sin disciplina destruye la usabilidad |
| [[C14]] | La evidencia causal más fuerte del poder del diseño es sobre su capacidad de daño |
| [[C15]] | Preguntar siempre qué se midió: preferencia, desempeño o consecuencia |
| [[C16]] | La curva antes que el signo |
| [[C17]] | El campo no corrige: acumula |
| [[C18]] | En LatAm, la conducta es local y el marco es importado; usar el primero, descontar el segundo |
| [[C19]] | Antes de descontar al emisor, verificar que el emisor lo haya dicho |
| [[C20]] | El chequeo de eco de cita se aplica también hacia adentro, y sobre todo cuando el hallazgo te conviene |
| [[C21]] | La conducta también se disputa: verificar la atribución, no solo el hecho |
| [[C22]] | Distinguir el eco de cita del huérfano de cita: contra el primero se lee el estudio, contra el segundo se exig |
