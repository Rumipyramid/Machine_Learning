import * as THREE from 'three'
import { useMemo } from 'react'

// Paleta única del proyecto: cambiar aquí cambia todo el ambiente.
export const COLORES = {
  cenit: '#b8a9f0',      // lila suave arriba
  horizonte: '#ffd6e8',  // rosa pastel en el horizonte (¡mismo color que el fog!)
  nadir: '#cdefff',      // celeste debajo
  luzAmbiente: '#ffeef8',
  luzSol: '#fff3c9',
}

// Cielo infinito: una esfera gigante vista desde adentro, con un degradé
// vertical calculado en shader (2 triángulos de costo — gratis en GPU).
const vertexShader = /* glsl */ `
  varying vec3 vDir;
  void main() {
    vDir = normalize(position);
    // quitamos la traslación de la cámara para que el cielo nunca "se acerque"
    vec4 pos = projectionMatrix * mat4(mat3(modelViewMatrix)) * vec4(position, 1.0);
    gl_Position = pos.xyww; // truco: siempre al fondo del depth buffer
  }
`

const fragmentShader = /* glsl */ `
  uniform vec3 uCenit;
  uniform vec3 uHorizonte;
  uniform vec3 uNadir;
  varying vec3 vDir;
  void main() {
    float h = vDir.y; // -1 abajo, 0 horizonte, 1 arriba
    vec3 color = h >= 0.0
      ? mix(uHorizonte, uCenit, smoothstep(0.0, 0.7, h))
      : mix(uHorizonte, uNadir, smoothstep(0.0, 0.6, -h));
    gl_FragColor = vec4(color, 1.0);
  }
`

export default function Cielo() {
  const uniforms = useMemo(
    () => ({
      uCenit: { value: new THREE.Color(COLORES.cenit) },
      uHorizonte: { value: new THREE.Color(COLORES.horizonte) },
      uNadir: { value: new THREE.Color(COLORES.nadir) },
    }),
    [],
  )

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
