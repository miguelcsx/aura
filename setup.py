import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="aura",
    version="0.1.0",
    author="Miguel Cárdenas",
    description="A Discord bot application for study assistance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miguelcsx/aura",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "aura=app.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)