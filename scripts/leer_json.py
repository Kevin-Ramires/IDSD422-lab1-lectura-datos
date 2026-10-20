# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa json y pandas
import json
import pandas as pd
# TODO 2: carga data/ventas.json con json.load
with open("data/ventas.json") as f:
    datos = json.load(f)
# TODO 3: convierte la lista de diccionarios en un DataFrame
ventas = pd.DataFrame(datos)

#         (recuerda del cap. 2: el JSON no llega como tabla directa)
# TODO 4: imprime las dimensiones y las primeras filas
print(ventas.head())
print(ventas.shape)
