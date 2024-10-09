import json

def ler_json_para_dicionario(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

# Nome do arquivo JSON
nome_arquivo = "produtos_extenso.json"

# Lendo o arquivo JSON e convertendo para um dicionário Python
dados_produtos = ler_json_para_dicionario(nome_arquivo)

if dados_produtos:
    print("Conteúdo do dicionário Python:")
    print(json.dumps(dados_produtos, indent=2, ensure_ascii=False))

    print("\nAcessando informações específicas:")
    for produto in dados_produtos['produtos']:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

    # Exemplo de como você pode trabalhar com os dados
    total_produtos = sum(produto['quantidade'] for produto in dados_produtos['produtos'])
    print(f"\nTotal de produtos em estoque: {total_produtos}")
