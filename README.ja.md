# rumath-network

[English](./README.md) | 日本語

龍谷大学先端理工学部数理・情報科学課程「ネットワーク及び演習」の Jupyter ノートブック集。

## 講義ページ

講義ページ（スケジュール・スライド・演習課題）は GitHub Pages で公開しています:
**<https://sanoakr.github.io/rumath-network/>**

`docs/` を [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) でビルドし、
`main` への push ごとに `.github/workflows/pages.yml` がデプロイします。
各回のページは講義の進行に合わせて追加します。

```fish
uv sync                 # mkdocs-material をインストール
uv run mkdocs serve     # http://127.0.0.1:8000/rumath-network/ でプレビュー
```

## ノートブック一覧

| ファイル | 内容 |
|---------|------|
| `python_tutorial.ipynb` | Python 入門 |
| `python_function.ipynb` | 関数とモジュール |
| `python_numeric.ipynb` | 数値計算（NumPy） |
| `python_string-list.ipynb` | 文字列とリスト |
| `python_sympy.ipynb` | 記号計算（SymPy） |

## 必要環境

- Python 3.8+
- Jupyter Notebook または JupyterLab
- NumPy, SymPy

```fish
pip install jupyter numpy sympy
```

## 使い方

```fish
jupyter notebook
```
