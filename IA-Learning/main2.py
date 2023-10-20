# Importa las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

producto = np.array([2, 4, 5, 6]).reshape(-1, 1)
precio = np.array([4, 8, 9, 12])

modeloRegLin = LinearRegression()
modeloRegLin.fit(producto, precio)

nuevoDato = np.array([20]).reshape(-1, 1)
print(modeloRegLin.predict(nuevoDato))

