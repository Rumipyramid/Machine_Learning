# Buenas Mierdas ✦ archivo de ruinas digitales y afectos reapropiados

Altar/archivo 3D interactivo en la web. Arte contemporáneo, diseño especulativo
y resistencia tecnopolítica: contra el colonialismo de datos, este archivo vive
en una computadora portátil.

## Cómo correrlo (para dummies)

Necesitas tener instalado [Node.js](https://nodejs.org) (versión 18 o más nueva).

```bash
# 1. entra a la carpeta del proyecto
cd buenas-mierdas

# 2. instala las dependencias (solo la primera vez, tarda un par de minutos)
npm install

# 3. enciende el servidor de desarrollo
npm run dev
```

Abre en tu navegador la dirección que aparece (normalmente `http://localhost:5173`).
Deberías ver: cielo pastel infinito con niebla, brillitos titilando, un objeto
de prueba rosado, y la ventana retro del manifiesto.

## Estructura de carpetas

```
buenas-mierdas/
├── index.html              ← la página (Vite la usa de punto de entrada)
├── package.json            ← lista de dependencias y comandos
├── vite.config.js          ← configuración de Vite
├── public/
│   ├── gifs/               ← AQUÍ van tus GIFs de GifCities
│   └── fonts/              ← aquí irá la fuente pixelada (.woff2)
└── src/
    ├── main.jsx            ← arranca React
    ├── App.jsx             ← el lienzo 3D + la UI 2D superpuesta
    ├── styles/
    │   └── global.css      ← estética Windows 95 / web vernácula
    ├── scene/              ← todo lo que vive DENTRO del 3D
    │   ├── Cielo.jsx       ← esfera-cielo con degradé pastel (shader)
    │   ├── ConstelacionGifs.jsx  ← reparte billboards por el cielo
    │   ├── GifBillboard.jsx      ← GIF animado como sprite 3D
    │   └── EstrellaPixel.jsx     ← estrellita procedural de relleno
    └── ui/                 ← componentes HTML que flotan sobre el canvas
        └── VentanaRetro.jsx      ← ventana estilo Win95 reutilizable
```

## Fases del proyecto

- [x] **Fase 1** — Cielo infinito: fog, degradé pastel, brillitos, billboards de GIFs, UI retro base
- [ ] Fase 2 — Carga de `.glb` (objetos escaneados) + vista de detalle
- [ ] Fase 3 — Backend Pocketbase local + formulario de subida (drag & drop)
- [ ] Fase 4 — Reapropiación visual (grietas/glitch, consagración a las 100)
- [ ] Fase 5 — Buscador Ctrl+F + vuelo de cámara
- [ ] Fase 6 — Cloudflare Tunnel + moderación de textos

## Stack

Vite · React · React Three Fiber · Drei · gifuct-js · (próximamente) Pocketbase
