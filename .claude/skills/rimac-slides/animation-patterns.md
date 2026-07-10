# Patrones de animación — Motion Rimac

Referencia para animar decks Rimac. **No hay "elige un feeling": hay UN registro de motion**, anclado en el token de `design.md` (§motion). La libertad creativa vive en **qué** animás y en **cómo lo coreografiás por slide**, no en cambiar la curva o el ritmo de la marca.

## Registro de motion Rimac (bloqueado)

| Token | Valor | Uso |
|---|---|---|
| **reveal** | `riseIn` — `opacity 0→1` + `translateY(28px→0)`, `0.75s`, `cubic-bezier(.22,1,.36,1)` | Entrada por defecto de todo elemento nuevo. Cada elemento lleva `.reveal`. |
| **stagger** | `0.05s → 0.55s` | Reparto escalonado de los hijos de un slide. Ordenalo para **revelar el argumento** (build-up por pasos), no como adorno mecánico. |
| **reduced-motion** | requerido | `@media (prefers-reduced-motion: reduce)` ya en `viewport-base.css`. No anular. |
| **énfasis** | gradiente `hero` o rojo sólido sobre **1 frase clave** por slide (opcional) | Animable como acento, nunca sobre el título completo ni el cuerpo. |

> El ritmo y la curva están fijos para que toda animación "se sienta de la misma familia". Lo **libre** es cómo el movimiento **revela el argumento**: qué entra, en qué orden, con qué build-up por pasos (Principio de variedad: calidad, no formato — design.md §El corazón del slide). **Animá para explicar, no para adornar**; que dos slides animen parecido está bien si cada uno explica bien su idea.

## Animaciones de entrada (on-brand)

```css
/* Fade + Slide Up — entrada por defecto Rimac (riseIn) */
.reveal {
    opacity: 0;
    transform: translateY(28px);
    transition: opacity 0.75s var(--ease-rimac),
                transform 0.75s var(--ease-rimac);
}
.slide.visible .reveal { opacity: 1; transform: translateY(0); }

/* Scale In — para un dato/KPI dominante o un visual protagonista */
.reveal-scale {
    opacity: 0;
    transform: scale(0.94);
    transition: opacity 0.75s var(--ease-rimac), transform 0.75s var(--ease-rimac);
}

/* Slide from Left — para listas o ejes horizontales */
.reveal-left {
    opacity: 0;
    transform: translateX(-40px);
    transition: opacity 0.75s var(--ease-rimac), transform 0.75s var(--ease-rimac);
}

/* Blur In — para una cita gigante o un cierre */
.reveal-blur {
    opacity: 0;
    filter: blur(10px);
    transition: opacity 0.9s var(--ease-rimac), filter 0.9s var(--ease-rimac);
}
```

`--ease-rimac` = `cubic-bezier(.22, 1, .36, 1)` (definido en el `:root`, ver html-template.md).

## Fondos y profundidad (tonal, no 3D)

La profundidad Rimac es **tonal**: blanco sobre lavanda sobre viewport. **Sin sombras** salvo la del stage. Usá los tokens, no rgba neón.

```css
/* Respiro lavanda — section dividers / fondos suaves */
.bg-section { background: var(--bg-section); }   /* #ECEEFC */

/* Gradiente suave Rimac — atmósfera cálida (úsalo con moderación) */
.bg-grad-soft { background: var(--grad-soft); }  /* #FFEFE3 → #FCE4EC */

/* Par cálido / frío para comparativas */
.bg-warm { background: var(--bg-warm-soft); }    /* #FFF6EF */
.bg-cool { background: var(--bg-cool-soft); }    /* #F7F8FE */

/* Gesto con el wave — atenuado, en una esquina, si aporta (design.md, capa libre).
   El wave NO es exclusivo de la portada; usalo solo si aporta a explicar la idea (capa libre), no por defecto ni para dar variedad. */
.wave-accent { position: absolute; inset: auto -10% -10% auto; opacity: 0.5; pointer-events: none; }
```

> El gradiente `hero` (naranja→rojo→magenta) es **acento puntual** sobre una frase o un dato, animable con `background-clip:text`. No es fill de bloques grandes ni fondo de slide.

## Recursos de profundidad — permitidos con disciplina

Rimac es "casi plano" **por defecto**. Algunos recursos de profundidad/efecto están **permitidos como excepción controlada**: el **límite es firme** (evita el slop), pero el **cuándo lo decide el skill por la intención de la idea, y propone** — no es un checklist.

| Recurso | Cuándo (intención, contextual) | Límite firme |
|---|---|---|
| **3D tilt** (hover) | dar dinamismo a cards · **≤ 3 cards** | perspectiva sutil; se activa al hover (vista interactiva), estático en proyección |
| **Hover-lift** (hover) | dar dinamismo a cards · **> 3 cards** | sombra chica, eleva poco, **siempre z-detrás** (nunca encima de otros elementos) |
| **Sombra ambiente** | separar una superficie cuando el tono no alcanza | **una sola**, muy difusa y sutil; nunca color / capas / long-shadow / neumorfismo |
| **Glassmorphism** | cierre/quiebre con foto-color | **solo slides oscuros** + fondo diseñado para que se note la translucidez |
| **Partículas** | **según el mensaje** | claro u oscuro; subordinadas al texto, densidad/opacidad baja |
| **Fondo-viñeta oscuro** | tratamiento estándar de slides oscuros | `radial-gradient(circle at 50% 40%, #15243a, #0B1620)` |
| **Scan lines** | idea = **sistemas / monitoreo / señal** (recurso muy peculiar) | semántico, contenedor acotado; nunca decorativo por defecto |

> **El skill propone, no impone.** Estos recursos —y cualquier técnica nueva (barrido de gradiente, subrayado que se dibuja, draw-on SVG, count-up, wipe, grano, parallax…)— son un **toolkit abierto, no un catálogo cerrado**: el skill los **propone** según la idea o los hace **a pedido**. La libertad es de técnica; el límite es de marca (paleta, tipografía, easing).

## Sigue FUERA de marca (no usar)

- ❌ **Glow neón / `box-shadow` de color** — sobre blanco (el 95% de los slides) pierde la gracia; paleta y atmósfera fuera de Rimac.

La profundidad **por defecto** se logra con **escala tipográfica, espacio negativo, tono de fondo y composición** — los recursos de arriba son la excepción, no el default.

## Troubleshooting

| Problema | Fix |
|---|---|
| Fuentes no cargan (caen a Helvetica) | `@font-face` local — **BRSonoma NO está en Google**. Verificá rutas `./assets/fonts/` o el base64. |
| Animaciones no disparan | Verificá que se agrega la clase `.visible` al slide activo en `showSlide()`. |
| Gradiente no aparece en PDF | `background-clip:text` no renderiza en export Chromium → caé a fill sólido `tertiary` (#F7052D) para PDF. |
| Issues en móvil | El stage escala como un todo (no reflow); verificá letterbox, no breakpoints. Probá swipe. |
| Performance | Animá solo `transform`/`opacity`; `will-change` con moderación. |
