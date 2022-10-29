# `pytest` Demos for `plotly_dash_demos` Package

<!-- MarkdownTOC -->

- How to Run
- Demos
    - `dash-geographical`
    - `dash-statistics`

<!-- /MarkdownTOC -->

## How to Run

These demos should be run from the top-most directory in this repo (alongside the outer [README.md]() and `conftest.py` files) by calling:

```bash
pytest -o addopts="" -o log_cli=true ./tests_demo/${DIRECTORY}/run.py
```

Where `${DIRECTORY}` should be the folder name for the demo here that you want to actually run.

Note that with `dash` many of these will spin-up a local webserver and needed to be viewed through a web-browser.

The above command will do a couple of things, so you can obviously modify the command as needed if you don't want any of these options:
- `-o addopts=""` - Disables the `pyproject.toml` config options for the `addopts` field
- `-o log_cli=true` - Enable Logging in the Terminal
- `pytest ./tests_demo/${DIRECTORY}/run.py` - Run only the tests (`test_` Methods) in the given `run.py` Module

## Demos

These are the demos provided here in this `tests_demo` folder. Each can be run the same way, by following the [How to Run](#how-to-run) section.

### `dash-geographical`

```bash
pytest -o addopts="" -o log_cli=true ./tests_demo/dash-geographical/run.py
```

### `dash-statistics`

```bash
pytest -o addopts="" -o log_cli=true ./tests_demo/dash-statistics/run.py
```

