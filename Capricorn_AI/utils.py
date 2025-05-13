# Capricorn_AI/utils.py
"""
Utility functions for image loading, preprocessing, and prediction.
"""
import numpy as np
from PIL import Image

from .models import load_model as _load_model


def load_image(path, target_size=(224, 224)):
    """Load an image file and return as a NumPy array."""
    img = Image.open(path).convert('RGB')
    img = img.resize(target_size)
    return np.array(img)


def preprocess_input(img_array, model_name='capricorn0.1'):
    """Preprocess array based on model architecture requirements."""
    # Normalize to [0,1]
    img = img_array.astype('float32') / 255.0
    # expand dims for batch
    return np.expand_dims(img, axis=0)


def predict(model_name, image_array):
    """Run inference on a raw image array using the named model."""
    model = _load_model(model_name)
    batch = preprocess_input(image_array, model_name)
    return model.predict(batch)
