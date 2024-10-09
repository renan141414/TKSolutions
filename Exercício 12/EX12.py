def encontrar_maior_numero():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))

        if num1 >= num2 and num1 >= num3:
            maior = num1
        elif num2 >= num1 and num2 >= num3:
            maior = num2
        else:
            maior = num3

        print(f"\nO maior número entre {num1}, {num2} e {num3} é: {maior}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

encontrar_maior_numero()
