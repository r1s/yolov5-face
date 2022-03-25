#!/usr/bin/python
"""Setuptools-based installation."""
from pathlib import Path

from setuptools import find_packages, setup

PACKAGE_DIR = "yolov5_face"
readme = Path(__file__).parent.joinpath(PACKAGE_DIR, "README.md")
requirements = Path(__file__).parent.joinpath("requirements.txt")
description = Path(__file__).parent.joinpath(PACKAGE_DIR, "README.md").open(encoding="utf-8").read()
version = "0.1"

with requirements.open() as file:
    dependencies = [line.rstrip() for line in file]


setup(
    name="yolov5_face",
    packages=find_packages(),
    description=description,
    long_description=description,
    author="EPAM Systems",
    version=version,
    include_package_data=True,
    install_requires=dependencies,
    dependency_links=[
        "https://download.pytorch.org/whl/cpu/torch_stable.html",
    ],
)


# pip install torch==1.10.2+cpu --find-links https://download.pytorch.org/whl/cpu/torch_stable.html
# pip install torchvision==0.11.3+cpu --find-links https://download.pytorch.org/whl/cpu/torch_stable.html
# pip install torchaudio==0.10.2+cpu --find-links https://download.pytorch.org/whl/cpu/torch_stable.html
