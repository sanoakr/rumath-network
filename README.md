# rumath-network

[日本語](./README.ja.md) | English

Jupyter notebooks for the "Network and Exercises" course at Ryukoku University, Department of Mathematical Sciences and Informatics.

## Course site

The course pages (schedule, lecture slides, exercises) are published with GitHub Pages:
**<https://sanoakr.github.io/rumath-network/>**

The site is built from `docs/` with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
and deployed by `.github/workflows/pages.yml` on every push to `main`.
Pages for each week are added as the course progresses.

```fish
uv sync                 # install mkdocs-material
uv run mkdocs serve     # preview at http://127.0.0.1:8000/rumath-network/
```

## Notebooks

| File | Content |
|------|---------|
| `python_tutorial.ipynb` | Python basics tutorial |
| `python_function.ipynb` | Functions and modules |
| `python_numeric.ipynb` | Numerical computation (NumPy) |
| `python_string-list.ipynb` | Strings and lists |
| `python_sympy.ipynb` | Symbolic computation (SymPy) |

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab
- NumPy, SymPy

```fish
pip install jupyter numpy sympy
```

## Usage

```fish
jupyter notebook
```
