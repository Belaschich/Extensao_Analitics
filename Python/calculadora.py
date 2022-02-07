'''Fazer uma calculadora simples, mas de forma mais profissional possivel'''

n1 = float(input('Primeiro valor: ')) 
n2 = float(input('Segundo avalor: '))
op = input('Digite a operação a ser usada: soma (+), subtração(-), multiplicação(*) ou divisão(/): ')


ad = (n1+n2) #Soma dos números digitados
sub = (n1-n2) #Subtração dos números digitados
mul = (n1*n2) #Multiplicação dos números digitados
div = (n1/n2) #Dibisão dos números digitados

#Estrutura de repetição caso o valor da operação digitado não seja um dos pedidos
while op != '+' and op != '-' and op != '*' and op != '/':
    print('Valor inválido, tente novamente')
    op = input('Digite a operação a ser usada: soma, subtração, multiplicação ou divisão: ')

#Estrutura de IF, Elif para facilitar o resultado final
if op == '+':
    print('Resultado de {} + {} = {}'.format(n1, n2, ad))
elif op == '-':
    print('Resultado de {} - {} = {}'.format(n1, n2,sub))
elif op == '*':
    print('Resultado de {} * {} = {}'.format(n1, n2,mul))
elif op == '/':
    print('Resultado de {} / {} = {}'.format(n1, n2,div))


