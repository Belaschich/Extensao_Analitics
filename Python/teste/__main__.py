from modules.mysql import Interface_mysql
from modules.mongo import Interface_mongo

def print_dados_bancos(banco_mysql, banco_mongo):
    print("Dados MySQL: ")
    print(banco_mysql.selecionar("SELECT * FROM funcionarios;"))
    print("Dados MongoDB: ")
    print(banco_mongo.buscar())
if __name__ == "__main__":
    try:
        banco_mysql = Interface_mysql("root","admin","localhost","teste")
        banco_mongo = Interface_mongo()
        print_dados_bancos(banco_mysql, banco_mongo)
        banco_mysql.inserir("INSERT INTO funcionarios(id, nome) VALUES(0,'Maria');")
        banco_mongo.inserir_um({"id":0,"nome":"Maria"})
        print_dados_bancos(banco_mysql, banco_mongo)
        banco_mysql.excluir("DELETE FROM funcionarios;")
        banco_mongo.excluir_varios({})
        
    except Exception as e:
        print(str(e))