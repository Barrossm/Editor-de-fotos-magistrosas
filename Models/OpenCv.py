import cv2
import numpy

def tirar_foto_webcam():
    webcam = cv2.VideoCapture(0)

    if webcam.isOpened():
        print("Webcam aberta com sucesso!")
        validacao, frame = webcam.read()

        while validacao:
            validacao, frame = webcam.read()
            # Tratativa para evitar erro caso a janela feche de repente
            if not validacao:
                break
                
            cv2.imshow("Video da Webcam - Pressione ESC para fotografar", frame)
            key = cv2.waitKey(5)
            
            if key == 27: # ESC
                cv2.imwrite("Foto.png", frame)    
                break

    webcam.release()
    cv2.destroyAllWindows()
    return "Foto.png" 