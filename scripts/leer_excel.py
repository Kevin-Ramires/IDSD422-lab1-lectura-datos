# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
import pandas as pd

# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
ventas=pd.ExcelFile("data/ventas.xlsx")
print(ventas.sheet_names)

# TODO 3: imprime las dimensiones y las primeras filas
ventas1= pd.read_excel(ventas, sheet_name="ventas")
print(ventas1.head())
print(ventas1.shape)
