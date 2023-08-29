#1. Crie um programa que peça um número e mostre o seu sucessor e antecessor

numeroRecebido = int(input("Digite um número: "))

numeroAntecessor = numeroRecebido - 1
numeroSucessor = numeroRecebido + 1

print(f"O número recebido foi: {numeroRecebido}")
print(f"O número antecessor é: {numeroAntecessor}")
print(f"O número sucessor é: {numeroSucessor}")
