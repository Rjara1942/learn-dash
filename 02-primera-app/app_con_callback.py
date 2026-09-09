"""
Fase 2 — App con callback
==========================

Ahora el gráfico reacciona a un dropdown.
Esta es la estructura reactiva básica de Dash:

    Usuario cambia INPUT  ─→  callback se dispara  ─→  OUTPUT se actualiza

Ejecutar:  python app_con_callback.py
"""

from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

# --- Datos ---
df = pd.DataFrame({
    "año":     list(range(2015, 2025)) * 3,
    "especie": ["Sardina"] * 10 + ["Anchoveta"] * 10 + ["Jurel"] * 10,
    "precio":  [380, 395, 410, 405, 420, 435, 445, 460, 475, 480,
                290, 305, 315, 310, 325, 330, 335, 340, 350, 355,
                510, 525, 540, 535, 550, 565, 575, 590, 605, 615],
})

# --- App ---
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Precios ex-vessel por especie"),
    html.Label("Selecciona una especie:"),
    dcc.Dropdown(
        id="dropdown-especie",
        options=[{"label": e, "value": e} for e in df["especie"].unique()],
        value="Sardina",
        clearable=False,
        style={"width": "300px"},
    ),
    dcc.Graph(id="grafico-precio"),
])

# --- Callback ---
# Cuando el valor del dropdown cambia, esta función se ejecuta
# y su return va al 'figure' del dcc.Graph.
@callback(
    Output("grafico-precio", "figure"),
    Input("dropdown-especie", "value"),
)
def actualizar_grafico(especie_seleccionada):
    filtrado = df[df["especie"] == especie_seleccionada]
    fig = px.line(
        filtrado,
        x="año",
        y="precio",
        markers=True,
        title=f"Precio ex-vessel — {especie_seleccionada}",
    )
    fig.update_layout(template="plotly_white")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
