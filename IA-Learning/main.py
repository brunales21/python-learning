# Importa las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de entrenamiento
tamanos = np.array([1400, 1600, 1700, 1875, 1100]).reshape(-1, 1)  # Tamaños de las casas
habitaciones = np.array([3, 3, 4, 3, 2])  # Número de habitaciones
precios = np.array([245000, 312000, 279000, 308000, 199000])  # Precios de las casas

# Crea un modelo de regresión lineal
modelo = LinearRegression()

# Entrena el modelo con los datos
modelo.fit(np.column_stack((tamanos, habitaciones)), precios)

# Realiza predicciones para nuevos datos
tamanos_nuevos = np.array([1500, 1800]).reshape(-1, 1)
habitaciones_nuevas = np.array([3, 4])
predicciones = modelo.predict(np.column_stack((tamanos_nuevos, habitaciones_nuevas)))

# Imprime las predicciones
for i in range(len(predicciones)):
    print(f"Para una casa de {tamanos_nuevos[i][0]} pies cuadrados y {habitaciones_nuevas[i]} habitaciones, el precio estimado es ${predicciones[i]:.2f}")

# Gráfico de los datos y la línea de regresión
plt.scatter(tamanos, precios, label='Datos reales')
plt.plot(tamanos, modelo.predict(np.column_stack((tamanos, habitaciones))), color='red', label='Línea de regresión')
plt.xlabel('Tamaño de la casa (pies cuadrados)')
plt.ylabel('Precio de la casa')
plt.legend()
plt.show()
