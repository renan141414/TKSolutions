import pytest


def converter_temperatura(celsius, tipo="F"):
    """
    Converte uma temperatura em Celsius para Fahrenheit ou Kelvin.

    :param celsius: Temperatura em Celsius (float)
    :param tipo: Tipo de conversão - "F" para Fahrenheit ou "K" para Kelvin (string, opcional)
    :return: Temperatura convertida (float)
    :raises ValueError: Se o tipo de conversão não for "F" ou "K"
    """
    if tipo.upper() == "F":
        return (celsius * 9 / 5) + 32
    elif tipo.upper() == "K":
        return celsius + 273.15
    else:
        raise ValueError("Tipo de conversão inválido. Use 'F' para Fahrenheit ou 'K' para Kelvin.")


# Testes usando pytest
def test_celsius_para_fahrenheit():
    assert converter_temperatura(0) == 32
    assert converter_temperatura(100) == 212
    assert round(converter_temperatura(37), 2) == 98.60

def test_celsius_para_fahrenheit_explicito():
    assert converter_temperatura(0, "F") == 32
    assert converter_temperatura(100, "f") == 212

def test_celsius_para_kelvin():
    assert converter_temperatura(0, "K") == 273.15
    assert converter_temperatura(100, "k") == 373.15

def test_temperatura_negativa():
    assert round(converter_temperatura(-40), 2) == -40.00
    assert round(converter_temperatura(-273.15, "K"), 2) == 0.00

def test_tipo_invalido():
    with pytest.raises(ValueError):
        converter_temperatura(0, "C")


# Exemplo interativo
if __name__ == "__main__":
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        tipo = input("Digite o tipo de conversão (F para Fahrenheit, K para Kelvin) ou pressione Enter para Fahrenheit: ")

        if not tipo:
            tipo = "F"

        resultado = converter_temperatura(celsius, tipo)
        unidade = "Fahrenheit" if tipo.upper() == "F" else "Kelvin"
        print(f"{celsius}°C é igual a {resultado:.2f}°{unidade}")
    except ValueError as e:
        print(f"Erro: {e}")
