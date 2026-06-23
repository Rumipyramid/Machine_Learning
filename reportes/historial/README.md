# 🕝 Repositorio de historial de cambios (últimos 15 días)

Registro legible de los cambios aplicados al tablero/matriz del Beholder en los **últimos 15 días**.
Es la "memoria reciente" del equipo; el historial **completo** siempre queda en el `git log`.

## Archivos
- **`CAMBIOS.md`** — vista legible (generada, no editar a mano).
- **`CAMBIOS.csv`** — fuente de datos (generada por el script).
- **`registrar_cambio.py`** — agrega una entrada, **purga las de más de 15 días** y regenera `CAMBIOS.md`.

## Registrar un cambio
```bash
python reportes/historial/registrar_cambio.py \
  --autor "Nombre" --clave Q-7 --campo "Estado" \
  --antes "Diseñado" --despues "In Review" --tipo normal
```

Cambio de **fecha** (campo controlado, requiere aprobación del owner — ver
`reportes/ALERTAS_FECHAS.md`):
```bash
python reportes/historial/registrar_cambio.py --autor "Meli" --clave Q-6 \
  --campo "Fecha de entrega" --antes "Julio 2026" --despues "Agosto 2026" \
  --tipo fecha --estado pendiente
# al aprobar:  ... --tipo fecha --estado aprobada
```

Solo purgar/regenerar (sin agregar):
```bash
python reportes/historial/registrar_cambio.py --solo-purgar
```

## Notas
- Retención: **15 días** (configurable en `registrar_cambio.py` → `RETENCION_DIAS`).
- Si quisieras un **repositorio Git aparte** solo para el historial, esta carpeta puede
  extraerse y publicarse igual que el skill (ver `scripts/publish_beholder_standalone.sh` como
  patrón).
