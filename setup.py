#!/usr/bin/python
"""Setuptools-based installation."""
from pathlib import Path

from setuptools import find_packages, setup

PACKAGE_DIR = "yolov5_face"
readme = Path(__file__).parent.joinpath(PACKAGE_DIR, "README.md")
requirements = Path(__file__).parent.joinpath("requirements.txt")
description = "yolov5-face wrapper"
version = "0.1.1"

with requirements.open() as file:
    dependencies = [line.rstrip().split("~=")[0] for line in file]


setup(
    name="yolov5_face",
    packages=find_packages(),
    description=description,
    long_description=description,
    author="Sukhikh Roman",
    version=version,
    include_package_data=True,
    install_requires=dependencies,
    dependency_links=[
        "https://download.pytorch.org/whl/cpu/torch_stable.html",
    ],
)
