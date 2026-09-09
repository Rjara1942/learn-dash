# Fase 5 — App analítica completa (multipágina)

## Objetivo

Pasar de "script con dashboard" a **aplicación estructurada** con:
- Múltiples páginas navegables (URL routing)
- Layouts reutilizables
- Datos compartidos entre páginas
- Estructura modular escalable

## Estructura recomendada

```
app/
├── app.py                  # entrada principal
├── pages/
│   ├── home.py             # página de inicio
│   ├── exploracion.py      # análisis exploratorio
│   └── modelo.py           # resultados del modelo
├── components/
│   ├── navbar.py           # componentes reutilizables
│   └── sidebar.py
├── data/
│   └── loader.py           # funciones para cargar datos
└── assets/
    └── style.css           # CSS custom (Dash lo carga solo)
```

## Dash Pages

Desde Dash 2.5+, hay un sistema de páginas incorporado:

```python
# app.py
from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.NavbarSimple(brand="Mi Dashboard", color="primary", dark=True),
    page_container,   # aquí se renderiza cada página
])

if __name__ == "__main__":
    app.run(debug=True)
```

Cada archivo en `pages/` se registra automáticamente:

```python
# pages/home.py
from dash import html, register_page

register_page(__name__, path="/", name="Inicio")

layout = html.Div([html.H1("Bienvenido")])
```

## Qué aprender

- [ ] `use_pages=True` y `register_page`
- [ ] `dcc.Location` y `dcc.Link` para navegación
- [ ] `dcc.Store` para compartir datos entre callbacks/páginas
- [ ] Callbacks con `pattern-matching` (para componentes dinámicos)
- [ ] Cargar datos una sola vez y cachear (`@functools.lru_cache` o `flask-caching`)
- [ ] Assets folder — CSS y JS custom cargan automáticamente

## Recursos

- 📖 [Dash Pages docs](https://dash.plotly.com/urls)
- 📖 [dcc.Store](https://dash.plotly.com/dash-core-components/store)
- 🎥 [Carpeta Analytic_Web_Apps del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Analytic_Web_Apps)
