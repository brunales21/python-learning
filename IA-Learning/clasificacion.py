import tensorflow as tf  # Importar TensorFlow, una biblioteca de aprendizaje automático.
import numpy as np  # Importar NumPy, una biblioteca para trabajar con matrices y arreglos.

# Cargar el modelo preentrenado MobileNetV2
model = tf.keras.applications.MobileNetV2(weights="imagenet")  # Cargar el modelo MobileNetV2 preentrenado en el conjunto de datos ImageNet.

# Cargar una imagen de prueba (reemplaza con la ruta de tu propia imagen)
image_path = 'C:\\Users\\2DAM\\PycharmProjects\\IA-Learning\\1671388889038.jpg'  # Ruta de la imagen que deseas clasificar
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))  # Cargar la imagen y redimensionarla a 224x224 píxeles

# Preprocesar la imagen
image = tf.keras.preprocessing.image.img_to_array(image)  # Convertir la imagen a un arreglo NumPy
image = np.expand_dims(image, axis=0)  # Agregar una dimensión adicional para crear un lote de imágenes
image = tf.keras.applications.mobilenet_v2.preprocess_input(image)  # Preprocesar la imagen según las expectativas de MobileNetV2

# Realizar la predicción
predictions = model.predict(image)  # Realizar una predicción en la imagen utilizando el modelo MobileNetV2

# Decodificar las predicciones (clasificación en ImageNet)
decoded_predictions = tf.keras.applications.imagenet_utils.decode_predictions(predictions)  # Decodificar las predicciones en etiquetas humanamente legibles

# Mostrar las predicciones
for _, label, score in decoded_predictions[0]:  # Iterar a través de las etiquetas y puntuaciones de las predicciones
    print(f"{label}: {score:.2f}")  # Imprimir la etiqueta y la puntuación
