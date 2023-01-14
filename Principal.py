from Operadores import Calculadora
user_input = ''
contador = 0
listacontador = []
while user_input.lower() != 'n':
    val1 = int(input('Ingresa primer valor: '))
    val2 = int(input('Ingresa segundo valor: '))
    operacion = int(input('Ingresa el operador: '))
    res = Calculadora.opr(operacion, val1, val2)
    print('El resultado es: ' + str(res))
    finalizar = input('¿Desea realizar otra operacion? == s o == n ')
    if finalizar == 'n':
        user_input = finalizar
    else:
        contador += 1
        listacontador.append(str(contador))
        for number in listacontador:
            print('Número de operacion realizada: ' + number)