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


def criar_banco_clientes(cliente, num_clientes=50):
    db = cliente['empresa']
    colecao_clientes = db['clientes']

    # Limpar coleção existente
    colecao_clientes.drop()

    # Dados de exemplo
    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Carla', 'Lucas', 'Julia', 'Marcos', 'Larissa', 'Gabriel']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Almeida', 'Pereira', 'Lima',
                  'Gomes']
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília', 'Curitiba', 'Porto Alegre',
               'Recife', 'Fortaleza', 'Manaus']

    clientes = []
    for _ in range(num_clientes):
        cliente = {
            'nome': f"{random.choice(nomes)} {random.choice(sobrenomes)}",
            'idade': random.randint(18, 70),
            'cidade': random.choice(cidades),
            'saldo': round(random.uniform(0, 10000), 2),
            'data_cadastro': (datetime.now() - timedelta(days=random.randint(0, 1825))).strftime("%Y-%m-%d")
        }
        clientes.append(cliente)

    colecao_clientes.insert_many(clientes)
    print(f"Banco de dados 'empresa' criado com {len(clientes)} clientes na coleção 'clientes'.")


def main():
    cliente_mongo = conectar_mongodb()
    if cliente_mongo:
        criar_banco_clientes(cliente_mongo, 50)
        cliente_mongo.close()


if __name__ == "__main__":
    main()