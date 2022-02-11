import datetime

class Produto:
    def __init__(self, id, descricao, preco):
        try:
            self.id = id
            self.descricao = descricao
            self.preco = preco
            
        except Exception as e:
            print(str(datetime.datetime.now()) + " ERRO: app3: produto: construtor: " + str(e))
    
    def set_id(self, id):
        self.id = id
        
    def get_id(self):
        return self.id
    
    def get_descricao(self):
        return self.descricao
    
    def get_preco(self):
        return self.preco
    
    def inserir(self, banco):
        try:        
            banco.inserir("INSERT INTO produtos (id, descricao, preco) VALUES ({}, '{}', {});".format(self.get_id(),self.get_descricao(),self.get_preco()))            
        except Exception as e:
            print(str(datetime.datetime.now()) + " ERRO: app3: produto: inserir: " + str(e))
            
    def printar(self):
        try:        
            print("Produto de id: ",self.get_id(), " desc: ", self.get_descricao()," preço: ",self.get_preco())
        except Exception as e:
            print(str(datetime.datetime.now()) + " ERRO: app3: produto: printar: " + str(e))