# README.md
---
# Capricorn AI

Deep-learning based histopathology image classifier built with TensorFlow Keras.

## Overview

Capricorn AI provides pre-trained Keras models for classifying H\&E–stained tissue patches into diagnostic categories. It offers a simple Python API to load different model versions, run inference on images, and integrate into larger pipelines.
PyPI link: https://pypi.org/project/capricorn-ai/

## Installation

```bash
# Clone the repo
git clone https://github.com/SigMoses/Capricorn.git
cd capricorn

# Install dependencies
pip install -r requirements.txt

# Install as a package
pip install capricorn-ai
```

Alternatively, install directly from GitHub:

```bash
pip install git+https://github.com/SigMoses/Capricorn.git
```

## Quickstart

```python
from capricorn import list_models, load_model, load_image, predict

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
from capricorn import load_image, predict, ALL_LABELS, label_confidences

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

*Add your own retrained models by placing the `.keras` file in `capricorn/ai_models/` and updating `capricorn/ai_models.py`.*

## Development & Testing

* Dependencies are in `requirements.txt`.
* Run tests with:

  ```bash
  pytest
  ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-model`).
3. Add your `.keras` model in `capricorn/ai_models/` and register it in `capricorn/models.py`.
4. Update docs and add tests.
5. Submit a pull request.

## Credits

- **Original Progenitor**  
  Capricorn AI was conceived and developed by **Moshe Newman**.  

- **Dataset**  
  This project relies on the MedMNIST dataset. Please credit the MedMNIST team as follows:  
  > Jiancheng Yang, Rui Shi, Donglai Wei, Zequan Liu, Lin Zhao, Bilian Ke, Hanspeter Pfister, Bingbing Ni.  
  > “MedMNIST v2—A large-scale lightweight benchmark for 2D and 3D biomedical image classification.” *Scientific Data*, 2023.  
  >  
  > Jiancheng Yang, Rui Shi, Bingbing Ni.  
  > “MedMNIST Classification Decathlon: A Lightweight AutoML Benchmark for Medical Image Analysis.” *IEEE 18th International Symposium on Biomedical Imaging (ISBI)*, 2021.

- **Usage & Modification**  
  You are free to modify or use this code as you please, **provided** that you retain proper credit to Moshe Newman as the original progenitor of Capricorn AI, and credit the MedMNIST team for the dataset as cited above.

## License

[MIT License](LICENSE)
