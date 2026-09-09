"""
Fase 1 — Facetas (small multiples)

Equivalente en R (ggplot):
    ggplot(df, aes(x = año, y = valor)) +
      geom_line() +
      facet_wrap(~ variable, scales = "free_y")
"""

import plotly.express as px
import pandas as pd

# Datos en formato largo (tidy data — mismo principio que en R)
años = list(range(2015, 2025))
df = pd.DataFrame({
    "año":      años * 3,
    "variable": ["Precio"] * 10 + ["Captura"] * 10 + ["Ingreso"] * 10,
    "valor":    [380, 395, 410, 405, 420, 435, 445, 460, 475, 480,
                 120, 118, 125, 122, 128, 135, 138, 142, 145, 148,
                 45600, 46610, 51250, 49410, 53760, 58725, 61410, 65320, 68875, 71040],
})

fig = px.line(
    df,
    x="año",
    y="valor",
    facet_col="variable",           # equivalente a facet_wrap
    facet_col_wrap=3,
    markers=True,
    title="Serie histórica sardina: precio, captura, ingreso",
)

# Que cada faceta tenga su propio eje Y (como scales = "free_y")
fig.update_yaxes(matches=None)

# Limpiar los títulos de faceta (por defecto vienen "variable=Precio")
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

fig.update_layout(template="plotly_white", showlegend=False)

fig.show()
