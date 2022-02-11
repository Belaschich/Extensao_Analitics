import datetime
from math import prod
#import logging
from modules.connector1 import Interface_mysql
from modules.produto import Produto

if __name__ == "__main__":
    try:

        banco = Interface_mysql("root", "admin", "localhost", "app3")
        while True:
            escolha = input("1-Cadastrar 2-alterar 3-excluir 4-listar 0-sair :")
            if int(escolha) == 1:
                
                id = int(input("digite a id do produto: "))
                descricao = input("Digite a descricao do produto: ")
                preco = float(input("Digite o preço do produto: "))
                produto = Produto(id, descricao, preco)
                produto.inserir(banco);
            
            elif int(escolha) == 2:
                
                id = int(input("Digite a id do produto a ser alterado: "))
                descricao = input("Digite a nova descricao do produto: ")
                preco = float(input("Digite o novo preço do produto: "))
                query = "UPDATE produtos SET descricao='" + str(descricao) + "', preco=" + str(preco)+ " WHERE id =" + str(id) +";"
                banco.atualizar(query)
                
            elif int(escolha) == 3:
                id = int(input("Digite a id do produto a ser excluido: "))
                query = "DELETE FROM produtos WHERE id =" + str(id) +";"
                banco.excluir(query)
                
            elif int(escolha) == 4:
                
                prods = banco.selecionar("SELECT * FROM produtos;")
                produtos = []
                if prods == []:
                    print("Nenhum registro encontrado!")
                else:
                    for p in prods:
                        pr = Produto(p[0], p[1], p[2])
                        produtos.append(pr)
                    for p in produtos:
                        p.printar()
                        
            elif int(escolha) == 0:
                print("Saindo!")
                break
            else:            
                print("Algo errado não está certo?")
            
    except Exception as e:
        print(str(datetime.datetime.now()) + " ERRO: app3: main: " + str(e))