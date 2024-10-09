def contar_vogais(texto):
    """
    Conta o número de vogais em uma string.

    :param texto: String para contar as vogais
    :return: Número de vogais na string
    """
    vogais = set('aeiouAEIOU')
    return sum(1 for caractere in texto if caractere in vogais)


# Testes usando pytest
def test_contar_vogais_minusculas():
    assert contar_vogais("hello") == 2

def test_contar_vogais_mixtas():
    assert contar_vogais("Hello World") == 3

def test_contar_vogais_sem_vogais():
    assert contar_vogais("rhythm") == 0

def test_contar_vogais_string_vazia():
    assert contar_vogais("") == 0

def test_contar_vogais_com_todas_as_vogais():
    assert contar_vogais("aeiouAEIOU") == 10

def test_contar_vogais_caracteres_especiais():
    assert contar_vogais("H3ll0, W0rld!") == 1


# Exemplo interativo
if __name__ == "__main__":
    texto_usuario = input("Digite um texto para contar as vogais: ")
    numero_vogais = contar_vogais(texto_usuario)
    print(f"O texto contém {numero_vogais} vogais.")
