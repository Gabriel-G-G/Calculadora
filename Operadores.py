# librerias
import math
import this

# Funciones de calculadora
def suma():
    this.res =  this.valor1 + this.valor2

def resta():
    this.res = this.valor1 - this.valor2

def multiplicar():
    this.res = this.valor1 * this.valor2

def dividir():
    this.res = this.valor1 / this.valor2

def raiz():
    this.res = math.sqrt(this.val1)

# Clase que contiene operadores suma, resta, multiplicación y divición
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

# clase que contiene 
class OprRaiz:
    valraiz = 0
    def raiz(val1):
        this.valraiz = val1
        this.res = math.sqrt(this.valraiz)
        retun = this.res
