#!/usr/bin/env python3
from setuptools import find_packages, setup

long_description = open("README.md", "r", encoding="utf-8").read()

setup(
    name="hearbaseline",
    version="2021.0.2",
    description="Holistic Evaluation of Audio Representations (HEAR) 2021 -- Baseline Model",
    author="HEAR 2021 NeurIPS Competition Committee",
    author_email="deep@neuralaudio.ai",
    url="https://github.com/neuralaudio/hear-baseline",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/neuralaudio/hear-baseline/issues",
        "Source Code": "https://github.com/neuralaudio/hear-baseline",
    },
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.6",
    install_requires=[
        "librosa",
        "numpy",
        "tensorflow",
        "torch",
        # For wav2vec2 model
        "speechbrain",
        "transformers==4.4.0"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-env",
        ],
        "dev": [
            "pre-commit",
            "black",  # Used in pre-commit hooks
            "pytest",
            "pytest-cov",
            "pytest-env",
        ],
    },
)
