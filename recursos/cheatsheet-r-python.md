# Cheatsheet R → Python

Equivalencias rápidas para no perder tiempo buscando "cómo hago X de dplyr en pandas".

## Manipulación de datos: dplyr/tidyr ↔ pandas

Todos los ejemplos asumen:
```python
import pandas as pd
df = pd.DataFrame({...})
```

| Operación | R (dplyr/tidyr) | Python (pandas) |
|-----------|-----------------|-----------------|
| Filtrar filas | `df %>% filter(x > 5)` | `df[df["x"] > 5]` o `df.query("x > 5")` |
| Seleccionar columnas | `df %>% select(a, b)` | `df[["a", "b"]]` |
| Quitar columnas | `df %>% select(-a)` | `df.drop(columns="a")` |
| Renombrar | `df %>% rename(nueva = vieja)` | `df.rename(columns={"vieja": "nueva"})` |
| Crear columna | `df %>% mutate(z = x + y)` | `df["z"] = df["x"] + df["y"]` |
| Ordenar | `df %>% arrange(x)` | `df.sort_values("x")` |
| Descendente | `df %>% arrange(desc(x))` | `df.sort_values("x", ascending=False)` |
| Agrupar y resumir | `df %>% group_by(g) %>% summarise(m = mean(x))` | `df.groupby("g", as_index=False).agg(m=("x", "mean"))` |
| Contar | `df %>% count(g)` | `df["g"].value_counts()` |
| Distinct | `df %>% distinct(g)` | `df["g"].unique()` o `df.drop_duplicates("g")` |
| Pivot longer | `pivot_longer(cols, names_to, values_to)` | `df.melt(id_vars, value_vars, var_name, value_name)` |
| Pivot wider | `pivot_wider(names_from, values_from)` | `df.pivot(index, columns, values).reset_index()` |
| Join | `left_join(x, y, by = "id")` | `x.merge(y, on="id", how="left")` |
| Encadenar | `%>%` (pipe) | `.` (métodos) o `.pipe(func)` |

### Ejemplo lado a lado

**R:**
```r
resultado <- df %>%
  filter(año >= 2020) %>%
  group_by(especie) %>%
  summarise(precio_medio = mean(precio, na.rm = TRUE)) %>%
  arrange(desc(precio_medio))
```

**Python:**
```python
resultado = (
    df.query("año >= 2020")
      .groupby("especie", as_index=False)
      .agg(precio_medio=("precio", "mean"))
      .sort_values("precio_medio", ascending=False)
)
```

---

## Visualización: ggplot2 ↔ Plotly Express

| Concepto | ggplot2 | Plotly Express |
|----------|---------|----------------|
| Estructura | `ggplot(df, aes(...)) + geom_*()` | `px.tipo(df, x, y, color, ...)` |
| Línea | `geom_line()` | `px.line()` |
| Puntos | `geom_point()` | `px.scatter()` |
| Barras | `geom_bar()` / `geom_col()` | `px.bar()` |
| Histograma | `geom_histogram()` | `px.histogram()` |
| Box plot | `geom_boxplot()` | `px.box()` |
| Facetas | `facet_wrap(~ var)` | `facet_col="var"` (argumento) |
| Color por variable | `aes(color = var)` | `color="var"` |
| Tema | `+ theme_minimal()` | `template="plotly_white"` |
| Título de eje | `+ labs(x = "Año")` | `labels={"x": "Año"}` |

---

## Framework web: Shiny ↔ Dash

| Concepto | Shiny (R) | Dash (Python) |
|----------|-----------|---------------|
| App | `shinyApp(ui, server)` | `Dash(__name__)` |
| UI declarativa | `fluidPage(...)` | `app.layout = html.Div([...])` |
| Componente input | `selectInput("id", ...)` | `dcc.Dropdown(id="id", ...)` |
| Componente output | `plotOutput("id")` | `dcc.Graph(id="id")` |
| Reactividad | Implícita con `reactive()` | Explícita con `@callback` |
| Leer input | `input$id` | argumento del callback |
| Actualizar output | `output$id <- renderPlot({...})` | `Output("id", "figure")` |
| Ejecutar | `runApp()` | `app.run(debug=True)` |

### Ejemplo lado a lado

**Shiny:**
```r
ui <- fluidPage(
  selectInput("especie", "Especie:", choices = c("Sardina", "Anchoveta")),
  plotOutput("grafico")
)
server <- function(input, output) {
  output$grafico <- renderPlot({
    ggplot(filter(df, especie == input$especie), aes(año, precio)) + geom_line()
  })
}
```

**Dash:**
```python
app.layout = html.Div([
    dcc.Dropdown(id="especie", options=["Sardina", "Anchoveta"], value="Sardina"),
    dcc.Graph(id="grafico"),
])

@callback(Output("grafico", "figure"), Input("especie", "value"))
def actualizar(especie):
    return px.line(df.query("especie == @especie"), x="año", y="precio")
```

---

## Gotchas de Python para gente de R

| Cosa | R | Python |
|------|---|--------|
| Índice base | 1 | 0 |
| Asignación | `<-` o `=` | solo `=` |
| Concatenar strings | `paste0("a", "b")` | `"a" + "b"` o f-strings |
| NA | `NA` | `None` o `np.nan` |
| Booleano | `TRUE`, `FALSE` | `True`, `False` |
| Comentario | `#` | `#` (igual ✓) |
| Función | `f <- function(x) {...}` | `def f(x): ...` |
| Return implícito | Sí | **No** — hay que escribir `return` |
| Punto en nombres | `mi.variable` ok | `mi.variable` = acceso a atributo. Usa `mi_variable` |
| Copia vs referencia | Copy-on-modify (seguro) | Referencia (¡cuidado con `df2 = df1`!) — usa `df2 = df1.copy()` |

---

## Recursos para profundizar

- 📖 [Python for R Users (Chapman & Hall)](https://www.oreilly.com/library/view/python-for-r/9781119126751/)
- 📖 [pandas Comparison with R / R libraries](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html) ← oficial
- 📖 [Plotly Express vs ggplot2](https://plotly.com/python/plotly-express/)
- 🐍 [Real Python — pandas tutorials](https://realpython.com/learning-paths/pandas-data-science/)
