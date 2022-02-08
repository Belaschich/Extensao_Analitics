#class funcionarios:
#    id = 0
#    nome = "teste"
#    funcao = "Operador"

#    def set_nome (self, nome):
#        self.nome = nome
#
#    def get_nome (self):
#        return self.nome
         

class Funcionarios:

    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def print_teste():
        print("eu nao preciso de self")