# Make your Python tests smell good!

Pytest-Smell is a Python library for detecting bad smells in unit tests written with the help of Pytest.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pytest-smell
```

## Usage

```bash
# Basic usage
pytest-smell

# Verbose output with traceback to smell in code
pytest-smell --verbose

# Specifying tests directory (if there is one dedicated) for optimization
pytest-smell --tests_path=path_to_tests

# Specifying output path for exporting results as a CSV file
pytest-smell --out_path=path_to_desired_directory

# Using it in a CI pipeline (returning 0 as exit code if no smells were found, 1 otherwise)
pytest-smell --ci
```

## Contributing
The library is still work in progress and serves as a research tool. Any collaboration or discussion is welcome.
Contact: alexandrubodeag@gmail.com