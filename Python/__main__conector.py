from modules.connector import Interface_mysql

banco = Interface_mysql("admin", "admin", "localhost", "teste")
dados = banco.selecionar("SELECT * FROM funcionarios")
print(dados)