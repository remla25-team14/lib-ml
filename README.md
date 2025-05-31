# lib-ml

ML preprocessing library for sentiment analysis with automatic versioning.

## Quick Start

```bash
git clone https://github.com/remla25-team14/lib-ml.git
cd lib-ml
pip install -e .
python test_libml.py
```

## Usage

```python
import libml

# Check version
print(libml.__version__)

# Preprocess reviews
data = {'Review': ['Great food!', 'Bad service.']}
result = libml.preprocess_reviews(data)
print(result)  # ['great food', 'bad servic']
```

## Features

- ✅ Automatic versioning from Git tags
- ✅ Text preprocessing for ML models
- ✅ Modern Python packaging

## Install from Git

```bash
pip install git+https://github.com/remla25-team14/lib-ml@v0.1.6
```

That's it! 🎉
