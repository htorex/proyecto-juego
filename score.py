

def archivo():

    try:
        with open("score.txt", "r+", encoding= "utf-8") as file:
            resultado = file.read()
            


    except Exception as e:
        
        resultado = 0
        


    finally:

        return resultado

def escribir(resultado):

    with open("score.txt", "w+", encoding= "utf-8") as file:
            file.write(str(resultado))
            
            