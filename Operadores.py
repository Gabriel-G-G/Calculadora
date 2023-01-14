import this
import numpy

def suma():
    this.res = this.valor1 + this.valor2

def resta():
    this.res = this.valor1 - this.valor2

def multiplicar():
    this.res = this.valor1 * this.valor2

def dividir():
    this.res = this.valor1 / this.valor2

class Calculadora:
    res = 0
    valor1 = 0
    valor2 = 0

    def opr(opcion, val1, val2):
        this.valor1 = val1
        this.valor2 = val2
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        return this.res


