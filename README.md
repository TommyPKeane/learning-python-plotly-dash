# `plotly` and `dash` Demos

Example code using the Python `plotly` and `dash` packages for demonstration and (educational) reference.

See here:
- https://plotly.com/python/
- https://dash.plotly.com/

<!-- MarkdownTOC -->

- Developer Setup
- Local Package: `plotly_dash_demos`
- Testing
  - Unit-Tests
  - Demo Tests
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

## Local Package: `plotly_dash_demos`

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
rootdir: /Users/tommy/dev/tommypkeane/plotly-dash_demos, configfile: pyproject.toml, testpaths: tests_unit
plugins: hypothesis-6.56.3, dash-2.6.2, cov-4.0.0
collected 0 items
/Users/tommy/dev/tommypkeane/plotly-dash_demos/.direnv/python-3.10.7/lib/python3.10/site-packages/coverage/control.py:801: CoverageWarning: No data was collected. (no-data-collected)
  self._warn("No data was collected.", slug="no-data-collected")

---------- coverage: platform darwin, python 3.10.7-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
plotly_dash_demos/__init__.py       0      0   100%
---------------------------------------------------
TOTAL                               0      0   100%

========================================= no tests ran in 0.01s ==========================================
````

### Demo Tests

These demos are larger "functional tests" that are actually localized demonstrations of `plotly` and `dash` functionality which can be tested, edited, or run here in-place.

Some of these may not rely on the local `plotly_dash_demos` package, and may be fully self-contained.

See the local [README.md](./tests_demo/README.md) for more details on what demos are currently available, and how to run them.

## License (Copyright)

See [LICENSE](./LICENSE) file.
