import csv


def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)

            print("Conteúdo do arquivo CSV:")
            for linha in leitor_csv:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")

            # Voltando ao início do arquivo para calcular a média de idade
            arquivo.seek(0)
            next(leitor_csv)  # Pula o cabeçalho

            total_idade = 0
            numero_pessoas = 0

            for linha in leitor_csv:
                total_idade += int(linha['Idade'])
                numero_pessoas += 1

            if numero_pessoas > 0:
                media_idade = total_idade / numero_pessoas
                print(f"\nMédia de idade: {media_idade:.2f} anos")
            else:
                print("\nNão há dados de idade no arquivo.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except csv.Error as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# Chamada da função
ler_arquivo_csv('pessoas.csv')

# Testes usando pytest
def test_arquivo_csv_existente(tmp_path):
    # Criando um arquivo CSV temporário para teste
    arquivo_csv = tmp_path / "pessoas.csv"
    arquivo_csv.write_text("""Nome,Idade,Cidade
João,25,São Paulo
Maria,30,Rio de Janeiro
Pedro,20,Brasília
""", encoding='utf-8')

    # Verificando se a função executa sem erros
    try:
        ler_arquivo_csv(arquivo_csv)
    except Exception as e:
        assert False, f"Erro inesperado ao ler o arquivo CSV: {e}"

def test_arquivo_csv_inexistente():
    nome_arquivo = 'arquivo_inexistente.csv'
    try:
        ler_arquivo_csv(nome_arquivo)
    except FileNotFoundError:
        assert True
    except Exception as e:
        assert False, f"Erro inesperado ao lidar com um arquivo inexistente: {e}"

# Para rodar os testes com pytest, salve este código em um arquivo chamado test_csv.py e execute:
# pytest test_csv.py
