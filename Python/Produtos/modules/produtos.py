#class produtos:
#    id = 0
#    produto = "teste"
    
#    def set_produto (self, produto):
#        self.produto = produto

#    def get_produto (self):
#        return self.produto


class Produtos:
    
    def __init__(self, id, descricao, preco):
        try:
            self.id = id
            self.descricao = descricao
            self.preco = preco
        except Exception as e:
            print(str(e))