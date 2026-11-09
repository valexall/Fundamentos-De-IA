
import random



x1 = random.uniform(-1, 1)  # Genera un valor aleatorio entre -1 y 1

peso = random.uniform(-1, 1)  # Genera un peso aleatorio entre -1 y 1

sesgo = random.uniform(-1, 1)  # Genera un sesgo aleatorio entre -1 y 1


def SumaPonderada(x1, peso, sesgo):
      return (x1 * peso) + sesgo


def FuncionActivacion(z):
    if z >= 0:
        return 1
    else:
        return 0


z = SumaPonderada(x1, peso, sesgo)  # Calcula la suma ponderada

y = FuncionActivacion(z)  # Aplica la función de activación


print("Valor de entrada (x1):", x1)
print("Peso (w):", peso)
print("Sesgo (b):", sesgo)
print("Suma ponderada (z):", z)
print("Salida (y):", y)
