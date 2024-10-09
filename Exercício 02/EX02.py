# Criando a matriz 2x2
matriz = [
    [2, 3],
    [4, 5]
]

# Definindo o número escalar
escalar = 3

# Multiplicando cada elemento da matriz pelo escalar
resultado = [
    [elemento * escalar for elemento in linha]
    for linha in matriz
]

# Função para exibir uma matriz formatada
def exibir_matriz(matriz, titulo="Matriz"):
    print(f"\n{titulo}:")
    for linha in matriz:
        print(" | ".join(f"{elemento:^5}" for elemento in linha))

# Exibindo a matriz original
exibir_matriz(matriz, "Matriz Original")

# Exibindo o escalar
print(f"\nEscalar: {escalar}")

# Exibindo o resultado da multiplicação
exibir_matriz(resultado, "Resultado da Multiplicação")

