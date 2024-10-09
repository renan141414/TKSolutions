def verificar_par_impar():
    try:
        # Solicita ao usuário um número inteiro
        numero = int(input("Por favor, digite um número inteiro: "))

        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")


# Executar o programa
verificar_par_impar()