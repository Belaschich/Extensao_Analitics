def funcao_exemplo(y) -> None: # -> <tipo> indica o tipo de retorno da funcao
    # comentarios ficam entre bloco """ """
    """Funcao para exemplo dos blocos try, except e finally

    Args:
        y (int): valor interiro a ser usado em divisao, dividendo.
    """
    try:
      x = y/0
    except Exception as e:
      print(e)
    finally:
      print("encerrando execucao")
      
    
if __name__ == "__main__":
 try:
  y = 10
  funcao_exemplo(y)

 except Exception as e:
      print(e)
 