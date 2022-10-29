# `plotly` and `dash` Demos

Example code using the Python `plotly` and `dash` packages for demonstration and (educational) reference.

See here:
- https://plotly.com/python/
- https://dash.plotly.com/

The `pandas` library provides a `Series`, `DataFrame`, and `MultiIndexDataFrame` set of utility functions and classes for organising, accessing, and processing tabular data (JSONs, CSVs, Parquet files, _etc._). Some of the syntax and implementation is non-standard in comparison to most Python code, so this reference repository should be a helpful means of pointing out some of the quirks of using `pandas`.

I created this repository to help remind myself how the `pandas` syntax works, and to test out some other features. This is available for general reference, in case it's helpful to anyone else.

<!-- MarkdownTOC -->

- Developer Setup
- Local Package: `pandas_demos`
- Testing
    - Unit-Tests
- License \(Copyright\)

<!-- /MarkdownTOC -->


## Developer Setup

- https://direnv.net/
- https://github.com/pyenv/pyenv

1. `pyenv install` -- skip this if you already have the version on your system
1. `direnv allow`
1. `pip install --upgrade pip`
1. `pip install poetry` -- Assumes `poetry >= 1.20.0`
1. `poetry install`

## Local Package: `pandas_demos`

> TBD

## Testing

These sections explain and show how to test this code and how it was tested during development.

A nice reference on the different kinds of Software Testing for Python can be found here: https://realpython.com/python-testing/

An introduction to `pytest` with technical details can be found here: https://docs.pytest.org/en/7.1.x/example/simple.html

### Unit-Tests

Run:

```bash
pytest
```

This should produce an output that looks like:

```bash
========================================== test session starts ===========================================
platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/tommy/dev/tommypkeane/pandas_demos, configfile: pyproject.toml, testpaths: tests_unit
plugins: hypothesis-6.56.3, cov-4.0.0
collected 1 item

tests_unit/pandas_demos/test_dataframe_examples.py .

---------- coverage: platform darwin, python 3.10.7-final-0 ----------
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
pandas_demos/__init__.py                         0      0   100%
pandas_demos/dataframe_examples.py               2      0   100%
pandas_demos/dataframe_groupby_examples.py       0      0   100%
pandas_demos/series_examples.py                  0      0   100%
----------------------------------------------------------------
TOTAL                                            2      0   100%

=========================================== 1 passed in 0.27s ============================================
````

## License (Copyright)

See [LICENSE](./LICENSE) file.
