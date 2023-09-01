def soma_com_parametros(x: int| float, y: int | float) -> int | float:
    """Soma x + y e retorna o resultado."""
    return x + y

# print(f"Resultado da soma com parâmetro: {soma(2.5, 10)}")

def print_subtracao(x: int| float, y: int | float) -> None:
    """Imprime o resultado da subtração entre x e y."""
    print(f"Resultado da subtração: {x - y}")

# print_subtracao(5, 2)

def soma_sem_parametro() -> int | float:
    """Retorna a soma das variáveis passadas dentro do código e retornará o resultado."""
    x = 5
    y = 6
    return x + y

# print(f"Resultado da soma sem parâmetro: {soma_sem_parametro()}")
