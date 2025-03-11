import random

# Parámetros de la simulación
probabilidad_enc = 40
costo_exploracion = 1000000
num_barriles = 300000
costo_barril = 150
simulaciones = 20

# Variables para almacenar los resultados totales
total_exitos = 0
total_fracasos = 0
ganancia_total = 0
perdida_total = 0

# Realizar las simulaciones
for i in range(simulaciones):
    resultado = random.randint(1, 100)

    if resultado <= probabilidad_enc:
        beneficio = num_barriles * costo_barril
        beneficio_empresa = beneficio * 0.60
        
        total_exitos += 1
        ganancia_total += beneficio_empresa
    else:
        total_fracasos += 1
        perdida_total += costo_exploracion

# Calcular el balance final
balance_final = ganancia_total - perdida_total

# Mostrar el resumen de las simulaciones
print("\n=== Resumen de las Simulaciones ===")
print(f"Total de simulaciones: {simulaciones}")
print(f"Exploraciones exitosas: {total_exitos}")
print(f"Exploraciones fallidas: {total_fracasos}")
print(f"Ganancia total de la empresa: {ganancia_total}")
print(f"Pérdida total por exploraciones fallidas: {perdida_total}")
print(f"Balance final: {balance_final}")
print(f"Tasa de éxito: {(total_exitos / simulaciones) * 100:.2f}%")