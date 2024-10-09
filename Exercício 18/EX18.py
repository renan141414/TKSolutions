def contar_vogais(texto):
    """
    Conta o número de vogais em uma string.

    :param texto: String para contar as vogais
    :return: Número de vogais na string
    """
    # Conjunto de vogais (maiúsculas e minúsculas)
    vogais = set('aeiouAEIOU')

    # Conta o número de caracteres no texto que estão no conjunto de vogais
    return sum(1 for caractere in texto if caractere in vogais)


# Testes da função
def testar_contar_vogais():
    print("Testando a função contar_vogais:")

    # Teste 1: String com vogais minúsculas
    print("Teste 1:", contar_vogais("hello") == 2)

    # Teste 2: String com vogais maiúsculas e minúsculas
    print("Teste 2:", contar_vogais("Hello World") == 3)

    # Teste 3: String sem vogais
    print("Teste 3:", contar_vogais("rhythm") == 0)

    # Teste 4: String vazia
    print("Teste 4:", contar_vogais("") == 0)

    # Teste 5: String com todas as vogais
    print("Teste 5:", contar_vogais("aeiouAEIOU") == 10)

    # Teste 6: String com caracteres especiais e números
    print("Teste 6:", contar_vogais("H3ll0, W0rld!") == 1)


if __name__ == "__main__":
    testar_contar_vogais()

    # Exemplo interativo
    texto_usuario = input("\nDigite um texto para contar as vogais: ")
    numero_vogais = contar_vogais(texto_usuario)
    print(f"O texto contém {numero_vogais} vogais.")