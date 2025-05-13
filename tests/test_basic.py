import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from PIL import Image
import pytest

from capricorn_ai.models import list_models, get_model_path
from capricorn_ai.utils import load_image, preprocess_input

def test_list_models():
    models = list_models()
    assert 'capricorn0.1' in models, f"Expected 'capricorn0.1' in {{models}}"

def test_get_model_path_exists():
    path = get_model_path('capricorn0.1')
    assert os.path.isfile(path), f"Model file not found at {{path}}"

def test_load_and_preprocess(tmp_path):
    # Create a random image and save
    arr = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    img_file = tmp_path / "test.png"
    Image.fromarray(arr).save(str(img_file))

    img = load_image(str(img_file))
    assert img.shape == (224, 224, 3), f"Unexpected loaded shape: {{img.shape}}"

    batch = preprocess_input(img)
    assert batch.shape == (1, 224, 224, 3), f"Unexpected batch shape: {{batch.shape}}"
