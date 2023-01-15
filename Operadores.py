# librerias
import numpy as np
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
    this.resRaiz = this.val1raiz ** this.val2raiz

def exponente():
    this.resExp = np.power(this.val1Exp, this.val2Exp)

# Clase que contiene operadores suma, resta, multiplicación y divición
class Calculadora:
    res = 0.0
    valor1 = 0.0
    valor2 = 0.0

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
        return str(this.res)

# clase que contiene operacion de la raiz
class OprRaiz:
    val1raiz = 0.0
    val2raiz = 0.0
    resRaiz = 0.0
    def raiz(val1, val2):
        this.val1raiz = val1
        this.val2raiz = val2
        raiz()
        return str(this.resRaiz)

class OprExponente:
    val1Exp = 0.0
    val2Exp = 0.0
    resExp = 0.0
    def exponentes(val1, val2):
        this.val1Exp = val1
        this.val2Exp = val2
        exponente()
        return str(this.resExp)

