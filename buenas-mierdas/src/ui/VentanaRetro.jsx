// VentanaRetro: ventana estilo Windows 95 hecha con HTML/CSS plano.
// Flota SOBRE el canvas 3D (no vive dentro de él).
export default function VentanaRetro({ titulo, onCerrar, children }) {
  return (
    <div className="ventana-fondo">
      <div className="ventana-retro" role="dialog" aria-label={titulo}>
        <div className="ventana-titulo">
          <span>{titulo}</span>
          <button className="ventana-cerrar" onClick={onCerrar} aria-label="cerrar">
            ✕
          </button>
        </div>
        <div className="ventana-cuerpo">{children}</div>
      </div>
    </div>
  )
}
