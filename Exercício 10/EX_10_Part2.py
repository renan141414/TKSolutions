from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


def conectar_mongodb():
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        cliente.admin.command('ismaster')
        print("Conexão bem-sucedida ao MongoDB!")
        return cliente
    except ConnectionFailure:
        print("Falha ao conectar ao MongoDB. Verifique se o servidor está rodando.")
        return None


def consultar_clientes_acima_de_30(cliente):
    try:
        db = cliente['empresa']
        colecao_clientes = db['clientes']

        # Consulta filtrada
        query = {"idade": {"$gt": 30}}
        clientes_filtrados = colecao_clientes.find(query)

        total_clientes = colecao_clientes.count_documents(query)

        if total_clientes == 0:
            print("Não foram encontrados clientes com mais de 30 anos.")
        else:
            print(f"\nClientes com mais de 30 anos (Total: {total_clientes}):")
            for cliente in clientes_filtrados:
                print(f"Nome: {cliente['nome']}")
                print(f"Idade: {cliente['idade']}")
                print(f"Cidade: {cliente['cidade']}")
                print(f"Saldo: R${cliente['saldo']:.2f}")
                print(f"Data de Cadastro: {cliente['data_cadastro']}")
                print("-" * 30)

    except OperationFailure as e:
        print(f"Erro ao consultar a coleção: {e}")


def main():
    cliente_mongo = conectar_mongodb()
    if cliente_mongo:
        consultar_clientes_acima_de_30(cliente_mongo)
        cliente_mongo.close()


if __name__ == "__main__":
    main()