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


# Una sola función que sirve para cualquier neurona de cualquier capa
def calcular_neurona(entradas_capa, pesos_neurona, sesgo_neurona):
    suma_ponderada = (
        sum(x * w for x, w in zip(entradas_capa, pesos_neurona))
        + sesgo_neurona
    )
    return funcion_activacion(suma_ponderada)


# --- PRIMERA CAPA OCULTA (4 neuronas, cada una con 4 pesos) ---
pesos_oculta_1 = [
    [random.uniform(-1, 1) for _ in range(4)] for _ in range(4)
]
sesgos_oculta_1 = [random.uniform(-1, 1) for _ in range(4)]

salidas_oculta_1 = [
    calcular_neurona(entradas, pesos_oculta_1[i], sesgos_oculta_1[i])
    for i in range(4)
]


# --- SEGUNDA CAPA OCULTA (3 neuronas, cada una con 4 pesos) ---
pesos_oculta_2 = [
    [random.uniform(-1, 1) for _ in range(4)] for _ in range(3)
]
sesgos_oculta_2 = [random.uniform(-1, 1) for _ in range(3)]

salidas_oculta_2 = [
    calcular_neurona(salidas_oculta_1, pesos_oculta_2[i], sesgos_oculta_2[i])
    for i in range(3)
]


# --- CAPA DE SALIDA (1 neurona que recibe la segunda capa oculta) ---
pesos_salida = [random.uniform(-1, 1) for _ in range(3)]
sesgo_salida = random.uniform(-1, 1)

prediccion_final = calcular_neurona(
    salidas_oculta_2,
    pesos_salida,
    sesgo_salida,
)

print("Entradas (4):", [round(x, 2) for x in entradas])
print("Salidas Primera Capa Oculta (4):", salidas_oculta_1)
print("Salidas Segunda Capa Oculta (3):", salidas_oculta_2)
print("Predicción Final (1):", prediccion_final)
