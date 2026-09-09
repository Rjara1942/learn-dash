"""
Fase 2 — App mínima de Dash
============================

Estructura:
  1. Importar Dash y componentes
  2. Crear la instancia app
  3. Definir el layout (qué se ve)
  4. Ejecutar el servidor

Ejecutar:  python app_hola_mundo.py
Abrir:     http://127.0.0.1:8050/
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# --- 1. Datos ---
df = pd.DataFrame({
    "año":    [2020, 2021, 2022, 2023, 2024],
    "precio": [420, 445, 460, 475, 480],
})

fig = px.line(df, x="año", y="precio", markers=True,
              title="Precio ex-vessel sardina (CLP/kg)")

# --- 2. Instancia de la app ---
app = Dash(__name__)

# --- 3. Layout ---
app.layout = html.Div([
    html.H1("Mi primera app Dash"),
    html.P("Este es un párrafo descriptivo del dashboard."),
    dcc.Graph(figure=fig),
])

# --- 4. Ejecutar ---
if __name__ == "__main__":
    app.run(debug=True)
