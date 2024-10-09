def excluir_aluno(cliente):
    try:
        db = cliente['escola']
        colecao_alunos = db['alunos']

        nome_aluno = input("Digite o nome completo do aluno que deseja excluir: ")
        aluno = colecao_alunos.find_one({'nome': nome_aluno})

        if aluno:
            confirmacao = input(f"Tem certeza que deseja excluir o aluno {nome_aluno}? (s/n): ")
            if confirmacao.lower() == 's':
                resultado = colecao_alunos.delete_one({'nome': nome_aluno})
                if resultado.deleted_count > 0:
                    print(f"Aluno {nome_aluno} foi excluído com sucesso.")
                else:
                    print("Erro ao excluir o aluno.")
            else:
                print("Exclusão cancelada.")
        else:
            print(f"Aluno {nome_aluno} não encontrado na base de dados.")

    except OperationFailure as e:
        print(f"Erro ao excluir o aluno: {e}")

def main():
    cliente = conectar_mongodb()
    if cliente:
        criar_banco_alunos(cliente)
        while True:
            print("\n--- Menu ---")
            print("1. Consultar todos os alunos\n2. Excluir um aluno\n3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                consultar_alunos(cliente)
            elif escolha == '2':
                excluir_aluno(cliente)
            elif escolha == '3':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        cliente.close()

if __name__ == "__main__":
    main()

