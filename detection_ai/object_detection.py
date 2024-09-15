import cv2
import numpy as np
from detection import ObjectDetector

# Configuration
VIDEO_SOURCE = 0  # Utiliser 0 pour la webcam locale  , ou l'URL pour la caméra de la voiture  http://<adresse_ip>:<port>/
YOLO_MODEL_PATH = 'yolov8n.pt'  # Chemin vers  modèle YOLO

# Init du modéle
detector = ObjectDetector(YOLO_MODEL_PATH)

def main():
    # Initialisation de la caméra
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print(f"Unable to connect to camera at {VIDEO_SOURCE}")
        return

    while True:
        # Capture des images depuis la caméra
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Traitement de l'image avec YOLO
        annotated_frame = detector.process_frame(frame)

        # Affichage du flux vidéo annoté
        cv2.imshow("YOLO Object Detection", annotated_frame)

        # Quitter lorsque la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libération des ressources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
