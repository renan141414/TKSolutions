import json
import random


# Função para gerar um produto aleatório
def gerar_produto(id):
    categorias = ["Eletrônicos", "Móveis", "Roupas", "Livros", "Alimentos", "Brinquedos"]
    nomes = ["Produto", "Item", "Artigo", "Mercadoria", "Objeto"]

    return {
        "id": id,
        "nome": f"{random.choice(nomes)} {id}",
        "categoria": random.choice(categorias),
        "preco": round(random.uniform(10.0, 1000.0), 2),
        "quantidade": random.randint(1, 100),
        "avaliacao": round(random.uniform(1.0, 5.0), 1)
    }


# Gerar 50 produtos
produtos = [gerar_produto(i) for i in range(1, 51)]

# Criar o dicionário final
dados = {
    "produtos": produtos,
    "total_produtos": len(produtos),
    "data_geracao": "2023-05-15"  # Você pode alterar esta data conforme necessário
}

# Nome do arquivo JSON
nome_arquivo = "produtos_extenso.json"

# Escrever os dados no arquivo JSON
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

print(f"Arquivo '{nome_arquivo}' criado com sucesso contendo {len(produtos)} produtos.")

# Ler e exibir uma amostra dos dados para verificação
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)

print("\nAmostra dos primeiros 5 produtos:")
for produto in dados_lidos['produtos'][:5]:
    print(
        f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Categoria: {produto['categoria']}")

print(f"\nTotal de produtos no arquivo: {dados_lidos['total_produtos']}")