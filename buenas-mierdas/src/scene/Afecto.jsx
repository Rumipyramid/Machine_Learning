import * as THREE from 'three'
import { Suspense, useRef, useState } from 'react'
import { useFrame } from '@react-three/fiber'
import { useGLTF, Sparkles } from '@react-three/drei'

// ---------------------------------------------------------------------------
// Afecto: un objeto del altar.
//
// - Si tiene `glb`, carga el modelo escaneado… pero SOLO cuando la cámara
//   está cerca (carga perezosa por distancia). De lejos muestra un brillito
//   de relleno. Así el altar aguanta decenas de objetos sin morir.
// - Si no tiene `glb`, muestra una forma geométrica de ejemplo.
// - Al pasar el mouse brilla suavecito (y el cursor cambia a manito).
// - `pulso` es un timestamp: cuando cambia, el objeto destella (glitch de
//   reapropiación) y el destello decae solo. Base del efecto de la Fase 4.
// ---------------------------------------------------------------------------

const DISTANCIA_DE_CARGA = 45 // a menos de esto (en unidades 3D) se carga el .glb

function Forma({ forma }) {
  switch (forma) {
    case 'caja': return <boxGeometry args={[1.4, 1.4, 1.4]} />
    case 'esfera': return <sphereGeometry args={[1, 12, 10]} />
    case 'toro': return <torusGeometry args={[0.9, 0.35, 10, 24]} />
    case 'nudo': return <torusKnotGeometry args={[0.7, 0.26, 48, 8]} />
    case 'dodecaedro': return <dodecahedronGeometry args={[1.1, 0]} />
    default: return <icosahedronGeometry args={[1.2, 0]} />
  }
}

function ModeloGLB({ url }) {
  const { scene } = useGLTF(url)
  return <primitive object={scene} />
}

export default function Afecto({ afecto, reapropiaciones = 0, pulso = 0, onClick }) {
  const grupo = useRef()
  const material = useRef()
  const [hover, setHover] = useState(false)
  const [cerca, setCerca] = useState(false)
  const cuadro = useRef(0)

  const consagrado = reapropiaciones >= 100

  useFrame(({ camera }) => {
    // chequeo de distancia solo 1 de cada 20 cuadros (no hace falta más)
    cuadro.current += 1
    if (afecto.glb && cuadro.current % 20 === 0 && grupo.current) {
      const d = camera.position.distanceTo(grupo.current.position)
      setCerca(d < DISTANCIA_DE_CARGA)
    }
    // brillo: reposo bajito, hover más, destello de reapropiación decae en ~0.5s
    if (material.current) {
      const destello = pulso ? Math.max(0, 1.6 - (performance.now() - pulso) / 300) : 0
      const base = consagrado ? 0.45 : hover ? 0.35 : 0.08
      material.current.emissiveIntensity = THREE.MathUtils.lerp(
        material.current.emissiveIntensity, base + destello, 0.18,
      )
    }
  })

  return (
    <group
      ref={grupo}
      position={afecto.posicion}
      onClick={(e) => { e.stopPropagation(); onClick(afecto) }}
      onPointerOver={(e) => { e.stopPropagation(); setHover(true); document.body.style.cursor = 'pointer' }}
      onPointerOut={() => { setHover(false); document.body.style.cursor = 'default' }}
    >
      {afecto.glb && cerca ? (
        // el .glb real, solo cuando estás cerca (Suspense muestra nada mientras baja)
        <Suspense fallback={null}>
          <ModeloGLB url={afecto.glb} />
        </Suspense>
      ) : (
        <mesh>
          <Forma forma={afecto.forma} />
          <meshStandardMaterial
            ref={material}
            color={afecto.color}
            emissive={afecto.color}
            emissiveIntensity={0.08}
            flatShading
          />
        </mesh>
      )}

      {/* los consagrados llevan su propia constelación orbitando */}
      {consagrado && <Sparkles count={24} scale={3.4} size={5} speed={0.6} color="#fff6b8" />}
    </group>
  )
}
