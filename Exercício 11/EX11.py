def verificar_par_impar():
    try:
        numero = int(input("Por favor, digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

verificar_par_impar()
