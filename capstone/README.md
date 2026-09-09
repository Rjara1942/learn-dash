# Capstone — Proyecto final

## Por qué un capstone

Un dashboard bien terminado vale más que 20 tutoriales aislados.
Además te queda como pieza de portafolio (perfil de GitHub, LinkedIn, CV).

## Ideas de proyecto

### Opción A — Dashboard tesis pesquera 🐟

**Datos:** Precios ex-vessel y desembarques del complejo sardina-anchoveta,
centro-sur de Chile.

**Vistas:**
- Serie temporal de precios (filtros: año, puerto, flota, especie)
- Mapa de desembarques por puerto (`px.scatter_mapbox`)
- Panel del modelo econométrico: coeficientes con intervalos de confianza
- Tabla de resultados de regresión (Ag-Grid) exportable

**Uso real:** presentar a IDECLab, adjuntar en la defensa, compartir con el gremio.

---

### Opción B — Explorador RBC-Chile 📈

**Datos:** Modelo Real Business Cycle calibrado con datos chilenos.

**Vistas:**
- Sliders para parámetros clave (β, δ, α, ρ, σ)
- Funciones impulso-respuesta que se actualizan en tiempo real
- Comparación entre modelo y momentos empíricos
- Tabla de momentos teóricos vs observados

**Uso real:** herramienta didáctica para ayudantías o para tu propia investigación.

---

### Opción C — Dashboard Econometría I 📚

**Datos:** Datasets usados en la ayudantía.

**Vistas:**
- Selector de dataset y modelo (OLS, IV, panel)
- Diagnósticos: residuos vs ajustados, QQ-plot, VIF
- Tabla de coeficientes con std. errors robustos
- Descarga de resultados en formato reporte

**Uso real:** los estudiantes lo usan para verificar tareas y explorar supuestos.

## Estructura sugerida del proyecto capstone

```
capstone/
├── README.md              # descripción, screenshots, link al deploy
├── app.py                 # entrada
├── requirements.txt
├── data/                  # datos (o script para descargarlos)
├── src/
│   ├── loader.py          # cargar y limpiar datos
│   ├── modelo.py          # cálculos econométricos
│   └── figuras.py         # funciones que retornan figuras Plotly
├── pages/                 # si es multipágina
└── assets/
    └── style.css
```

## Buenas prácticas

- **Escribe tests**: al menos que las funciones que retornan figuras no crasheen.
- **Documenta**: README con screenshots y un GIF corto es 10x más atractivo.
- **Deploy**: publicalo. Un dashboard local que nadie ve no cuenta.
- **Versiona los datos**: si son públicos, ok subirlos. Si no, incluye un script
  para descargarlos con instrucciones.
