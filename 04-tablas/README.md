# Fase 4 — Tablas interactivas

## Objetivo

Mostrar datos tabulares que el usuario puede filtrar, ordenar, editar y exportar.
Crítico para trabajos de economía: coeficientes de regresión, series desagregadas,
resultados de estimaciones.

## Dos opciones

### 1. `dash_table.DataTable` (clásico)
- Viene incluido en `dash`
- Bueno para casos simples
- Sintaxis un poco verbosa

### 2. `dash-ag-grid` (recomendado hoy)
- Basado en AG Grid (líder de mercado en tablas web)
- Filtros avanzados, agrupación, edición, pinning
- Mejor para tablas grandes

```python
import dash_ag_grid as dag

dag.AgGrid(
    id="tabla",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": c} for c in df.columns],
    defaultColDef={"filter": True, "sortable": True, "resizable": True},
)
```

## Qué aprender

- [ ] Renderizar un DataFrame como tabla interactiva
- [ ] Definir tipos de columna (numérica, texto, fecha)
- [ ] Formatos (moneda, porcentaje, decimales)
- [ ] Filtros por columna
- [ ] Editar celdas y capturar el cambio con callback
- [ ] Exportar a CSV/Excel desde la UI

## Recursos

- 📖 [dash-ag-grid docs](https://dash.plotly.com/dash-ag-grid)
- 📖 [DataTable docs](https://dash.plotly.com/datatable)
- 🎥 [Carpeta Ag-Grid del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Ag-Grid)
