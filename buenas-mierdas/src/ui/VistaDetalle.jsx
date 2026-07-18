import VentanaRetro from './VentanaRetro.jsx'

// ---------------------------------------------------------------------------
// VistaDetalle (pantalla 6): la ficha de un afecto.
// Sin likes: solo "reapropiar". Cada reapropiación hace destellar el objeto
// (y en la Fase 4 dejará grieta/mugre acumulada). A las 100, se consagra.
// ---------------------------------------------------------------------------

export default function VistaDetalle({ afecto, reapropiaciones, onReapropiar, onVolar, onCerrar }) {
  const consagrado = reapropiaciones >= 100

  return (
    <VentanaRetro titulo={`${afecto.nombre}.txt`} onCerrar={onCerrar}>
      <p className="detalle-campo"><b>ubicación:</b> {afecto.ubicacion}</p>
      <p className="detalle-campo"><b>historia:</b> {afecto.historia}</p>
      <p className="detalle-campo">
        {afecto.tags.map((tag) => (
          <span key={tag} className="chip-tag">#{tag}</span>
        ))}
      </p>

      <p className="detalle-campo contador-reapropiaciones">
        {consagrado ? (
          <span className="consagrado">★ CONSAGRADO ★ afecto de afectos</span>
        ) : (
          <>reapropiado <b>{reapropiaciones}</b> de 100 veces</>
        )}
      </p>

      <div className="centrado botones-detalle">
        {!consagrado && (
          <button className="boton-retro" onClick={onReapropiar}>
            ✥ Reapropiar
          </button>
        )}
        <button className="boton-retro" onClick={onVolar}>
          ➤ Volar hacia él
        </button>
      </div>
    </VentanaRetro>
  )
}
