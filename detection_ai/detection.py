import numpy as np
from ultralytics import YOLO
from PIL import Image
import io


class ObjectDetector:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        # Traitement YOLO
        results = self.model(frame)
        annotated_frame = results[0].plot()
        return annotated_frame
