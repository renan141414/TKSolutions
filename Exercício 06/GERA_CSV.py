import csv

# Dados das pessoas
pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana Silva", "28", "São Paulo"],
    ["Carlos Oliveira", "35", "Rio de Janeiro"],
    ["Maria Santos", "42", "Belo Horizonte"],
    ["João Pereira", "31", "Porto Alegre"],
    ["Beatriz Lima", "39", "Curitiba"]
]

# Nome do arquivo CSV
nome_arquivo = "pessoas.csv"

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(pessoas)

print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")

# Lendo e exibindo o conteúdo do arquivo CSV
print("\nConteúdo do arquivo CSV:")
with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")