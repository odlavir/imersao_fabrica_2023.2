"""
Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. 
    - Mostre que ele foi multado. 
    - A multa deve ser no valor de 7R$ por cada km acima do limite.
"""

velocidadeDoMotorista = input("Digite a velocidade que o carro passou: ")


try:
    velocidadeDoMotorista_int = int(velocidadeDoMotorista)

    if (velocidadeDoMotorista_int > 80):
        velocidadeExcedida = velocidadeDoMotorista_int - 80
        valorMulta = velocidadeExcedida * 7
        print(f"O motorista passou em {velocidadeExcedida}km/h acima do permitido e receberá uma multa de R$ {valorMulta} reais.")
    elif (velocidadeDoMotorista_int == 80):
        print("O motorista passou no limite de velocidade.")
    else:
        print("O motorista passou abaixo do limite de velocidade.")

except ValueError:
    raise ValueError("Digite um valor de número válido.")