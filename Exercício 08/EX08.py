from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import random
from datetime import datetime, timedelta


def conectar_mongodb():
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        cliente.admin.command('ismaster')
        print("Conexão bem-sucedida ao MongoDB!")
        return cliente
    except ConnectionFailure:
        print("Falha ao conectar ao MongoDB. Verifique se o servidor está rodando.")
        return None


def criar_banco_alunos(cliente):
    db = cliente['escola']
    colecao_alunos = db['alunos']

    # Limpar coleção existente
    colecao_alunos.drop()

    # Dados de exemplo
    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Carla', 'Lucas', 'Julia', 'Marcos', 'Larissa', 'Gabriel']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Almeida', 'Pereira', 'Lima',
                  'Gomes']
    cursos = ['Engenharia', 'Medicina', 'Direito', 'Administração', 'Psicologia', 'Ciência da Computação',
              'Arquitetura']

    alunos = []
    for _ in range(20):
        aluno = {
            'nome': f"{random.choice(nomes)} {random.choice(sobrenomes)}",
            'idade': random.randint(18, 30),
            'curso': random.choice(cursos),
            'nota': round(random.uniform(5.0, 10.0), 1),
            'data_inscricao': (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        }
        alunos.append(aluno)

    colecao_alunos.insert_many(alunos)
    print(f"Banco de dados 'escola' criado com {len(alunos)} alunos na coleção 'alunos'.")


def consultar_alunos(cliente):
    try:
        db = cliente['escola']
        colecao_alunos = db['alunos']

        total_alunos = colecao_alunos.count_documents({})
        if total_alunos == 0:
            print("A coleção 'alunos' está vazia.")
            return

        print(f"\nExibindo {total_alunos} alunos da coleção 'alunos':")
        for aluno in colecao_alunos.find():
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Nota: {aluno['nota']}")
            print(f"Data de Inscrição: {aluno['data_inscricao']}")
            print("-" * 30)

    except OperationFailure as e:
        print(f"Erro ao consultar a coleção: {e}")


def main():
    cliente = conectar_mongodb()
    if cliente:
        criar_banco_alunos(cliente)
        consultar_alunos(cliente)
        cliente.close()


if __name__ == "__main__":
    main()
