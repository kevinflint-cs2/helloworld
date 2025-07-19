# HelloWorld

A minimal Python package that prints “Hello, world!” Built and managed with [Poetry](https://python-poetry.org), tested with [pytest](https://docs.pytest.org), and linted with [Black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [Flake8](https://flake8.pycqa.org).

## Codespace
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=1022198669)

## Project Structure

```
helloworld/
├── src/
│   └── helloworld/
│       └── hello.py
├── tests/
│   └── test_helloworld.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Prerequisites

- Python **3.8+**
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/kevinflint-cs2/helloworld.git
cd helloworld
poetry install
```

> This will create a virtual environment and install both runtime and development dependencies.

## Usage

Run the module directly:

```bash
poetry run python -m helloworld
```

You should see:

```
Hello, world!
```

## Running Tests

Execute the full test suite with:

```bash
poetry run pytest
```

## Linting

### Pre-commit (local)

We use [pre-commit](https://pre-commit.com) to auto-format and catch lint issues before each commit. If you haven’t already:

```bash
poetry run pre-commit install
```

To run all hooks against all files manually:

```bash
poetry run pre-commit run --all-files
```

### GitHub Actions (CI)

Our CI workflow will automatically run:

1. `black --check .`
2. `isort --check .`
3. `flake8 .`
4. `pytest`

on every push and pull request. See `.github/workflows/ci.yml`.

## Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -m "feat: add foo"`)  
4. Push to your branch (`git push origin feature/foo`)  
5. Open a Pull Request

Please make sure all tests and linters pass before submitting.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
