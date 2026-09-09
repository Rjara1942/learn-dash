"""
Fase 1 — Gráfico de líneas con Plotly Express

Equivalente en R (ggplot):
    ggplot(df, aes(x = año, y = precio, color = especie)) +
      geom_line() + geom_point()
"""

import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "año":     list(range(2015, 2025)) * 2,
    "especie": ["Sardina"] * 10 + ["Anchoveta"] * 10,
    "precio":  [380, 395, 410, 405, 420, 435, 445, 460, 475, 480,
                290, 305, 315, 310, 325, 330, 335, 340, 350, 355],
})

# Un gráfico con una línea por especie (color mapea a variable)
fig = px.line(
    df,
    x="año",
    y="precio",
    color="especie",
    markers=True,
    title="Precio ex-vessel promedio (CLP/kg)",
    labels={"precio": "Precio (CLP/kg)", "año": "Año"},
)

# Personalizar layout (equivalente a theme() en ggplot)
fig.update_layout(
    template="plotly_white",
    hovermode="x unified",
    legend_title_text="Especie",
)

# Mostrar en navegador
fig.show()

# Guardar como HTML interactivo (se puede compartir por email)
fig.write_html("precio_pelagicos.html")
print("✓ Gráfico guardado en precio_pelagicos.html")
