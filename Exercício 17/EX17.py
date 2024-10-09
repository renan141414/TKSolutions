# Arquivo: calcular_media.py

def calcular_media(numeros):
    """
    Calcula a média de uma lista de números.

    :param numeros: Lista de números (int ou float)
    :return: Média dos números (float)
    :raises ValueError: Se a lista estiver vazia
    :raises TypeError: Se a lista contiver elementos não numéricos
    """
    if not numeros:
        raise ValueError("A lista está vazia.")

    try:
        total = sum(numeros)
        media = total / len(numeros)
        return media
    except TypeError:
        raise TypeError("A lista contém elementos não numéricos.")


# Arquivo: test_calcular_media.py

import pytest
from calcular_media import calcular_media

def test_calcular_media_inteiros():
    assert calcular_media([1, 2, 3, 4, 5]) == 3.0

def test_calcular_media_floats():
    assert pytest.approx(calcular_media([10.5, 20.3, 30.7, 40.1]), 0.01) == 25.4

def test_calcular_media_unico_elemento():
    assert calcular_media([100]) == 100.0

def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError):
        calcular_media([])

def test_calcular_media_elementos_nao_numericos():
    with pytest.raises(TypeError):
        calcular_media([1, 2, "3", 4, 5])
