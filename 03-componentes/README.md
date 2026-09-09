# Fase 3 — Componentes e interactividad real

## Objetivo

Ir más allá del "un dropdown, un gráfico" y construir interfaces con múltiples
inputs, layouts responsivos y estética profesional.

## Qué aprender

- [ ] **Componentes `dcc`**: `Slider`, `RangeSlider`, `DatePickerRange`, `Tabs`, `Checklist`, `RadioItems`
- [ ] **Callbacks con múltiples Inputs/Outputs**
- [ ] **`State`** vs `Input` — cuándo dispara el callback y cuándo solo lee valor
- [ ] **`prevent_initial_call=True`** — para evitar callbacks al cargar
- [ ] **`dash-bootstrap-components`** — layouts con `Row`/`Col`, cards, navbar, temas
- [ ] **Callbacks con múltiples outputs** en una sola función
- [ ] **Callbacks encadenados** (output de uno = input del siguiente)

## Diferencia entre Input y State

```python
@callback(
    Output("resultado", "children"),
    Input("boton", "n_clicks"),          # dispara el callback
    State("campo-texto", "value"),       # solo lee el valor, NO dispara
)
def procesar(n_clicks, texto):
    return f"Procesé: {texto}"
```

Sin `State`, el callback correría cada tecla. Con `State`, solo al presionar el botón.

## Bootstrap para layouts

```python
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(id="g1"), width=6),
        dbc.Col(dcc.Graph(id="g2"), width=6),
    ]),
])
```

## Archivos por hacer

- `app_multi_input.py` — Slider de años + dropdown de especie
- `app_bootstrap.py` — Layout con dos columnas y una card informativa
- `app_tabs.py` — Múltiples vistas con pestañas

## Recursos

- 📖 [dcc components reference](https://dash.plotly.com/dash-core-components)
- 📖 [dash-bootstrap-components docs](https://dash-bootstrap-components.opensource.faculty.ai/)
- 🎥 [Carpeta Bootstrap del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Bootstrap)
