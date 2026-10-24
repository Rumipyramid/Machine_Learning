---
name: grimorio
description: El Grimorio es el ledger de fuentes de las crónicas paranormales (`cronicas/grimorio.md`), el equivalente del códice para ese mundo. Registra cada fuente usada en una investigación paranormal (rigor A-E + cercanía al hecho P1-P5) y responde consultas sobre lo ya registrado. Úsalo SIEMPRE que el usuario invoque /grimorio, pida ver o buscar fuentes de un caso paranormal ("qué fuentes tenemos de la casa X", "busca G-12", "qué documentos P1 hay"), o cuando `/aquelarre` u otra investigación paranormal use fuentes que deban quedar registradas.
---

# 📕 Grimorio — Ledger de fuentes de las crónicas paranormales

## Propósito

El grimorio cumple para las crónicas lo que el códice (`research/fuentes/codice.md`) cumple
para la investigación de seguros y diseño: ninguna fuente usada queda sin trazabilidad.

Está separado del códice a propósito. El códice alimenta a Mu, al grafo y a sus métricas de
madurez; mezclar en él testimonios de fantasmas distorsionaría esas cifras. Los dos ledgers
usan la misma disciplina: una fila por fuente, IDs que nunca se reusan, rigor declarado.

A diferencia de `cronista` + `codice`, este skill hace las dos cosas: **registra** y
**consulta**.

## Dónde vive

`cronicas/grimorio.md`. IDs `G-n` (correlativos, nunca se reusan ni renumeran). Si el
archivo no existe, créalo con la cabecera y las dos escalas de abajo.

## Contrato de campos

| Campo | Regla |
|---|---|
| **ID** | `G-n` correlativo. |
| **Autor** | Persona, medio u organismo. `Anónimo` si no se sabe. |
| **Año** | Año de la fuente; `s.f.` si no tiene. Para prensa de época, la fecha completa si se conoce. |
| **Fuente / Título** | Lo más específico posible (diario + fecha + titular; fondo + legajo). |
| **Pista** | 📜 archivo · 🗣️ voces · 🔬 escéptica. |
| **Rigor** | A-E con la rúbrica del códice, con justificación de una línea. |
| **Cercanía** | P1-P5 si la fuente habla del caso; `—` si es contexto general (p. ej. un paper sobre parálisis del sueño). |
| **Resumen breve** | 1-2 frases: qué dice y qué aporta al caso. |
| **Caso / expediente** | Expediente(s) que sustenta, en `cronicas/expedientes/`. |
| **URL / referencia** | Enlace o cita completa. Si la fuente también está en el códice, anota su `F-n`. |
| **Registrado** | Fecha `YYYY-MM-DD`. |

### Rigor A-E (misma rúbrica del códice)

| Nivel | Criterio |
|---|---|
| 🟢 A | Académico peer-reviewed, datos primarios, método explícito. |
| 🔵 B | Archivo u organismo oficial, documento público con procedencia. |
| 🟡 C | Investigación con método propio no auditable (investigador escéptico o parapsicológico con protocolo declarado, libro de historia local con fuentes). |
| 🟠 D | Prensa, documental, programa de TV o blog que cita a otros sin método propio. |
| 🔴 E | Testimonio anónimo, foro, video viral, contenido sin origen verificable. |

### Cercanía al hecho P1-P5

| Nivel | Qué es |
|---|---|
| P1 | Documento primario contemporáneo al hecho (expediente, acta, partida, foto o grabación original con procedencia). |
| P2 | Prensa de la época o testimonio registrado poco después del hecho. |
| P3 | Testimonio de primera mano, identificado, recogido después. |
| P4 | Relato de segunda mano o recopilación posterior (libro de leyendas, TV, nota retrospectiva). |
| P5 | Amigo de un amigo, anónimo o viral sin origen. |

Los dos ejes son independientes: un acta notarial de 1950 puede ser 🔵 B · P1, y un paper
excelente sobre infrasonido es 🟢 A · —.

## Registrar

1. Deduplica por URL o Autor + Año + Título. Si existe, agrega el nuevo caso en
   "Caso / expediente"; no dupliques la fila.
2. Asigna el siguiente `G-n` y llena todos los campos.
3. Si un testimonio nombra a una persona privada, regístralo por rol ("vecina antigua de la
   cuadra"), nunca con su nombre o datos de contacto.
4. Al cerrar, informa qué registraste: *"Registré 4 fuentes: G-7 (El Comercio, 1952, 🔵 B ·
   P2), …"*.

Nunca inventes una fuente, una fecha o una cita. Si no se encontró, no se registra.

## Consultar

- **Puntual**: por ID, autor, medio o palabra clave → tabla filtrada, solo columnas útiles.
- **Por caso**: qué sostiene un expediente; si el expediente cita un `G-n` que no existe en
  el grimorio (o al revés), repórtalo como inconsistencia.
- **Agregada**: distribución por rigor, por cercanía o por pista. Cuenta sobre la tabla real,
  no estimes. Una línea de lectura si algo destaca (p. ej. "el caso se apoya solo en P4-P5:
  no hay ningún documento de época").
- **Sin resultados**: dilo. "No está registrada" es una respuesta válida.
