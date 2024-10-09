def calculadora_simples():
    try:
        # Solicita dois números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Solicita a operação
        print("\nEscolha a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        operacao = input("Digite o número da operação desejada (1/2/3/4): ")

        # Realiza a operação escolhida
        if operacao == '1':
            resultado = num1 + num2
            simbolo = '+'
        elif operacao == '2':
            resultado = num1 - num2
            simbolo = '-'
        elif operacao == '3':
            resultado = num1 * num2
            simbolo = '*'
        elif operacao == '4':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
            simbolo = '/'
        else:
            raise ValueError("Operação inválida.")

        # Exibe o resultado
        print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")

    except ValueError as e:
        if str(e) == "Operação inválida.":
            print("Erro: Operação inválida. Por favor, escolha uma operação válida (1, 2, 3 ou 4).")
        else:
            print("Erro: Por favor, insira números válidos.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")

# Executar o programa
calculadora_simples()