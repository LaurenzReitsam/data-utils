from setuptools import setup, find_packages

setup(
    name="data-utils",
    version="0.0.0",
    description="This package includes utilities to interact with data in GCP",
    author="Laurenz Reitsam",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=[
        "sklearn",
        "tensorflow",
    ]
)
