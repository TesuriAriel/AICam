# Procesamiento de Imágenes y Detección de Formas con OpenCV
## 1. Introducción a OpenCV en Python

OpenCV es una biblioteca de código abierto que permite procesar imágenes y videos en tiempo real. En este proyecto, se utiliza Python y OpenCV para capturar imágenes desde una webcam y detectar formas presentes en la escena.

## 2. Etapas del Procesamiento
- Captura de video (cv2.VideoCapture): conecta la aplicación con la webcam y obtiene fotogramas continuamente.
- Redimensionamiento (cv2.resize): ajusta cada imagen a una resolución de 640 × 480 píxeles para reducir la carga de procesamiento.
- Conversión a escala de grises (cv2.cvtColor): simplifica la imagen eliminando la información de color y conservando los niveles de intensidad.
- Reducción de ruido (cv2.GaussianBlur): suaviza la imagen para disminuir pequeñas variaciones que podrían generar detecciones innecesarias.
- Umbralización (cv2.threshold): convierte la imagen en blanco y negro para facilitar la separación de ciertas formas respecto del fondo.
- Detección de contornos (cv2.findContours): identifica los límites de las regiones presentes en la imagen procesada.
- Delimitación de formas (cv2.boundingRect y cv2.rectangle): calcula las dimensiones de cada contorno válido y dibuja un rectángulo verde alrededor de las formas detectadas.
## 3. Filtrado de Detecciones

Para evitar que pequeñas irregularidades de la imagen generen demasiados rectángulos, el sistema descarta los contornos cuya área sea inferior o igual a 1000 píxeles cuadrados.

Este filtro ayuda a reducir el ruido visual y permite concentrarse en regiones de mayor tamaño. Sin embargo, el tamaño de un contorno no determina si corresponde a una persona.

## 4. Visualización en Tiempo Real

Los resultados se muestran en una nueva ventana del sistema, donde se visualiza el video capturado con los rectángulos verdes sobre las regiones detectadas.

El procesamiento se repite continuamente mientras la cámara está activa.

## 5. Rendimiento y Limitaciones

La aplicación utiliza técnicas básicas de procesamiento de imágenes que permiten detectar formas basicas.

Su funcionamiento puede verse afectado por la iluminación, las sombras, el fondo y el contraste entre los objetos y su entorno. Además, el umbral utilizado y el tamaño mínimo de los contornos influyen en los resultados.