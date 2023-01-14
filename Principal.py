from Operadores import Calculadora
val1 = int(input('Ingresa primer valor: '))
val2 = int(input('Ingresa segundo valor: '))
operacion = int(input('Ingresa el operador: '))
res = Calculadora.opr(operacion, val1, val2)

if res != None:
    print('El resultado es: ' + str(res))