# Fase 1 — Plotly puro (sin Dash todavía)

## Objetivo

Dominar Plotly antes de meterle Dash encima. Si dominas Plotly,
la mitad del trabajo de Dash ya está resuelta.

## Dos APIs de Plotly

1. **`plotly.express` (px)** — Alto nivel, una línea = un gráfico. **Empieza aquí.**
   Es lo más parecido a ggplot2 en filosofía.
2. **`plotly.graph_objects` (go)** — Bajo nivel, control total.
   Para cuando px no alcanza (gráficos combinados, subplots complejos).

## Qué aprender

- [ ] Gráficos básicos con px: `line`, `bar`, `scatter`, `histogram`, `box`
- [ ] Facetas: `facet_row`, `facet_col` (equivalente a `facet_wrap` de ggplot)
- [ ] Color/tamaño mapeado a variables
- [ ] Ejes logarítmicos, rangos, formato de fechas
- [ ] Personalización con `update_layout()`
- [ ] Exportar a HTML interactivo o PNG estático

## Ejercicio propuesto

Toma 3–4 gráficos que ya hayas hecho en ggplot2 y reprodúcelos en Plotly Express.
Compara el código: verás que la sintaxis es más compacta pero menos "declarativa".

## Recursos

- 📖 [Plotly Express Docs](https://plotly.com/python/plotly-express/)
- 📖 [Plotly Graphing Library](https://plotly.com/python/)
- 🎥 [Carpeta Plotly_Graphs del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Plotly_Graphs)

## Archivos en esta carpeta

- `01_grafico_lineas.py` — Serie de tiempo simple
- `02_facetas.py` — Múltiples paneles con facet_col
