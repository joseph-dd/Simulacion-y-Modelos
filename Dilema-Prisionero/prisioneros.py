import random

def prisioneros():
    opciones = ["Cooperar", "Traicionar"]
    
    eleccion1 = random.choice(opciones)
    eleccion2 = random.choice(opciones)

    print(f"\nELECCIONES:\nEl primer prisionero elige {eleccion1}\nEl segundo prisionero elige {eleccion2}")

    if eleccion1 == "Cooperar" and eleccion2 == "Cooperar":
        return [1, 1]
    elif eleccion1 == "Cooperar" and eleccion2 == "Traicionar":
        return [10, 0]
    elif eleccion1 == "Traicionar" and eleccion2 == "Cooperar":
        return [0, 10]
    else:
        return [3, 3]

resultado = prisioneros()

print(f"\nRESULTADO:\nEl primer prisionero debera recibira {resultado[0]} años en prision\nEl segundo prisionero recibira {resultado[1]} años en prision\n")
