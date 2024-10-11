import random

dinero = 1000

def tirada():
    dado = random.randint(1,6)
    moneda = random.choice(["Cara","Sello"])
    return dado, moneda

def apuesta(apostado):
    global dinero
    dado, moneda = tirada()
    print(f"Dado: {dado} -- Moneda: {moneda}")
    if ((dado % 2) == 0) and moneda == "cara":
        print("Usted ha ganado")
        dinero += apostado*2
    else:
        print("Usted ha perdido")
        dinero -= apostado
    
while dinero > 0:
    dinero_apostado = int(input(f"Dinero: {dinero}$ - ¿Cuanto desea APOSTAR? - "))
    apuesta(dinero_apostado)

print("Te haz quedado sin dinero, Gracias por jugar.")