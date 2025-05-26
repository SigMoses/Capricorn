# Capricorn_AI/utils.py
"""
Utility functions for image loading, preprocessing, and prediction.
"""
import numpy as np # type: ignore
from PIL import Image # type: ignore

from .models import load_model as _load_model
from .labels import ALL_LABELS, NUM_CLASSES


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


def predict(model_name, image_array, top_k=None):
    """
    Run inference on a raw image array using the named model,
    and return a sorted list of (label, confidence) tuples.
    If top_k is given, returns only the top_k entries.
    """
    model = _load_model(model_name)
    batch = preprocess_input(image_array, model_name)
    raw_probs = model.predict(batch)[0]  # one-dimensional array

    # sanity check
    if raw_probs.shape[0] != len(ALL_LABELS):
        raise ValueError(
            f"Expected {len(ALL_LABELS)} outputs, got {raw_probs.shape[0]}"
        )

    # pair & sort by confidence descending
    labeled = sorted(
        zip(ALL_LABELS, raw_probs),
        key=lambda x: x[1],
        reverse=True
    )

    return labeled if top_k is None else labeled[:top_k]

def label_confidences(probs, labels=ALL_LABELS):
    """
    Given a 1D array of softmax probabilities (shape == NUM_CLASSES),
    return a list of (label, confidence) tuples sorted by confidence desc.
    """
    return sorted(zip(labels, probs), key=lambda x: x[1], reverse=True)
