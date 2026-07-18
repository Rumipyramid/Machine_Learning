import VentanaRetro from './VentanaRetro.jsx'

// Pantalla 7: cómo escanear tu objeto con el celular (DIY, gratis).
export default function InstruccionesEscaneo({ onVolver }) {
  return (
    <VentanaRetro titulo="como_escanear.txt" onCerrar={onVolver}>
      <p>
        <b>1.</b> Descarga <b>Polycam</b> en tu celular (también sirven Luma AI
        o Kiri Engine — todas tienen modo gratis).
      </p>
      <p>
        <b>2.</b> Pon tu objeto sobre una mesa con buena luz y dale la vuelta
        despacio con la cámara, como si lo acariciaras con la mirada. Entre 20
        y 50 fotos alcanzan.
      </p>
      <p>
        <b>3.</b> Exporta como <b>GLB</b>. Si te deja elegir calidad, elige la
        MÁS BAJA: lo tosco y lo roto son parte de la estética de este altar, y
        además carga rápido.
      </p>
      <p>
        <b>4.</b> Pásate el archivo a la computadora (correo, WhatsApp,
        cable…) y arrástralo al formulario.
      </p>
      <p className="parpadeo">▸ las ruinas no necesitan verse perfectas</p>
      <div className="centrado">
        <button className="boton-retro" onClick={onVolver}>
          ← volver al formulario
        </button>
      </div>
    </VentanaRetro>
  )
}
