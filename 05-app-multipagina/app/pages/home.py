"""Página de inicio."""
from dash import html, register_page

register_page(__name__, path="/", name="Inicio")

layout = html.Div([
    html.H1("Dashboard analítico"),
    html.P("Bienvenido. Usa el menú superior para navegar."),
])
