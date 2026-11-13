
import pandas as pd
import numpy as np

# Cargar los datos
entradas = pd.read_csv('data/datos_estudiantes.csv')

x1 = entradas['horas_estudio'].values.astype(float)
x2 = entradas['asistencia'].values.astype(float)
salida = entradas['resultado'].values.astype(int)

# Normalizar los datos
max_x1 = max(np.max(np.abs(x1)), 1)
max_x2 = max(np.max(np.abs(x2)), 1)

x1 = x1 / max_x1
x2 = x2 / max_x2


# Calcular la suma ponderada
def SumaPonderada(x1, x2, peso1, peso2, sesgo):
    return ((x1 * peso1) + (x2 * peso2)) + sesgo


# Funcion de activacion sigmoide
def FuncionSigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


# Calcular el error cuadratico
def funcionPerdida(salida_esperada, salida_obtenida):
    return (salida_esperada - salida_obtenida) ** 2


# Actualizar el peso
def pesoNuevo(pesoActual, tasaDeAprendizaje, salida, entrada, prediccion):
    error = salida - prediccion
    derivada = prediccion * (1 - prediccion)

    return pesoActual + (tasaDeAprendizaje * 2 * error * derivada * entrada)


# Actualizar el sesgo
def sesgoNuevo(sesgoActual, tasaDeAprendizaje, salida, prediccion):
    error = salida - prediccion
    derivada = prediccion * (1 - prediccion)

    return sesgoActual + (tasaDeAprendizaje * 2 * error * derivada)


# Realizar una prediccion
def predecir(x1, x2, peso1, peso2, sesgo):
    z = SumaPonderada(x1, x2, peso1, peso2, sesgo)
    return FuncionSigmoid(z)


# Inicializar los parametros
peso1 = 0.0
peso2 = 0.0
sesgo = 0.0

tasaDeAprendizaje = 0.01
epocas = 1000

# Entrenar la neurona
for epoca in range(epocas):

    errorTotal = 0

    for i in range(len(salida)):

        # Realizar la prediccion
        prediccion = predecir(x1[i], x2[i], peso1, peso2, sesgo)

        # Calcular el error
        error = funcionPerdida(salida[i], prediccion)
        errorTotal += error

        # Actualizar los pesos
        nuevoPeso1 = pesoNuevo(
            peso1, tasaDeAprendizaje, salida[i], x1[i], prediccion
        )

        nuevoPeso2 = pesoNuevo(
            peso2, tasaDeAprendizaje, salida[i], x2[i], prediccion
        )

        # Actualizar el sesgo
        nuevoSesgo = sesgoNuevo(
            sesgo, tasaDeAprendizaje, salida[i], prediccion
        )

        peso1 = nuevoPeso1
        peso2 = nuevoPeso2
        sesgo = nuevoSesgo

    # Mostrar el error cada 100 epocas
    if epoca % 100 == 0:
        print(f"Epoca {epoca} - Error: {errorTotal / len(salida):.4f}")


# Mostrar los parametros entrenados
print("\n--- PARAMETROS FINALES ---")
print("Peso 1:", peso1)
print("Peso 2:", peso2)
print("Sesgo:", sesgo)


# Evaluar la neurona
predicciones = predecir(x1, x2, peso1, peso2, sesgo)
clasificaciones = (predicciones >= 0.5).astype(int)

exactitud = np.mean(clasificaciones == salida)

print("\n--- EVALUACION ---")
print(f"Exactitud de entrenamiento: {exactitud * 100:.2f}%")
print("Aprobados reales:", np.sum(salida == 1))
print("Desaprobados reales:", np.sum(salida == 0))
print("Aprobados predichos:", np.sum(clasificaciones == 1))
print("Desaprobados predichos:", np.sum(clasificaciones == 0))


# Probar con un estudiante nuevo
horas_estudio = 5
asistencia = 80

# Normalizar con los valores del entrenamiento
horas_normalizadas = horas_estudio / max_x1
asistencia_normalizada = asistencia / max_x2

resultado = predecir(
    horas_normalizadas,
    asistencia_normalizada,
    peso1,
    peso2,
    sesgo
)

print("\n--- PREDICCION DE UN ESTUDIANTE ---")
print("Horas de estudio:", horas_estudio)
print("Asistencia:", asistencia)
print(f"Probabilidad estimada de aprobar: {resultado * 100:.2f}%")
print("Clasificacion:", 1 if resultado >= 0.5 else 0)
