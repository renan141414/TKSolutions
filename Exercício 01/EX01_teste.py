# Código original para teste
def formatar_matriz(matriz):
    return "\n".join(" | ".join(f"{elemento:^3}" for elemento in linha).rstrip() for linha in matriz)


# Testes usando pytest
def test_matriz_formato():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    resultado_esperado = (
        " 1  |  2  |  3\n"
        " 4  |  5  |  6\n"
        " 7  |  8  |  9"
    )
    
    assert formatar_matriz(matriz) == resultado_esperado

def test_estrutura_matriz():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Verificando o tamanho da matriz
    assert len(matriz) == 3
    for linha in matriz:
        assert len(linha) == 3

# Para rodar os testes com pytest, salve este código em um arquivo chamado test_matriz.py e execute:
# pytest test_matriz.py
