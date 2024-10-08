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

# Exibindo a matriz original
print("Matriz original:")
for linha in matriz:
    print(linha)

# Exibindo o escalar
print(f"\nEscalar: {escalar}")

# Exibindo o resultado
print("\nResultado da multiplicação:")
for linha in resultado:
    print(linha)