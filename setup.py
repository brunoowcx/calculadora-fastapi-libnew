from setuptools import setup, find_packages

# Lendo o README.md para o PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculatornew-lib",  # ⚡ Nome com hífen para o PyPI
    version="0.1.1",
    description="Biblioteca de operações matemáticas básicas em Python com raiz e exponencial.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bruno Alves de Moraes",
    author_email="brunoowcx1@gmail.com",
    url="https://github.com/brunoowcx/calculadora-fastapi-lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
