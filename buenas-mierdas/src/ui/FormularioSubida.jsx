import { useRef, useState } from 'react'
import VentanaRetro from './VentanaRetro.jsx'
import { subirAfecto } from '../lib/api.js'

// ---------------------------------------------------------------------------
// FormularioSubida (pantalla 8): drag & drop del .glb + los campos del afecto.
// Sin GPS, sin datos personales: la ubicación es texto libre y poético.
// ---------------------------------------------------------------------------

export default function FormularioSubida({ onCreado, onCerrar, onInstrucciones }) {
  const inputArchivo = useRef()
  const [archivo, setArchivo] = useState(null)
  const [arrastrando, setArrastrando] = useState(false)
  const [nombre, setNombre] = useState('')
  const [ubicacion, setUbicacion] = useState('')
  const [historia, setHistoria] = useState('')
  const [tags, setTags] = useState('')
  const [error, setError] = useState('')
  const [subiendo, setSubiendo] = useState(false)

  const recibirArchivo = (f) => {
    if (!f) return
    const nombreArchivo = f.name.toLowerCase()
    if (!nombreArchivo.endsWith('.glb') && !nombreArchivo.endsWith('.gltf')) {
      setError('Ese archivo no es un modelo 3D — necesito un .glb (exportado de Polycam o similar).')
      return
    }
    setError('')
    setArchivo(f)
  }

  const enviar = async (e) => {
    e.preventDefault()
    if (!nombre.trim()) {
      setError('Tu afecto necesita al menos un nombre.')
      return
    }
    setError('')
    setSubiendo(true)
    try {
      const nuevo = await subirAfecto({
        nombre: nombre.trim(),
        ubicacion: ubicacion.trim(),
        historia: historia.trim(),
        tags: tags
          .split(',')
          .map((t) => t.trim().replace(/^#/, '').toLowerCase())
          .filter(Boolean),
        archivo,
      })
      onCreado(nuevo)
    } catch (err) {
      console.error(err)
      setError('No se pudo subir. ¿El altar (Pocketbase) está encendido? Intenta de nuevo.')
      setSubiendo(false)
    }
  }

  return (
    <VentanaRetro titulo="subir_un_afecto" onCerrar={onCerrar}>
      <form onSubmit={enviar}>
        <div
          className={
            'zona-drop' + (arrastrando ? ' arrastrando' : '') + (archivo ? ' con-archivo' : '')
          }
          onClick={() => inputArchivo.current.click()}
          onDragOver={(e) => { e.preventDefault(); setArrastrando(true) }}
          onDragLeave={() => setArrastrando(false)}
          onDrop={(e) => {
            e.preventDefault()
            setArrastrando(false)
            recibirArchivo(e.dataTransfer.files[0])
          }}
        >
          {archivo ? (
            <>📦 {archivo.name} ({Math.round(archivo.size / 1024)} KB) — clic para cambiar</>
          ) : (
            <>⬇ arrastra aquí tu escaneo .glb<br />(o haz clic para buscarlo)</>
          )}
          <input
            ref={inputArchivo}
            type="file"
            accept=".glb,.gltf"
            hidden
            onChange={(e) => recibirArchivo(e.target.files[0])}
          />
        </div>

        <p className="nota-form">
          ¿todavía no escaneas tu objeto?{' '}
          <button type="button" className="enlace-retro" onClick={onInstrucciones}>
            aprende a escanearlo aquí
          </button>{' '}
          — también puedes subir solo la historia y el objeto flotará como forma pastel.
        </p>

        <div className="campo-form">
          <label>nombre de tu afecto *</label>
          <input
            className="input-retro"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            placeholder="taza despostillada de la abuela"
          />
        </div>

        <div className="campo-form">
          <label>ubicación (texto libre — sin GPS, tu anonimato importa)</label>
          <input
            className="input-retro"
            value={ubicacion}
            onChange={(e) => setUbicacion(e.target.value)}
            placeholder="cocina de una casa que ya no existe"
          />
        </div>

        <div className="campo-form">
          <label>historia (el porqué)</label>
          <textarea
            className="input-retro"
            value={historia}
            onChange={(e) => setHistoria(e.target.value)}
            placeholder="por qué este objeto merece existir en otro plano…"
          />
        </div>

        <div className="campo-form">
          <label>etiquetas (separadas por comas)</label>
          <input
            className="input-retro"
            value={tags}
            onChange={(e) => setTags(e.target.value)}
            placeholder="cerámica, familia, desayuno"
          />
        </div>

        {error && <p className="error-form">{error}</p>}

        <div className="centrado">
          <button className="boton-retro boton-start" type="submit" disabled={subiendo}>
            {subiendo ? 'subiendo…' : '✧ Situar en el altar'}
          </button>
        </div>
      </form>
    </VentanaRetro>
  )
}
