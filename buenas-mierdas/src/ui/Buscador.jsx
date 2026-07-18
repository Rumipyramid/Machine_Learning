import { useState } from 'react'
import VentanaRetro from './VentanaRetro.jsx'

// ---------------------------------------------------------------------------
// Buscador (pantalla 5): se abre con Ctrl+F o con el botón 🔍.
// Índice visual de afectos: muestrita de color, nombre, coordenadas X,Y,Z
// y tags. Puedes filtrar escribiendo. Al hacer clic en uno, la cámara
// vuela automáticamente hacia él.
// ---------------------------------------------------------------------------

export default function Buscador({ afectos, onVolar, onCerrar }) {
  const [filtro, setFiltro] = useState('')

  const texto = filtro.trim().toLowerCase()
  const resultados = afectos.filter(
    (a) =>
      !texto ||
      a.nombre.toLowerCase().includes(texto) ||
      a.tags.some((tag) => tag.toLowerCase().includes(texto)),
  )

  return (
    <VentanaRetro titulo="buscar_afecto.exe" onCerrar={onCerrar}>
      <input
        className="input-retro"
        type="text"
        placeholder="escribe un nombre o etiqueta…"
        value={filtro}
        onChange={(e) => setFiltro(e.target.value)}
        autoFocus
      />

      <div className="lista-afectos">
        {resultados.length === 0 && (
          <p className="sin-resultados">no se encontró ese afecto…</p>
        )}
        {resultados.map((a) => (
          <button key={a.id} className="item-afecto" onClick={() => onVolar(a)}>
            <span className="muestra-color" style={{ background: a.color }} />
            <span className="item-nombre">{a.nombre}</span>
            <span className="item-coords">
              [{a.posicion.map((n) => Math.round(n)).join(', ')}]
            </span>
            <span className="item-tags">
              {a.tags.map((tag) => (
                <span key={tag} className="chip-tag">#{tag}</span>
              ))}
            </span>
          </button>
        ))}
      </div>
    </VentanaRetro>
  )
}
