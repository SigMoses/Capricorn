---

# requirements.txt

tensorflow>=2.10.0
numpy>=1.19.5
Pillow>=8.0.0

# (Optional, for tests and dev)

pytest>=7.0.0

---

# README.md

# Capricorn AI

Deep-learning based histopathology image classifier built with TensorFlow Keras.

## Overview

Capricorn AI provides pre-trained Keras models for classifying H\&E–stained tissue patches into diagnostic categories. It offers a simple Python API to load different model versions, run inference on images, and integrate into larger pipelines.

## Installation

```bash
# Clone the repo
git clone https://github.com/your-org/capricorn-ai.git
cd capricorn-ai

# Install dependencies
pip install -r requirements.txt

# Install as a package
pip install .
```

Alternatively, install directly from GitHub:

```bash
pip install git+https://github.com/your-org/capricorn-ai.git
```

## Quickstart

```python
from capricorn_ai import list_models, load_model, load_image, predict

# List available models
print(list_models())  # ['capricorn0.1']

# Load an image
img = load_image('path/to/slide_patch.png')

# Run prediction
detections = predict('capricorn0.1', img)
print(detections)
```

## Example Usage

```python
from capricorn_ai import load_image, predict, ALL_LABELS, label_confidences

# Load and preprocess an image patch
img = load_image("path/to/patch.png")

# Run inference (returns shape (1, NUM_CLASSES))
probs = predict("capricorn0.1", img)[0]

# Print all label confidences in descending order
for label, confidence in label_confidences(probs):
    print(f"{label:30s} {confidence*100:5.1f}%")
```

## Available Models

* **capricorn0.1**: Initial version trained on PathMNIST subsets.

*Add your own retrained models by placing the `.keras` file in `models/` and updating `Capricorn_AI/models.py`.*

## Development & Testing

* Dependencies are in `requirements.txt`.
* Run tests with:

  ```bash
  pytest
  ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-model`).
3. Add your `.keras` model in `models/` and register it in `Capricorn_AI/models.py`.
4. Update docs and add tests.
5. Submit a pull request.

## License

[MIT License](LICENSE)
