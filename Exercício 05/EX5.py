import json

# Criando um dicionário com dados de cinco alunos
alunos = {
    "alunos": [
        {"nome": "Maria Silva", "nota": 8.5},
        {"nome": "João Santos", "nota": 7.8},
        {"nome": "Ana Oliveira", "nota": 9.2},
        {"nome": "Pedro Souza", "nota": 6.9},
        {"nome": "Carla Ferreira", "nota": 8.7}
    ]
}

# Nome do arquivo JSON
nome_arquivo = "alunos.json"

# Escrevendo os dados no arquivo JSON
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=2)
    print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")

except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")

# Lendo e exibindo o conteúdo do arquivo JSON para verificação
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)

    print("\nConteúdo do arquivo JSON:")
    print(json.dumps(dados_lidos, ensure_ascii=False, indent=2))

    print("\nDados dos alunos:")
    for aluno in dados_lidos['alunos']:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")