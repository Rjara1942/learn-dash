# Fase 6 — Deploy

## Objetivo

Publicar tu app en internet para compartirla.

## Opciones actuales (2026)

| Servicio | Nivel gratis | Facilidad | Notas |
|----------|--------------|-----------|-------|
| **Render** | Sí (con límites) | ⭐⭐⭐⭐⭐ | Recomendado para empezar |
| **Railway** | $5 crédito inicial | ⭐⭐⭐⭐⭐ | Muy pulido, buena UX |
| **Fly.io** | Sí (con límites) | ⭐⭐⭐ | Más control, más complejo |
| **PythonAnywhere** | Sí | ⭐⭐⭐⭐ | Bueno para prototipos |
| ~~Heroku~~ | ❌ | — | Ya no tiene tier gratuito |

## Requisitos mínimos para deploy

### 1. `requirements.txt`
Con las dependencias exactas (o rangos):
```
dash>=2.17
plotly>=5.20
pandas>=2.0
gunicorn>=21
```

### 2. Servidor de producción — **gunicorn**
El servidor de desarrollo de Dash (`app.run(debug=True)`) **no** sirve para producción.
Se usa `gunicorn` (Linux/Mac).

Requisito clave: tu app debe exponer `server = app.server` para que gunicorn lo encuentre.

### 3. Comando de start
En Render/Railway:
```bash
gunicorn app:server
```
Donde `app` es el nombre del archivo Python (sin `.py`) y `server` el atributo.

### 4. Variables de entorno
Nunca subas contraseñas o API keys al repo. Usa variables de entorno:
```python
import os
DB_URL = os.getenv("DB_URL")
```
Y configúralas en el dashboard del servicio.

## Checklist antes de deployar

- [ ] `requirements.txt` completo y probado en un venv limpio
- [ ] `server = app.server` expuesto en el archivo principal
- [ ] `debug=False` (o al menos configurable con env var)
- [ ] `.gitignore` excluye `.env`, `.venv/`, secretos
- [ ] La app corre localmente sin errores en consola
- [ ] Datos: si son grandes, usar almacenamiento externo (no subir CSVs enormes al repo)

## Archivos en esta carpeta

- `Procfile` — para Heroku-style deploys (algunos servicios lo aceptan)
- `render.yaml` — configuración declarativa para Render

## Recursos

- 📖 [Deploy Dash apps (docs oficiales)](https://dash.plotly.com/deployment)
- 🎥 [Carpeta Deploy_App_to_Web del repo base](https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Deploy_App_to_Web)
