from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def conectar_mongodb():
    try:
        # Conectar ao MongoDB local na porta padrão 27017
        cliente = MongoClient('mongodb://localhost:27017/')

        # Verificar a conexão
        cliente.admin.command('ping')

        print("Conexão bem-sucedida ao MongoDB!")
        return cliente
    except ConnectionFailure:
        print("Falha ao conectar ao MongoDB. Verifique se o servidor está rodando.")
        return None

def listar_bancos_de_dados(cliente):
    if cliente is not None:
        dbs = cliente.list_database_names()
        if dbs:
            print("\nBancos de dados disponíveis:")
            for db in dbs:
                print(f"- {db}")
        else:
            print("\nNão há bancos de dados disponíveis.")
    else:
        print("Não foi possível listar os bancos de dados devido à falha na conexão.")

def main():
    cliente = conectar_mongodb()
    if cliente:
        listar_bancos_de_dados(cliente)
        cliente.close()  # Fechar a conexão

if __name__ == "__main__":
    main()
