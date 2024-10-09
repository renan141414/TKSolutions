import pytest


def encontrar_maximo(numeros):
    """
    Encontra o maior número em uma lista de números.

    :param numeros: Lista de números (int ou float)
    :return: O maior número da lista, ou None se a lista estiver vazia
    """
    if not numeros:  # Verifica se a lista está vazia
        return None

    try:
        return max(numeros)
    except TypeError:
        raise TypeError("A lista contém elementos não comparáveis.")


# Testes
def test_lista_normal():
    assert encontrar_maximo([1, 5, 3, 9, 2]) == 9


def test_lista_float():
    assert encontrar_maximo([10.5, 20.3, 30.7, 40.1]) == 40.1


def test_lista_um_elemento():
    assert encontrar_maximo([100]) == 100


def test_lista_vazia():
    assert encontrar_maximo([]) is None


def test_lista_negativos():
    assert encontrar_maximo([-5, -2, -10, -1]) == -1


def test_lista_com_elemento_nao_comparavel():
    with pytest.raises(TypeError):
        encontrar_maximo([1, 2, "3", 4, 5])


# Exemplo de uso interativo (não é um teste)
if __name__ == "__main__":
    try:
        entrada = input("Digite uma lista de números separados por espaço: ")
        lista_usuario = [float(x) for x in entrada.split()]
        maximo = encontrar_maximo(lista_usuario)
        if maximo is None:
            print("A lista está vazia.")
        else:
            print(f"O maior número na lista é: {maximo}")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")