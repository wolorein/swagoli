# SWAGOLI -demo

This is a small python demo with fastapi.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install poetry.
(You can also use venv etc.)

```bash
pip3 install poetry
poetry install
```

## Usage

```python
# RUN
poetry run python3 main.py
# ENDPOINTS
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/travel/beforestarts/2020-05-14T06:04:00
http://127.0.0.1:8000/travel/withstops/AAA%20LLL
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Todo

- Comment the code: description, input, output
- Pagination for endpoints
- Input check/sanity
- Create tests
- Create logging
- Create debug
