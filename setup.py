
from setuptools import setup, find_packages

setup(
    name="sharedflet",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.4.7'
    ],
    author='Amir Louktila',
    author_email='amir.louktila@example.com',
    description="SharedPreference-like encrypted storage using JSON for Flet apps",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
