#Crie um programa que receba uma idade e retorne se pode obter carteira de motorista (CNH)

idade = input("Digite a sua idade: ")

try:
    if (int(idade) >= 18):
        print("Olá, seja bem vindo! Você tem idade suficiente para tirar a sua CNH.")
    else:
        print("Olá, seja bem vindo! Você ainda não idade suficiente para tirar a sua CNH.")

except ValueError:
    raise ValueError("Digite um valor de número válido.")
        