"""Página de exploración — placeholder."""
from dash import html, register_page

register_page(__name__, path="/exploracion", name="Exploración")

layout = html.Div([
    html.H2("Exploración de datos"),
    html.P("Aquí irán filtros y gráficos exploratorios."),
])
