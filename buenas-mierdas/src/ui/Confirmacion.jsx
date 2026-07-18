import VentanaRetro from './VentanaRetro.jsx'

// Pantalla 9: el afecto ya existe. La cámara volará hacia él.
export default function Confirmacion({ afecto, onIr }) {
  return (
    <VentanaRetro titulo="✧" onCerrar={onIr}>
      <p className="mensaje-confirmacion">
        Tu afecto ahora existe en este plano.
        <br />
        <b>{afecto.nombre}</b>
        <br />
        flota en [{afecto.posicion.map((n) => Math.round(n)).join(', ')}]
      </p>
      <div className="centrado">
        <button className="boton-retro boton-start" onClick={onIr}>
          Ve con él →
        </button>
      </div>
    </VentanaRetro>
  )
}
