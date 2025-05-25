# Capricorn AI
Deep-learning based histopathology image classifier built with TensorFlow Keras.

# Overview:
Capricorn AI provides pre-trained Keras models for classifying H&E–stained tissue patches into diagnostic categories. It offers a simple Python API to load different model versions, run inference on images, and integrate into larger pipelines.

# Installation:

## Clone the repo
git clone https://github.com/your-org/capricorn-ai.git
cd capricorn-ai

## Install dependencies
pip install -r requirements.txt

## Install as a package
pip install .

Alternatively, install directly from GitHub:

pip install git+https://github.com/your-org/capricorn-ai.git

# Quickstart

from capricorn_ai import list_models, load_model, load_image, predict

## List available models
print(list_models())  # ['capricorn0.1']

## Load an image
img = load_image('path/to/slide_patch.png')

## Run prediction
detections = predict('capricorn0.1', img)
print(detections)


# Available Models:

capricorn0.1: Initial version trained on 3 PathMNIST subsets.

Add your own retrained models by placing the .keras file in models/ and updating Capricorn_AI/models.py.


# Development & Testing:

Dependencies are in requirements.txt.


# Run tests with:

pytest


# Contributing:

+ Fork the repository.

+ Create a new branch (git checkout -b feature/my-model).

+ Add your .keras model in models/ and register it in Capricorn_AI/models.py.

+ Update docs and add tests.

+ Submit a pull request.


# License:

MIT License