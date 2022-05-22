
def numero_primo(numero:int):

    if numero>0:
        for n in range(2,numero):
            if numero % n == 0:
                return False
        return True

    else:
        return False

def comprobar():
    numero = int(input("Introduce un numero: "))
    resultado = numero_primo(numero)
    if resultado==True:
        print("El numero es primo")
    else:
        print("El numero no es primo")

comprobar()