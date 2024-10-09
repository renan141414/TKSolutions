def classificar_idade():
    try:
        idade = int(input("Por favor, digite sua idade: "))
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

classificar_idade()
