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