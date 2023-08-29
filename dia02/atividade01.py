#2. Implementando o try e exception no código do dia anterior.

numeroRecebido = input("Digite um número: ")

#numeroAntecessor = 0
#numeroSucessor = 0

try:
    numeroAntecessor = int(numeroRecebido) - 1
    numeroSucessor = int(numeroRecebido) + 1

except ValueError:
    raise ValueError("Digite um valor de número válido.")

print(f"O número recebido foi: {numeroRecebido}")
print(f"O número antecessor é: {numeroAntecessor}")
print(f"O número sucessor é: {numeroSucessor}")