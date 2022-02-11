from modules.connector2 import Interface_mysql

if __name__ == "__main__":
    try:

        banco = Interface_mysql("root", "0000", "localhost", "teste")
        #dados = banco.selecionar("SELECT * FROM funcionarios")
        print(banco.selecionar_funcionarios())
        banco.inserir("insert into funcionarios (id, nome) values (3, 'Ricardo');")
        print(banco.selecionar_funcionarios())

    except Exception as e:
        print(str(e))