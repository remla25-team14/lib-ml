from setuptools import setup, find_packages

setup(
    name="libml",
    version="0.1.6",
    description="ML preprocessing library",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "nltk==3.8.1",
        "pandas==2.2.3",
        "numpy==1.26.4"
    ],
    python_requires=">=3.8",
)