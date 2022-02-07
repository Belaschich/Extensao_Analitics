
class Calculadora:
    #TODO: documentacao
    
    def valida_numero(x):
        """Retorna True ou False representando se o valor passado é ou não um numero.

        Args:
            x (any): valor passado para teste.

        Returns:
            [boolean]: resultado do teste.
        """
        try:
            if isinstance(x, float):
                return True
            elif isinstance(x, int):
                return True
            else:
                return False
           
        except Exception as e:
            print(e)
    
    def pede_numero():
        try:
            num1 = float(input("Digite um numero:  "))
            while not(Calculadora.valida_numero(num1)):
                num1 = float(input("Digite um numero:  "))
            return num1
        except Exception as e:
            print(e)
            
   
    def soma(lista_numeros):
        try:
            resultado = 0
            for i in lista_numeros:
                resultado += i
            return resultado
        except Exception as e:
            print(e)

    def sub(lista_numeros):
        try:
            resultado = lista_numeros[0] - lista_numeros[1]

            return resultado
        except Exception as e:
            print(e)

    def mult(lista_numeros):
        try:
            resultado = 1
            for i in lista_numeros:
                resultado *= i
            return resultado
        except Exception as e:
            print(e)

    def div(lista_numeros):
        try:
            resultado = lista_numeros[0] / lista_numeros[1]
            return resultado
        except Exception as e:
            print(e)        
    
    def pot2(lista_numeros):
        try:
            resultado = lista_numeros[0] ** lista_numeros[1]
            return resultado
        except Exception as e:
            print(e)