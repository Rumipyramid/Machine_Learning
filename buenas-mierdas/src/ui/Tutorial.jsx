import VentanaRetro from './VentanaRetro.jsx'

// Pantalla 3 del flujo: guía rápida de controles + botón Start.
export default function Tutorial({ onEmpezar }) {
  return (
    <VentanaRetro titulo="como_navegar.txt" onCerrar={onEmpezar}>
      <table className="tabla-controles">
        <tbody>
          <tr><td>🖱️ arrastrar</td><td>girar alrededor del altar</td></tr>
          <tr><td>🖱️ clic derecho + arrastrar</td><td>desplazarte de lado</td></tr>
          <tr><td>🖱️ rueda</td><td>acercarte / alejarte</td></tr>
          <tr><td>⌨️ W A S D o flechas</td><td>volar por el cielo</td></tr>
          <tr><td>⌨️ Q / E</td><td>subir / bajar</td></tr>
          <tr><td>⌨️ Ctrl + F</td><td>buscar un afecto</td></tr>
          <tr><td>✨ clic en un objeto</td><td>ver su historia</td></tr>
        </tbody>
      </table>
      <div className="centrado">
        <button className="boton-retro boton-start" onClick={onEmpezar}>
          ▶ Start
        </button>
      </div>
    </VentanaRetro>
  )
}
