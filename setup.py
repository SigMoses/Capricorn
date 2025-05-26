# setup.py
from setuptools import setup, find_packages
import pathlib

# Project root
here = pathlib.Path(__file__).parent.resolve()

# Read long description from README
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Parse requirements
requirements = []
for line in (here / 'requirements.txt').read_text(encoding='utf-8').splitlines():
    req = line.strip()
    if req and not req.startswith('#'):
        requirements.append(req)

setup(
    name='capricorn',
    version='0.1.0',
    description='Deep learning histopathology classification with Keras',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Moshe Newman',  # TODO: replace with actual author if desired
    url='https://github.com/SigMoses/Capricorn.git',  # TODO: update URL if needed
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # Include any .keras files placed under capricorn/models/
        'capricorn': ['ai_models/*.keras'],
    },
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: TensorFlow',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
