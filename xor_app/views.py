from django.shortcuts import render

# Se carga la libreria para operaciones matemáticas/estadísticas
import numpy as np

# Se importa las librerias para la red neuronal
from keras.models import Sequential
from tensorflow.keras.layers import Dense


# def main(request):
#     return render(request, "index.html")


# Create your views here.
def predict(request):
    # Definir las entradas y salidas para la compuerta XOR
    entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")
    salidas = np.array([[0], [1], [1], [0]], "float32")

    # Crear la red neuronal
    modelo = Sequential()
    modelo.add(Dense(8, activation="relu", input_dim=2))
    modelo.add(Dense(1, activation="sigmoid"))

    # Compilar el modelo
    # modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    modelo.compile(
        optimizer="adam", loss="mean_squared_error", metrics=["binary_accuracy"]
    )

    # Entrenar el modelo
    modelo.fit(entradas, salidas, epochs=1000, verbose=0)

    # Evaluamos el modelo
    loss, accuracy = modelo.evaluate(entradas, salidas, verbose=0)
    print(f"Pérdida: {loss:.4f}, Precisión: {accuracy:.2f}%")

    # Realizamos predicciones
    predictions = modelo.predict(entradas)
    print("Predicciones:")
    print(np.round(predictions))

    # Estructura los datos en un formato que se pueda pasar a la plantilla
    results = []
    for entrada, salida_esperada, prediccion_obtenida in zip(
        entradas, salidas, predictions
    ):
        results.append(
            {
                "entrada_1": int(entrada[0]),
                "entrada_2": int(entrada[1]),
                "salida_esperada": int(salida_esperada[0]),
                "prediccion_obtenida": prediccion_obtenida[0],
            }
        )

    context = {"results": results}

    return render(request, "../templates/index.html", context)
