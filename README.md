# Learn Dash — Ruta de aprendizaje

Repositorio personal para aprender **Dash + Plotly** desde cero, viniendo de R.
Organizado por fases progresivas siguiendo la estructura del repo educativo
[Coding-with-Adam/Dash-by-Plotly](https://github.com/Coding-with-Adam/Dash-by-Plotly).

## Objetivo final

Construir un dashboard interactivo con datos reales de mi trabajo.


---

## Ruta de aprendizaje

| Fase | Carpeta | Foco | Tiempo estimado |
|------|---------|------|-----------------|
| 0 | `00-python-basico/` | Python mínimo viable + pandas | 1–2 semanas |
| 1 | `01-plotly-puro/` | Plotly Express sin Dash | 1 semana |
| 2 | `02-primera-app/` | Layout + primer callback | 1 semana |
| 3 | `03-componentes/` | dcc + dash-bootstrap-components | 2 semanas |
| 4 | `04-tablas/` | DataTable y Ag-Grid | 1 semana |
| 5 | `05-app-multipagina/` | Dash Pages + estructura modular | 2–3 semanas |
| 6 | `06-deploy/` | Publicar en Render/Railway | 1 semana |
| ★ | `capstone/` | Proyecto propio con datos reales | 2–4 semanas |

---

## Setup inicial

### 1. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
# .venv\Scripts\activate         # Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Verificar que Dash funciona

```bash
python 02-primera-app/app_hola_mundo.py
```

Debería abrirse en `http://127.0.0.1:8050/`.

---

## Recursos clave

- 📁 [`recursos/cheatsheet-r-python.md`](recursos/cheatsheet-r-python.md) — Equivalencias R ↔ Python (dplyr, ggplot, Shiny)
- 📁 [`recursos/enlaces.md`](recursos/enlaces.md) — Documentación oficial, videos, foros
- 🎥 [Canal Charming Data](https://www.youtube.com/@CharmingData) — Videos del autor del repo base

---

## Subir a GitHub

```bash
git init
git add .
git commit -m "Inicio: estructura y roadmap"
git branch -M main
git remote add origin https://github.com/Rjara1942/learn-dash.git
git push -u origin main
```
