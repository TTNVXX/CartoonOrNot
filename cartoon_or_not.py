# cartoon_or_not.py

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

class CartoonOrNot:
    def __init__(self, model_path, labels_path):
        self.model = load_model(model_path, compile=False)
        self.class_names = open(labels_path, "r").readlines()

    def analyze(self, image_path):
        data = self._prepare_image(image_path)
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = self.class_names[index][2:].strip()  # Strip to remove newline characters
        confidence_score = prediction[0][index]
        return class_name, confidence_score

    def _prepare_image(self, image_path):
        size = (224, 224)
        image = Image.open(image_path).convert("RGB")
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
        return data
