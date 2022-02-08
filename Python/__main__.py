from Funcionarios.modules.funcionarios import Funcionarios
from Produtos.modules.produtos import Produtos
func = [Funcionarios(0, "maria", "vendedor"), Funcionarios(1, "joao", "vendedor"), Funcionarios(2, "Ricardo", "gerente")]
prod = [Produtos(0, "arroz", 1.5), Produtos(1, "feijao", 5.6), Produtos(2, "macarrao", 0.6), Produtos(3, "leite", 5.0)]
#venda = funcionario, [[produto, quantidade], ...]
#venda = [2, [[0, 5], [1, 3], [3, 12]]]
#vd = venda[funcioário,[produto, quantidade],...]
venda = [[0, [[0, 5], [1, 3], [2, 7]]], [1, [[0, 5], [1, 3], [2, 7]]]]

#total = 0
#for v in vd[1]:
#    for p in prod:
#        if v[0] == p.id:
#            total += v[1] * p.preco
#print("O total de vendas foi R${}".format(total))

for cada in venda:
 total = 0
 for v in cada[1]:
    for p in prod:
        if v[0] == p.id:
            total += v[1] * p.preco
 print("total da venda: ", total)

 for f in func:
    if cada[0] == f.id:
        print("funcionario responsavel pela venda: ", f.nome)