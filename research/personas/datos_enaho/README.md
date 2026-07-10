# Datos ENAHO (microdato crudo) — carpeta de trabajo local

> Esta carpeta es para **colocar los CSV de ENAHO descargados del INEI**. Los `.csv`
> y `.zip` aquí están en `.gitignore` (no se versionan: son grandes y regenerables).
> El microdato es público y gratuito; no requiere convenio.

## 1. Dónde descargar
- **Portal INEI Microdatos:** https://proyectos.inei.gob.pe/microdatos/
  → *Consulta por Encuestas* → **ENAHO – Condiciones de Vida y Pobreza** → elige el **año**
  → descarga los **módulos** que necesitas (botón CSV). Cada módulo baja como un **ZIP**
  que contiene `ENAHO01-<año>-<módulo>.csv` (p. ej. `ENAHO01-2024-300.csv`).
- **Alternativa programática (recomendada):**
  ```bash
  pip install enahodata           # o: pip install inei-microdatos
  ```
  y descarga por año/módulo sin navegar el portal.

## 2. Qué módulos bajar (para sembrar el generador)
| Archivo CSV | Módulo | Aporta a lapuerta |
|---|---|---|
| `ENAHO01-AAAA-100.csv` | 100 Vivienda | `tenencia_vivienda` (p105a) |
| `ENAHO01-AAAA-200.csv` | 200 Miembros del hogar | dependientes / composición |
| `ENAHO01-AAAA-300.csv` | 300 Educación | nivel educativo (p301a) |
| `ENAHO01-AAAA-500.csv` | 500 Empleo e ingresos | `situacion_laboral` (ocu500/p507/p511a) |
| `Sumaria-AAAA.csv` | Sumaria | `nse_proxy` (gasto per cápita: gashog2d/mieperho) |

Baja también el **Diccionario** del año (PDF) para confirmar nombres de columnas.

## 3. Cómo enchufarlo al modelo (3 comandos)
Desde la raíz del repo, con los CSV ya en esta carpeta:

```bash
# (a) ENAHO -> tabla conjunta ponderada (semilla con correlaciones reales)
python research/personas/generador/enaho_loader.py \
  --modulo300 research/personas/datos_enaho/ENAHO01-2024-300.csv \
  --modulo100 research/personas/datos_enaho/ENAHO01-2024-100.csv \
  --sumaria   research/personas/datos_enaho/Sumaria-2024.csv \
  --dim region --dim nse_proxy --dim educacion --dim tenencia_vivienda \
  --out-joint research/personas/datos_enaho/joint.csv

# (b) Ajustar la semilla a las marginales objetivo (raking/IPF)
python research/personas/generador/ipf.py \
  --joint research/personas/datos_enaho/joint.csv \
  --targets research/personas/datos_enaho/targets.json \
  --out-fitted research/personas/datos_enaho/fitted.csv

# (c) Generar usuarios sembrados desde el dato real
python research/personas/generador/generate_synthetic_users.py \
  --n 2000 --joint research/personas/datos_enaho/fitted.csv \
  --out research/personas/datos_enaho/usuarios.csv

# (d) Comprobar objetivamente si calibrar mejoró
python research/personas/generador/validate.py \
  --joint research/personas/datos_enaho/fitted.csv
```

`targets.json` = las marginales objetivo (las que quieres imponer), formato:
```json
{"nse": {"A":0.02,"B":0.11,"C":0.27,"D":0.26,"E":0.34},
 "region": {"Lima_Metropolitana":0.33,"Resto_Costa":0.25,"Sierra":0.30,"Selva":0.12}}
```

## 4. Nota importante: factor de expansión
ENAHO trae **pesos muestrales** (`factor07`, o `fac500a` en el módulo 500). El loader
los aplica por defecto; sin ellos las cifras salen sesgadas. Si tu año usa otro nombre
de columna, pásalo con `--factor <columna>`.

## 5. Si los nombres de columna no coinciden
Si `enaho_loader.py` reporta "tabla vacía", revisa el Diccionario del año: los códigos
(`dominio`, `estrato`, `p301a`, `p105a`, `gashog2d`, `mieperho`, llaves
`conglome/vivienda/hogar/codperso`) pueden cambiar entre años. Ajusta los recodificadores
en `enaho_loader.py` (sección RECODERS) según corresponda.
