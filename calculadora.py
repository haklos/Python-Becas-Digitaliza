import time

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("\n RECORDATORIO: Usted no debe utilizar la división, ya que no se puede dividir entre 0\n")
        time.sleep(2)
        return "Le he dicho que no marque división. FIN"

def potencia(a,b):
    return a**b




print("Bienvenido a calculadora.py, el programa más usado por 9 de cada 10 matématicos en España. Disfrute su ejecución.")
time.sleep(2)
valido = False
while valido == False:
    try:
        var1 = float(input("Introduce el primer número: "))
        var2 = float(input("Introduce el segundo número: "))
        valido = True
    except ValueError:
        print("Elemento no válido. Introduzca un número por favor.")
    except Exception:
        print("Error no esperado, vuelva a introducir los números. Disculpe las molestias")

operaciones={"suma": sumar(var1,var2), "resta": restar(var1,var2), "multiplicacion": multiplicar(var1,var2), "division": dividir(var1,var2),
             "exponente" : potencia(var1,var2)}
#Se que implementar un diccionario en esta posición no es muy útil, pero no se me ocurre otra forma de usar un diccionario en una calculadora.

valido = False
while valido==False:
    op = input("Por último, introduzca la operación que desea realizar entre las siguientes opciones(minúsculas):\n-Suma\n-Resta\n-Multiplicacion\n"
                   "-Division\n-Exponente\n")

    if op in operaciones:
        valido = True
    else:
        print("No intente tomarme el pelo, eso no es una operación válida.")

print("El resultado es: ",operaciones.get(op))