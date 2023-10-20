# Importar las bibliotecas necesarias
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de entrenamiento
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Características (entrada)
y = np.array([2, 4, 5, 4, 5])  # Variable de salida

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Realizar una predicción
nueva_data = np.array([6]).reshape(-1, 1)
prediccion = modelo.predict(nueva_data)

# Imprimir la predicción
print(f"Predicción para X=6: {prediccion[0]:.2f}")
