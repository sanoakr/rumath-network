# 教材ノートブック

Python の教材は **marimo** ノートブックです。リンクを開くと、ブラウザ内で Python が動きます（インストール不要。初回は読み込みに少し時間がかかります）。
セルを書き換えて実行しながら読み進めてください。

| ノートブック | 内容 | 使う回 |
|---|---|---|
| [ノートブックとは](https://sanoakr.github.io/rumath-network/notebooks/jupyter/) | セルの実行、marimo と Jupyter の違い | ex1 |
| [Python 入門](https://sanoakr.github.io/rumath-network/notebooks/python_tutorial/) | インタプリタ、動的型付け、インデント構文 | ex1 |
| [文字列とリスト](https://sanoakr.github.io/rumath-network/notebooks/python_string-list/) | 文字列・リストの操作、スライス | ex2 |
| [関数](https://sanoakr.github.io/rumath-network/notebooks/python_function/) | 関数の定義、引数と戻り値 | ex3 |
| [数値](https://sanoakr.github.io/rumath-network/notebooks/python_numeric/) | 整数・浮動小数点・Decimal・複素数 | 参考 |
| [SymPy](https://sanoakr.github.io/rumath-network/notebooks/python_sympy/) | 記号計算（数学系の参考） | 参考 |

## 自分の PC で動かす

ノートブックはふつうの Python ファイル（`.py`）です。ソースは [GitHub の `notebooks/`](https://github.com/sanoakr/rumath-network/tree/main/notebooks) にあります。

```
pip install marimo
marimo edit python_tutorial.py
```

VS Code を使う場合は拡張機能「marimo」を入れると、VS Code 内でノートブックを開けます。

!!! note "Jupyter 版"
    以前の Jupyter Notebook（`.ipynb`）も [リポジトリ直下](https://github.com/sanoakr/rumath-network) に残してあります。Google Colab で開きたい場合はそちらを使ってください。
