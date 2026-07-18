// ---------------------------------------------------------------------------
// afectos.js — el catálogo de objetos del altar.
//
// Por ahora es una lista escrita a mano con objetos de ejemplo (formas
// geométricas de mentira). En la Fase 3, esta lista vendrá de Pocketbase
// con los .glb reales que suba la gente.
//
// Para probar un .glb TUYO hoy mismo:
//   1. pon el archivo en  public/modelos/  (ej: public/modelos/taza.glb)
//   2. agrega aquí un objeto con  glb: '/modelos/taza.glb'
//      (la forma/color se ignoran cuando hay glb)
// ---------------------------------------------------------------------------

export const AFECTOS = [
  {
    id: 'a1',
    nombre: 'taza despostillada',
    historia: 'Era de mi abuela. El borde roto marca el lado por donde ella tomaba.',
    ubicacion: 'cocina de una casa que ya no existe',
    tags: ['cerámica', 'familia', 'desayuno'],
    posicion: [0, 0, 0],
    forma: 'icosaedro',
    color: '#ffb7d5',
  },
  {
    id: 'a2',
    nombre: 'walkman amarillo',
    historia: 'Lo encontré en la cachina. Todavía gira, aunque ya no suena.',
    ubicacion: 'mercado de segunda, mesa del fondo',
    tags: ['música', 'plástico', '90s'],
    posicion: [9, 2, -6],
    forma: 'caja',
    color: '#ffe9a8',
  },
  {
    id: 'a3',
    nombre: 'peluche tuerto',
    historia: 'Perdió el ojo en una mudanza. Nadie lo quiso tirar.',
    ubicacion: 'caja de "cosas que duelen"',
    tags: ['infancia', 'suave', 'testigo'],
    posicion: [-11, 4, -3],
    forma: 'esfera',
    color: '#d9c6ff',
  },
  {
    id: 'a4',
    nombre: 'anillo de fantasía',
    historia: 'Me lo regalaron a los 15. El dorado se fue, la promesa no.',
    ubicacion: 'joyero heredado',
    tags: ['promesa', 'metal', 'brillo'],
    posicion: [6, 7, 8],
    forma: 'toro',
    color: '#c9f6ff',
  },
  {
    id: 'a5',
    nombre: 'casete sin etiqueta',
    historia: 'Nadie sabe qué tiene grabado. Preferimos no averiguarlo.',
    ubicacion: 'guantera de un auto vendido',
    tags: ['misterio', 'voz', 'cinta'],
    posicion: [-7, 1, 10],
    forma: 'caja',
    color: '#ffc7e6',
  },
  {
    id: 'a6',
    nombre: 'llave de una puerta demolida',
    historia: 'La casa ya no está. La llave sigue abriendo algo, no sabemos qué.',
    ubicacion: 'llavero de mi papá',
    tags: ['casa', 'pérdida', 'metal'],
    posicion: [14, 5, 4],
    forma: 'nudo',
    color: '#b8e6c9',
  },
  {
    id: 'a7',
    nombre: 'gameboy con pantalla quemada',
    historia: 'Se ve una sombra fantasma de Tetris para siempre.',
    ubicacion: 'cajón de cables viejos',
    tags: ['juego', 'pantalla', 'fantasma'],
    posicion: [-4, 9, -12],
    forma: 'caja',
    color: '#cdefff',
  },
  {
    id: 'a8',
    nombre: 'flor de tela desteñida',
    historia: 'Vino en un ramo de despedida. Es la única que no se marchitó.',
    ubicacion: 'entre las páginas de un diccionario',
    tags: ['despedida', 'tela', 'rosa'],
    posicion: [2, 12, -18],
    forma: 'dodecaedro',
    color: '#ffd6e8',
  },
  // ejemplo con .glb (descomenta cuando pongas tu archivo en public/modelos/):
  // {
  //   id: 'a9',
  //   nombre: 'mi primer escaneo',
  //   historia: 'Escaneado con Polycam en la sala.',
  //   ubicacion: 'mi sala',
  //   tags: ['prueba'],
  //   posicion: [-15, 3, 12],
  //   glb: '/modelos/mi_escaneo.glb',
  //   color: '#ffffff',
  // },
]
