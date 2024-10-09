import csv
import os

# Nome do arquivo CSV
nome_arquivo = "pessoas.csv"


# Função para criar um arquivo CSV de exemplo, se não existir
def criar_arquivo_exemplo():
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            escritor.writerows([
                ['Ana Silva', '28', 'São Paulo'],
                ['Carlos Oliveira', '35', 'Rio de Janeiro'],
                ['Maria Santos', '42', 'Belo Horizonte'],
                ['João Pereira', '31', 'Porto Alegre'],
                ['Beatriz Lima', '39', 'Curitiba']
            ])
        print(f"Arquivo de exemplo '{nome_arquivo}' criado.")


# Função para ler o arquivo CSV
def ler_csv():
    pessoas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            pessoas.append(linha)
    return pessoas


# Função para exibir as pessoas
def exibir_pessoas(pessoas):
    for i, pessoa in enumerate(pessoas, 1):
        print(f"{i}. {pessoa['Nome']} - {pessoa['Idade']} anos - {pessoa.get('Cidade', 'N/A')}")


# Função para atualizar a idade
def atualizar_idade(pessoas):
    exibir_pessoas(pessoas)
    try:
        indice = int(input("\nDigite o número da pessoa que deseja atualizar: ")) - 1
        if 0 <= indice < len(pessoas):
            nova_idade = input(f"Digite a nova idade para {pessoas[indice]['Nome']}: ")
            pessoas[indice]['Idade'] = nova_idade
            print("Idade atualizada com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


# Função para salvar as alterações no arquivo CSV
def salvar_csv(pessoas):
    # Determinar todos os campos únicos presentes nos dados
    campos = set()
    for pessoa in pessoas:
        campos.update(pessoa.keys())
    campos = list(campos)

    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(pessoas)
    print(f"Alterações salvas no arquivo '{nome_arquivo}'.")


# Programa principal
def main():
    criar_arquivo_exemplo()

    while True:
        print("\n--- Gerenciador de Idades ---")
        print("1. Exibir pessoas")
        print("2. Atualizar idade")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            pessoas = ler_csv()
            exibir_pessoas(pessoas)
        elif escolha == '2':
            pessoas = ler_csv()
            atualizar_idade(pessoas)
            salvar_csv(pessoas)
        elif escolha == '3':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()