import random

entradas = [-1,-2,-3, 1, 2, 3]
salida = [0, 0, 0, 1, 1, 1]


pesoActual = 0
sesgo = 0
tasaDeAprendizaje = 0.1


def SumaPonderada(entradas, peso, sesgo):
      return (entradas * peso) + sesgo


def FuncionActivacion(z):
    if z >= 0:
        return 1
    else:
        return 0

def funcionPerdida(salida_esperada, salida_obtenida):
    return (salida_esperada - salida_obtenida) ** 2



def pesoNuevo(pesoActual, tasaDeAprendizaje, salida, entrada, prediccion):

    return pesoActual + (tasaDeAprendizaje * (salida - prediccion) * entrada)

def sesgoNuevo(sesgoActual, tasaDeAprendizaje, salida, prediccion):
    return sesgoActual + (tasaDeAprendizaje * (salida - prediccion))



for epoca in range(2):
    perdidaTotal = 0
    for entrada, real in zip(entradas, salida):
        z = SumaPonderada(entrada, pesoActual, sesgo)
        salida_obtenida = FuncionActivacion(z)
        perdida = funcionPerdida(real, salida_obtenida)
        print(f"Entrada: {entrada}, Salida obtenida: {salida_obtenida}, Salida esperada: {real}, Pérdida: {perdida}")
        pesoActual = pesoNuevo(pesoActual, tasaDeAprendizaje, real, entrada, salida_obtenida)
        sesgo = sesgoNuevo(sesgo, tasaDeAprendizaje, real, salida_obtenida)
        print(f"Peso actualizado: {pesoActual}, Sesgo actualizado: {sesgo}\n")
        perdidaTotal += perdida

    print(f"Epoca {epoca + 1}: Pérdida total: {perdidaTotal}\n")

print(f"Peso final: {pesoActual}, Sesgo final: {sesgo}")



def predecir(entrada):
    z = SumaPonderada(entrada, pesoActual, sesgo)
    return FuncionActivacion(z)

predecir(-100)
