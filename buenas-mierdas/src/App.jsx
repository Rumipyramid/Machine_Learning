import { Canvas } from '@react-three/fiber'
import { OrbitControls, Sparkles } from '@react-three/drei'
import Cielo, { COLORES } from './scene/Cielo.jsx'
import ConstelacionGifs from './scene/ConstelacionGifs.jsx'
import VentanaRetro from './ui/VentanaRetro.jsx'
import { useState } from 'react'

export default function App() {
  const [manifiestoAbierto, setManifiestoAbierto] = useState(true)

  return (
    <div className="app">
      {/* ---------- EL LIENZO 3D (el altar) ---------- */}
      <Canvas
        // dpr limitado a 1.5: en pantallas retina no renderizamos al doble
        // de resolución — se ve igual de bien con estética pixelada y va más fluido
        dpr={[1, 1.5]}
        camera={{ position: [0, 0, 12], fov: 55, near: 0.1, far: 400 }}
        gl={{ antialias: false }}
      >
        {/* Niebla: el color debe coincidir con el horizonte del cielo
            para que los objetos se "disuelvan" en la distancia */}
        <fog attach="fog" args={[COLORES.horizonte, 15, 120]} />

        {/* Luz suave y tierna: ambiental pastel + una direccional cálida */}
        <ambientLight intensity={0.9} color={COLORES.luzAmbiente} />
        <directionalLight position={[5, 10, 5]} intensity={0.7} color={COLORES.luzSol} />

        <Cielo />

        {/* Brillitos volumétricos de drei: miles de partículas en UN solo
            draw call. Baratísimos. */}
        <Sparkles count={220} scale={[70, 40, 70]} size={4} speed={0.35} color="#ffd9f2" opacity={0.8} />
        <Sparkles count={120} scale={[50, 30, 50]} size={2.5} speed={0.2} color="#c9f6ff" opacity={0.6} />

        {/* Constelación de GIFs retro flotando como billboards */}
        <ConstelacionGifs />

        {/* Objeto de prueba: aquí después vivirán los .glb subidos */}
        <mesh position={[0, 0, 0]}>
          <icosahedronGeometry args={[1.2, 0]} />
          <meshStandardMaterial color="#ffb7d5" flatShading />
        </mesh>

        <OrbitControls
          enableDamping
          dampingFactor={0.06}
          minDistance={3}
          maxDistance={90}
        />
      </Canvas>

      {/* ---------- LA UI 2D (HTML plano flotando encima) ---------- */}
      <div className="ui-overlay">
        <header className="barra-superior">
          <span className="titulo-sitio">✦ buenas mierdas ✦</span>
          <button className="boton-retro" onClick={() => setManifiestoAbierto(true)}>
            manifiesto.txt
          </button>
        </header>

        <button className="boton-retro boton-subir">⬆ Subir un afecto</button>

        {manifiestoAbierto && (
          <VentanaRetro titulo="manifiesto.txt" onCerrar={() => setManifiestoAbierto(false)}>
            <p>
              Archivo de ruinas digitales y afectos reapropiados.
              <br />
              <br />
              Contra el colonialismo de datos, este altar vive en una
              computadora portátil. Aquí las cosas rotas, viejas y amadas
              existen en un plano más allá del físico.
            </p>
            <p className="parpadeo">▸ haz clic y arrastra para explorar el cielo</p>
          </VentanaRetro>
        )}
      </div>
    </div>
  )
}
