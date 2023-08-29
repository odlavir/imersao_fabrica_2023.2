# Crie um programa que va de 0 à 30, mas pare quando encontrar o 20.

for i in range(0, 31):
    if (i == 20):
        print("Chegou no número 20, o programa parou!")
        break
    print(f"Número - {i}")