"""
Fase 0 — Operaciones básicas en pandas
=======================================

Este archivo muestra las operaciones más comunes de dplyr/tidyr en pandas.
Ejecutar con:  python 01_pandas_basico.py
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------
# 1. Crear un DataFrame (equivalente a tibble/data.frame en R)
# ---------------------------------------------------------------
df = pd.DataFrame({
    "año":       [2020, 2020, 2021, 2021, 2022, 2022, 2023, 2023],
    "especie":   ["sardina", "anchoveta"] * 4,
    "captura":   [120, 85, 135, 92, 128, 88, 142, 95],
    "precio":    [420, 310, 445, 335, 460, 340, 480, 355],
})

print("DataFrame original:")
print(df)
print()

# ---------------------------------------------------------------
# 2. Filtrar filas
# ---------------------------------------------------------------
# R:  df %>% filter(especie == "sardina")
sardina = df[df["especie"] == "sardina"]
# Alternativa más legible con .query():
# sardina = df.query("especie == 'sardina'")

# ---------------------------------------------------------------
# 3. Seleccionar columnas
# ---------------------------------------------------------------
# R:  df %>% select(año, precio)
subset = df[["año", "precio"]]

# ---------------------------------------------------------------
# 4. Crear nuevas columnas (mutate)
# ---------------------------------------------------------------
# R:  df %>% mutate(ingreso = captura * precio)
df["ingreso"] = df["captura"] * df["precio"]

# Alternativa inmutable (crea una copia):
# df = df.assign(ingreso=lambda x: x["captura"] * x["precio"])

# ---------------------------------------------------------------
# 5. Agrupar y resumir
# ---------------------------------------------------------------
# R:  df %>% group_by(especie) %>% summarise(precio_medio = mean(precio))
resumen = df.groupby("especie", as_index=False).agg(
    precio_medio=("precio", "mean"),
    captura_total=("captura", "sum"),
)
print("Resumen por especie:")
print(resumen)
print()

# ---------------------------------------------------------------
# 6. Ordenar
# ---------------------------------------------------------------
# R:  df %>% arrange(desc(ingreso))
ordenado = df.sort_values("ingreso", ascending=False)

# ---------------------------------------------------------------
# 7. Pivot longer (formato wide → long)
# ---------------------------------------------------------------
# R:  df %>% pivot_longer(cols = c(captura, precio), names_to = "variable")
largo = df.melt(
    id_vars=["año", "especie"],
    value_vars=["captura", "precio"],
    var_name="variable",
    value_name="valor",
)
print("Formato largo (primeras 5 filas):")
print(largo.head())
print()

# ---------------------------------------------------------------
# 8. Pivot wider (formato long → wide)
# ---------------------------------------------------------------
# R:  largo %>% pivot_wider(names_from = variable, values_from = valor)
ancho = largo.pivot_table(
    index=["año", "especie"],
    columns="variable",
    values="valor",
).reset_index()

# ---------------------------------------------------------------
# 9. Joins (merge)
# ---------------------------------------------------------------
metadata = pd.DataFrame({
    "especie": ["sardina", "anchoveta"],
    "nombre_cientifico": ["Sardinops sagax", "Engraulis ringens"],
})
# R:  left_join(df, metadata, by = "especie")
enriquecido = df.merge(metadata, on="especie", how="left")

# ---------------------------------------------------------------
# 10. Leer/escribir archivos
# ---------------------------------------------------------------
# R:  read_csv("archivo.csv") / write_csv(df, "salida.csv")
# df = pd.read_csv("archivo.csv")
# df.to_csv("salida.csv", index=False)
# df.to_excel("salida.xlsx", index=False)

print("✓ Ejercicio completado. Prueba modificar el DataFrame y explorar.")
