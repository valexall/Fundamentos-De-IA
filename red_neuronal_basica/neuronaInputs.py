
import random
import pandas as pd

dataset = pd.read_csv("data/datos_estudiantes.csv")

x1 = dataset["horas_estudio"].values
x2 = dataset["asistencia"].values

peso1 = random.uniform(-1,1)
peso2 = random.uniform(-1,1)
sesgo = random.uniform(-1,1)


def SumaPonderada(x1, x2, peso1, peso2, sesgo):
      return ((x1 * peso1) + (x2 * peso2)) + sesgo


def FuncionActivacion(z):
    if z >= 0:
        return 1
    else:
        return 0

z = SumaPonderada(x1, x2, peso1, peso2, sesgo)
y = FuncionActivacion(z)

print("x1:", x1)
print("x2:", x2)
print("peso1:", peso1)
print("peso2:", peso2)
print("sesgo:", sesgo)
print("Suma Ponderada:", z)
print("Salida de la función de activación:", y)
