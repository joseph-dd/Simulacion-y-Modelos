import random

probabilidad_enc = 40
costo_exploracion = 1000000
num_barriles = 300000
costo_barril = 150

resultado = random.randint(1,100)
if resultado <= probabilidad_enc :
    beneficio = num_barriles*costo_barril
    print(f"\nSe consiguió petroleo\nBeneficio total:{beneficio}\nBeneficio de la empresa:{beneficio*0.60}\n")
else:
    print("\nNo se consiguió petroleo\n")