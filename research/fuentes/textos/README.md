# Textos completos de fuentes

Hoy el cerebro conoce la mayoría de sus fuentes por la ficha o por un resumen oficial: en el entorno en la nube solo
funciona la búsqueda web, no la lectura de páginas ni de PDFs. Esta carpeta y la lista priorizada
(`research/fuentes/lectura_pendiente.md`) existen para cerrar esa brecha.

## Dos caminos

1. **Subir el texto.** Deja aquí el PDF o el texto de una fuente con su código como nombre: `F-246.pdf`, `F-718.txt`.
   Si el archivo pesa más de unos MB o tiene derechos restringidos, no lo commitees: déjalo solo en la sesión.
2. **Habilitar la red del entorno.** En la configuración del entorno en la nube (menú del entorno en la barra de
   título de la sesión → Editar → Acceso a la red), agrega estos dominios en *Allowed domains* dejando marcada la
   casilla de gestores de paquetes. Instrucciones: https://code.claude.com/docs/en/cloud-environments#network-access

   Dominios que más se repiten entre las fuentes pendientes:
   `doi.org`, `pmc.ncbi.nlm.nih.gov`, `pubmed.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `arxiv.org`,
   `www.sciencedirect.com`, `dl.acm.org`, `onlinelibrary.wiley.com`, `www.science.org`, `www.mdpi.com`,
   `www.frontiersin.org`, `journals.plos.org`, `aclanthology.org`, `proceedings.mlr.press`, `www.oecd.org`.

## Qué pasa después de leer una fuente completa

- Se contrasta la ficha con el texto. Autor, año, revista o DOI se corrigen sin preguntar (y se anota). Cifras,
  hallazgos, rigor o URL solo se corrigen con autorización del usuario.
- Sus relaciones del grafo semántico pasan a `lectura: completa` con un pase (`relaciones/pase_0NN.json`).
- Se regenera la lista con `python research/grafo/lectura_pendiente.py`.
