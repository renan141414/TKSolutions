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

# Testes usando pytest
def test_multiplicacao_escalar():
    matriz = [
        [2, 3],
        [4, 5]
    ]
    escalar = 3
    resultado_esperado = [
        [6, 9],
        [12, 15]
    ]
    resultado = [
        [elemento * escalar for elemento in linha]
        for linha in matriz
    ]
    assert resultado == resultado_esperado

def test_estrutura_matriz():
    matriz = [
        [2, 3],
        [4, 5]
    ]
    assert len(matriz) == 2
    for linha in matriz:
        assert len(linha) == 2

# Para rodar os testes com pytest, salve este código em um arquivo chamado test_matriz.py e execute:
# pytest test_matriz.py
