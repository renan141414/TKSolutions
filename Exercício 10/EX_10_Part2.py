from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


def conectar_mongodb():
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        cliente.admin.command('ismaster')  # Verifica a conectividade com o servidor
        print("Conexão bem-sucedida ao MongoDB!")
        return cliente
    except ConnectionFailure:
        print("Erro: Não foi possível conectar ao MongoDB. Verifique se o servidor está rodando.")
        return None


def consultar_clientes_acima_de_30(cliente):
    try:
        db = cliente['empresa']
        colecao_clientes = db['clientes']

        # Consulta filtrada para clientes acima de 30 anos, retornando apenas os campos necessários
        query = {"idade": {"$gt": 30}}
        projection = {"_id": 0, "nome": 1, "idade": 1, "cidade": 1, "saldo": 1, "data_cadastro": 1}
        clientes_filtrados = colecao_clientes.find(query, projection)

        total_clientes = colecao_clientes.count_documents(query)

        if total_clientes == 0:
            print("Nenhum cliente com mais de 30 anos foi encontrado.")
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
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        cliente.close()
        print("Conexão com MongoDB encerrada.")


def main():
    cliente_mongo = conectar_mongodb()
    if cliente_mongo:
        consultar_clientes_acima_de_30(cliente_mongo)


if __name__ == "__main__":
    main()
