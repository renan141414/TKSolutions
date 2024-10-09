def classificar_idade():
    try:
        # Solicita a idade ao usuário
        idade = int(input("Por favor, digite sua idade: "))

        # Classifica a faixa etária usando if, elif e else
        if idade < 0:
            print("Idade inválida. Por favor, insira um número positivo.")
        elif idade < 12:
            print("Classificação: Criança")
        elif idade < 18:
            print("Classificação: Adolescente")
        elif idade < 65:
            print("Classificação: Adulto")
        else:
            print("Classificação: Idoso")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para a idade.")

# Executar o programa
classificar_idade()