# cartoon_or_not.py

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import requests
from io import BytesIO

class CartoonOrNot:
    def __init__(self, model_url, labels_url):
        # Download model and labels
        model_content = self._download_content('https://github.com/TTNVXX/CartoonOrNot/blob/main/model/keras_model.h5')
        labels_content = self._download_content('https://github.com/TTNVXX/CartoonOrNot/blob/main/model/labels.txt')

        # Load model and labels
        self.model = load_model(BytesIO(model_content), compile=False)
        self.class_names = labels_content.decode("utf-8").splitlines()

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

    def _download_content(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

