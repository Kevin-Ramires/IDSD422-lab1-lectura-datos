# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
import pandas as pd
ventas = pd.read_csv("data/ventas.csv")
# TODO 2: imprime los tipos (dtypes) de cada columna
print(ventas.dtypes)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
print(ventas.head())
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
print("Venta promedio:", ventas["ventas"].mean())
#         - ticket promedio (ventas totales / clientes totales)
print("Ticket promedio:", ventas["ventas"].sum() / ventas["clientes"].sum())
#         - sucursal con mayor y menor venta
print("Mayor venta:", ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
print("Menor venta:", ventas.loc[ventas["ventas"].idxmin(), "sucursal"])
#         - región con mayor venta total
print("Región top:", ventas.groupby("region")["ventas"].sum().idxmax())
