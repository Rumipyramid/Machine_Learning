import { Canvas } from '@react-three/fiber'
import { Sparkles } from '@react-three/drei'
import { useEffect, useState } from 'react'
import Cielo, { COLORES } from './scene/Cielo.jsx'
import ConstelacionGifs from './scene/ConstelacionGifs.jsx'
import Afecto from './scene/Afecto.jsx'
import ControlesCamara from './scene/ControlesCamara.jsx'
import VentanaRetro from './ui/VentanaRetro.jsx'
import Tutorial from './ui/Tutorial.jsx'
import Buscador from './ui/Buscador.jsx'
import VistaDetalle from './ui/VistaDetalle.jsx'
import { AFECTOS } from './data/afectos.js'

export default function App() {
  // flujo de entrada: manifiesto → tutorial → altar libre (null)
  const [pantalla, setPantalla] = useState('manifiesto')
  const [buscadorAbierto, setBuscadorAbierto] = useState(false)
  const [seleccionado, setSeleccionado] = useState(null) // afecto en vista de detalle
  const [destino, setDestino] = useState(null) // afecto hacia el que vuela la cámara
  const [reapropiaciones, setReapropiaciones] = useState({}) // { id: cuenta } (en Fase 3 vivirá en Pocketbase)
  const [pulsos, setPulsos] = useState({}) // { id: timestamp } del último destello

  // atajo Ctrl+F → abrir buscador · Escape → cerrar ventanas
  useEffect(() => {
    const onTecla = (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'f') {
        e.preventDefault() // que no se abra el buscador del navegador
        setBuscadorAbierto(true)
      }
      if (e.key === 'Escape') {
        setBuscadorAbierto(false)
        setSeleccionado(null)
      }
    }
    window.addEventListener('keydown', onTecla)
    return () => window.removeEventListener('keydown', onTecla)
  }, [])

  const volarHacia = (afecto) => {
    setBuscadorAbierto(false)
    setSeleccionado(null)
    setDestino(afecto)
  }

  const reapropiar = (afecto) => {
    setReapropiaciones((r) => ({ ...r, [afecto.id]: (r[afecto.id] || 0) + 1 }))
    setPulsos((p) => ({ ...p, [afecto.id]: performance.now() }))
  }

  return (
    <div className="app">
      {/* ---------- EL LIENZO 3D (el altar) ---------- */}
      <Canvas
        dpr={[1, 1.5]}
        camera={{ position: [0, 3, 14], fov: 55, near: 0.1, far: 400 }}
        gl={{ antialias: false }}
      >
        <fog attach="fog" args={[COLORES.horizonte, 15, 120]} />
        <ambientLight intensity={0.9} color={COLORES.luzAmbiente} />
        <directionalLight position={[5, 10, 5]} intensity={0.7} color={COLORES.luzSol} />

        <Cielo />
        <Sparkles count={220} scale={[70, 40, 70]} size={4} speed={0.35} color="#ffd9f2" opacity={0.8} />
        <Sparkles count={120} scale={[50, 30, 50]} size={2.5} speed={0.2} color="#c9f6ff" opacity={0.6} />
        <ConstelacionGifs />

        {/* los afectos del altar */}
        {AFECTOS.map((a) => (
          <Afecto
            key={a.id}
            afecto={a}
            reapropiaciones={reapropiaciones[a.id] || 0}
            pulso={pulsos[a.id] || 0}
            onClick={setSeleccionado}
          />
        ))}

        <ControlesCamara destino={destino} onFinDeVuelo={() => setDestino(null)} />
      </Canvas>

      {/* ---------- LA UI 2D (HTML plano flotando encima) ---------- */}
      <div className="ui-overlay">
        <header className="barra-superior">
          <span className="titulo-sitio">✦ buenas mierdas ✦</span>
          <span>
            <button className="boton-retro" onClick={() => setBuscadorAbierto(true)}>
              🔍 buscar
            </button>{' '}
            <button className="boton-retro" onClick={() => setPantalla('manifiesto')}>
              manifiesto.txt
            </button>
          </span>
        </header>

        <button className="boton-retro boton-subir">⬆ Subir un afecto</button>

        {pantalla === 'manifiesto' && (
          <VentanaRetro titulo="manifiesto.txt" onCerrar={() => setPantalla('tutorial')}>
            <p>
              Archivo de ruinas digitales y afectos reapropiados.
              <br />
              <br />
              Contra el colonialismo de datos, este altar vive en una
              computadora portátil. Aquí las cosas rotas, viejas y amadas
              existen en un plano más allá del físico.
            </p>
            <p className="parpadeo">▸ cierra esta ventana para continuar</p>
          </VentanaRetro>
        )}

        {pantalla === 'tutorial' && <Tutorial onEmpezar={() => setPantalla(null)} />}

        {buscadorAbierto && (
          <Buscador afectos={AFECTOS} onVolar={volarHacia} onCerrar={() => setBuscadorAbierto(false)} />
        )}

        {seleccionado && (
          <VistaDetalle
            afecto={seleccionado}
            reapropiaciones={reapropiaciones[seleccionado.id] || 0}
            onReapropiar={() => reapropiar(seleccionado)}
            onVolar={() => volarHacia(seleccionado)}
            onCerrar={() => setSeleccionado(null)}
          />
        )}
      </div>
    </div>
  )
}
