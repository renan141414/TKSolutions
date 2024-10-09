def classificar_nota():
    try:
        # Solicita a nota ao usuário
        nota = float(input("Por favor, digite a nota (de 0 a 100): "))

        # Verifica se a nota está no intervalo válido
        if not 0 <= nota <= 100:
            print("Erro: A nota deve estar entre 0 e 100.")
            return

        # Classifica a nota usando um dicionário
        if nota >= 90:
            classificacao = "A"
        elif nota >= 80:
            classificacao = "B"
        elif nota >= 70:
            classificacao = "C"
        elif nota >= 60:
            classificacao = "D"
        else:
            classificacao = "F"

        # Exibe o resultado
        print(f"Nota: {nota:.1f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Por favor, digite um número válido para a nota.")

# Executar o programa
classificar_nota()
