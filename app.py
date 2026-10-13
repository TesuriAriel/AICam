import cv2
import numpy as np

def main():
    # Inicializar la captura de video (0 = webcam USB predeterminada)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo conectar con la webcam.")
        return

    print("Cámara iniciada. Detección básica de formas activa. Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el fotograma.")
            break

        # Optimización para Raspberry Pi: Redimensionar imagen
        frame = cv2.resize(frame, (640, 480))

        # --- Detección y enmarcado básico de formas ---
        # 1. Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 2. Aplicar desenfoque para reducir ruido
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # 3. Umbralización para destacar objetos/formas
        _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)
        
        # 4. Encontrar contornos de las formas
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 5. Enmarcar las formas detectadas (sin categorizar)
        for c in contours:
            # Filtrar contornos muy pequeños para evitar ruido visual
            if cv2.contourArea(c) > 1000:
                x, y, w, h = cv2.boundingRect(c)
                # Dibujar rectángulo alrededor de la forma
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostrar el resultado en ventana
        cv2.imshow("AICam - Deteccion Basica de Formas", frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
