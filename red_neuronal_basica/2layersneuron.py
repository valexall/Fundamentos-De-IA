import random

# 1. Las 4 entradas en una sola lista
entradas = [
    random.randint(-10, 10),
    random.uniform(-10, 10),
    random.randint(-10, 10),
    random.uniform(-10, 10),
]


# Función de activación (Escalón / Step)
def funcion_activacion(z):
  return 1 if z >= 0 else 0


# UNA sola función que sirve para cualquier neurona de cualquier capa
def calcular_neurona(entradas_capa, pesos_neurona, sesgo_neurona):
  # Multiplica cada entrada por su peso y suma todo + el sesgo
  suma_ponderada = (
      sum(x * w for x, w in zip(entradas_capa, pesos_neurona)) + sesgo_neurona
  )
  return funcion_activacion(suma_ponderada)


# --- CAPA OCULTA (4 neuronas, cada una con 4 pesos y 1 sesgo propio) ---
pesos_oculta = [
    [random.uniform(-1, 1) for _ in range(4)] for _ in range(4)
]  # Matriz 4x4 (16 pesos)
sesgos_oculta = [random.uniform(-1, 1) for _ in range(4)]  # 4 sesgos

# Calculamos las 4 salidas de la capa oculta en una sola línea
salidas_oculta = [
    calcular_neurona(entradas, pesos_oculta[i], sesgos_oculta[i])
    for i in range(4)
]

# --- CAPA DE SALIDA (1 neurona que recibe las 4 salidas de la capa oculta) ---
pesos_salida = [random.uniform(-1, 1) for _ in range(4)]  # 4 pesos
sesgo_salida = random.uniform(-1, 1)  # 1 sesgo

prediccion_final = calcular_neurona(salidas_oculta, pesos_salida, sesgo_salida)

print("Entradas (4):", [round(x, 2) for x in entradas])
print("Salidas Capa Oculta (4):", salidas_oculta)
print("Predicción Final (1):", prediccion_final)
