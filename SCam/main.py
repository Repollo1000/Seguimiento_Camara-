import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

nombre_dispositivo = "Logitech StreamCam"
cap = cv2.VideoCapture(0)

# Verifica si el dispositivo de imagen se abrió correctamente
if not cap.isOpened():
    print("Error al abrir el dispositivo de imagen")
    exit()

while True:
    ret, frame = cap.read()  # Unpack the return value

    # Verifica si el fotograma se leyó correctamente
    if not ret:
        print("Error al leer el fotograma")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)

    if key == 27:
        break

# Liberar los recursos al finalizar
cap.release()
cv2.destroyAllWindows()
