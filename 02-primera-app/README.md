# Fase 2 — Tu primera app Dash

## Objetivo

Entender el modelo mental de Dash: **layout + callbacks**.

## Analogía con Shiny (R)

| Shiny (R) | Dash (Python) |
|-----------|---------------|
| `ui <- fluidPage(...)` | `app.layout = html.Div([...])` |
| `server <- function(input, output) {...}` | Funciones decoradas con `@callback` |
| `reactive({...})` | Se declara explícitamente con `Input`/`Output` |
| `renderPlot({...})` | `Output("id", "figure")` |
| `input$mi_input` | argumento de la función callback |

**Diferencia clave:** en Dash todo es explícito — declaras qué input dispara qué output.
En Shiny, la reactividad es implícita.

## Qué aprender

- [ ] Estructura mínima de una app Dash
- [ ] Componentes HTML: `html.Div`, `html.H1`, `html.P`
- [ ] Componentes core: `dcc.Graph`, `dcc.Dropdown`, `dcc.Slider`
- [ ] El decorador `@callback` con `Input` y `Output`
- [ ] Modo `debug=True` — recarga automática al guardar

## Archivos en esta carpeta

- `app_hola_mundo.py` — App mínima sin interactividad
- `app_con_callback.py` — Dropdown que filtra un gráfico

## Cómo ejecutar

```bash
python app_hola_mundo.py
```

Abre en `http://127.0.0.1:8050/`. Con `debug=True`, al editar y guardar,
la app se recarga sola.

## Recursos

- 📖 [Dash Tutorial](https://dash.plotly.com/tutorial)
- 🎥 [Carpeta Dash_Interactive_Graphs del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Dash_Interactive_Graphs)
