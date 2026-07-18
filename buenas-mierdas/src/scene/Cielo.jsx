import * as THREE from 'three'
import { useMemo } from 'react'
import { useFrame } from '@react-three/fiber'

// Paleta única del proyecto: cambiar aquí cambia todo el ambiente.
export const COLORES = {
  cenit: '#b8a9f0',      // lila suave arriba
  horizonte: '#ffd6e8',  // rosa pastel en el horizonte (¡mismo color que el fog!)
  nadir: '#cdefff',      // celeste debajo
  vapor1: '#ffe9f6',     // vapor rosado claro
  vapor2: '#dcd0ff',     // vapor lila
  luzAmbiente: '#ffeef8',
  luzSol: '#fff3c9',
}

// Cielo infinito y GASEOSO: esfera gigante vista desde adentro.
// Al degradé pastel se le suman, en el mismo shader (gratis en GPU):
//  - dos capas de vapor fbm que se mueven lento (nubes de gas)
//  - grano de ruido fino (textura, nada de degradés "limpios" de computadora)
//  - glitter: puntitos que titilan como escarcha
const vertexShader = /* glsl */ `
  varying vec3 vDir;
  void main() {
    vDir = normalize(position);
    vec4 pos = projectionMatrix * mat4(mat3(modelViewMatrix)) * vec4(position, 1.0);
    gl_Position = pos.xyww; // truco: siempre al fondo del depth buffer
  }
`

const fragmentShader = /* glsl */ `
  uniform vec3 uCenit;
  uniform vec3 uHorizonte;
  uniform vec3 uNadir;
  uniform vec3 uVapor1;
  uniform vec3 uVapor2;
  uniform float uTiempo;
  varying vec3 vDir;

  float hash(vec3 p) {
    return fract(sin(dot(p, vec3(127.1, 311.7, 74.7))) * 43758.5453);
  }
  float ruido(vec3 p) {
    vec3 i = floor(p);
    vec3 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    return mix(
      mix(mix(hash(i), hash(i + vec3(1,0,0)), f.x),
          mix(hash(i + vec3(0,1,0)), hash(i + vec3(1,1,0)), f.x), f.y),
      mix(mix(hash(i + vec3(0,0,1)), hash(i + vec3(1,0,1)), f.x),
          mix(hash(i + vec3(0,1,1)), hash(i + vec3(1,1,1)), f.x), f.y),
      f.z
    );
  }
  float fbm(vec3 p) {
    float v = 0.0;
    float a = 0.5;
    for (int i = 0; i < 4; i++) {
      v += a * ruido(p);
      p *= 2.03;
      a *= 0.5;
    }
    return v;
  }

  void main() {
    float h = vDir.y; // -1 abajo, 0 horizonte, 1 arriba

    // 1) degradé base
    vec3 color = h >= 0.0
      ? mix(uHorizonte, uCenit, smoothstep(0.0, 0.7, h))
      : mix(uHorizonte, uNadir, smoothstep(0.0, 0.6, -h));

    // 2) vapores: dos capas de gas fbm derivando a distinta velocidad
    float gas1 = fbm(vDir * 2.6 + vec3(uTiempo * 0.018, uTiempo * 0.011, 0.0));
    float gas2 = fbm(vDir * 5.5 + vec3(0.0, -uTiempo * 0.014, uTiempo * 0.02) + 31.7);
    color = mix(color, uVapor1, smoothstep(0.42, 0.78, gas1) * 0.45);
    color = mix(color, uVapor2, smoothstep(0.48, 0.82, gas2) * 0.30);

    // 3) grano fino: rompe el degradé "perfecto", textura de ruido
    color += (hash(vDir * 380.0) - 0.5) * 0.045;

    // 4) glitter: escarcha rala que titila con el tiempo
    vec3 celda = floor(vDir * 240.0);
    float esChispa = step(0.9982, hash(celda));
    float titilar = 0.5 + 0.5 * sin(uTiempo * 2.5 + hash(celda + 5.0) * 6.2831);
    color += esChispa * titilar * 0.30;

    gl_FragColor = vec4(color, 1.0);
  }
`

export default function Cielo() {
  const uniforms = useMemo(
    () => ({
      uCenit: { value: new THREE.Color(COLORES.cenit) },
      uHorizonte: { value: new THREE.Color(COLORES.horizonte) },
      uNadir: { value: new THREE.Color(COLORES.nadir) },
      uVapor1: { value: new THREE.Color(COLORES.vapor1) },
      uVapor2: { value: new THREE.Color(COLORES.vapor2) },
      uTiempo: { value: 0 },
    }),
    [],
  )

  useFrame(({ clock }) => {
    uniforms.uTiempo.value = clock.elapsedTime
  })

  return (
    <mesh>
      <sphereGeometry args={[300, 32, 16]} />
      <shaderMaterial
        uniforms={uniforms}
        vertexShader={vertexShader}
        fragmentShader={fragmentShader}
        side={THREE.BackSide}
        depthWrite={false}
        fog={false}
      />
    </mesh>
  )
}
