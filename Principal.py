# Librerias
import numpy as np
# Archivos importados
from Operadores import Calculadora
user_input = ''
contador = 0
listacontador = []
while user_input.lower() != 'n':
    operacion = int(input('Ingresa el operador: '))
    if operacion < 1 or operacion > 9:
        print('Operación no valida')
        finalizar = input('¿Desea realizar otra operacion? == s o == n ')
    elif operacion > 1 and operacion <= 4:
        val1 = int(input('Ingresa primer valor: '))
        val2 = int(input('Ingresa segundo valor: '))
        res = Calculadora.opr(operacion, val1, val2)
        print('El resultado es: ' + str(res))
        finalizar = input('¿Desea realizar otra operacion? == s o == n ')
    elif operacion == 5 or operacion == 6:
        val1 = int(input('Ingresa un valor: '))
        res = Calculadora.OprRaiz(val1)
        print('El resultado es: ' + str(res))
        finalizar = input('¿Desea realizar otra operacion? == s o == n ')

    if finalizar == 'n':
        user_input = finalizar
    else:
        contador += 1
        listacontador.append(str(contador))
        for number in listacontador:
            print('Número de operacion realizada: ' + number)