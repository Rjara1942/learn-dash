"""
Fase 5 — App multipágina (esqueleto)

Estructura mínima con Dash Pages. Cada archivo en pages/ se registra
automáticamente al usar use_pages=True.

Ejecutar:  python app/app.py
"""

from dash import Dash, html, page_container, page_registry
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

# Navbar con links a todas las páginas registradas
navbar = dbc.NavbarSimple(
    brand="Mi Dashboard",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
        for page in page_registry.values()
    ],
)

app.layout = html.Div([
    navbar,
    dbc.Container(page_container, className="pt-4"),
])

# Necesario para deploy con gunicorn
server = app.server

if __name__ == "__main__":
    app.run(debug=True)
