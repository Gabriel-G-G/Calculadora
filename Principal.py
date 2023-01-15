# Archivos importados
from Operadores import *
user_input = ''
contador = 0
listacontador = []
while user_input.lower() != 'n':
    val1 = 0.0
    val2 = 0.0
    res = ''
    try:
        operacion = int(input('Ingresa un operador \n1 -> Suma \n2 -> Resta \n3 -> Multiplicación \n4 -> División \n'
                              '5 -> Potencias \n6 -> Exponentes \n7 -> Seno \n8 -> Coseno \n9 -> Tangente \n10 -> Salir \n==> '))
    except ValueError:
        print('Operación no valida')
        finalizar = input('¿Desea realizar otra operacion? == s o == n ')
    else:
        if not int(operacion):
            print('Operación no valida')
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
        elif operacion == 10:
            finalizar = 'n'
        elif operacion < 1 or operacion > 9:
            print('Operación no valida')
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
        elif operacion >= 1 and operacion <= 4:
            val1 = float(input('Ingresa primer valor: '))
            val2 = float(input('Ingresa segundo valor: '))
            res = Calculadora.opr(operacion, val1, val2)
            print('El resultado es: ' + res)
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
        elif operacion == 5 :
            val1 = float(input('Ingresa un valor: '))
            val2 = float(input('Ingresa un valor para la potencia: '))
            res = OprRaiz.raiz(val1, val2)
            print('El resultado es: ' + res)
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
        elif operacion == 6:
            val1 = float(input('Ingresa primer valor: '))
            val2 = float(input('Ingresa segundo valor: '))
            res = OprExponente.exponentes(val1,val2)
            print('El resultado es: ' + res)
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
        elif operacion >= 7 and operacion <= 9:
            val1 = float(input('Ingresa los grados: '))
            res = OprTrigonometria.trigonometria(operacion, val1)
            print(res)
            finalizar = input('¿Desea realizar otra operacion? == s o == n ')
    if finalizar == 'n':
        user_input = finalizar
    else:
        contador += 1
        listacontador.append(str(contador))
        for number in listacontador:
            print('Número de operacion realizada: ' + number)
