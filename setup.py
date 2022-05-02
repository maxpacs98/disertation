import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pytest-smell",
    version="1.0.4",
    description="Automated bad smell detection tool for Pytest",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/maxpacs98/disertation",
    author="Bodea Alex",
    author_email="alexandrubodeag@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["pytest_smell"],
    entry_points={
        "console_scripts": [
            'pytest-smell=pytest_smell:pytest_smell',
        ]
    },
)
