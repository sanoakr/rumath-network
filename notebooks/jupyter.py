import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **ノートブックとは**

    ノートブックは、Python をインタラクティブに動作させるための対話型の実行環境です。
    ノートブック上では、この文章のように実行可能な Python コードの他に、テキストや数式、画像などを含めることができます。

    $$\sin^2\theta + \cos^2\theta = 1$$

    ノートブック環境として有名なのは **Jupyter**（ジュピター）で、この科目の教材も以前は Jupyter Notebook（`.ipynb` ファイル）で配布していました。
    現在は、Jupyter を発展させた **marimo**（マリモ）というノートブックを使っています。いま読んでいるこのページが marimo のノートブックです。

    | | Jupyter | marimo |
    |---|---|---|
    | ファイル形式 | `.ipynb`（JSON） | `.py`（ふつうの Python ファイル） |
    | セルの実行 | 自分で選んだ順に実行 | 変数の依存関係を追跡し、**関係するセルを自動で再実行** |
    | 動かす場所 | Jupyter / Colab / VS Code | ブラウザだけで動く（インストール不要）、VS Code、ローカル |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **ノートブックを実行するには**

    この科目のノートブックは、科目 Web ページからブラウザで開くだけで実行できます（WebAssembly 版の Python がブラウザ内で動きます）。
    自分の PC に何もインストールする必要はありません。

    自分の PC 上で動かしたい場合は、Python がインストール済みであれば次の 2 行で動きます。

    ```
    pip install marimo
    marimo edit jupyter.py
    ```

    また、このノートブックはふつうの Python ファイルなので、`python jupyter.py` として**スクリプトとして実行する**こともできます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **セルを実行する**

    Python のコードは以下のような BOX（**コードセル**）に記述されています。
    セルを選択した状態で `Shift + Enter` を押すか、セル右の ▷ をクリックすると、セル内の Python コードが実行されます。

    以下の 2 つのセルを上から順に実行してみましょう。
    """)
    return


@app.cell
def _():
    a = 1234
    b = 5678
    return a, b


@app.cell
def _(a, b):
    b / a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `b / a` の計算結果がセルの下に表示されたと思います。

    次に、**上のセルの `a`, `b` の値を書き換えて実行**してみてください。
    `b / a` のセルは自分で実行し直さなくても、**自動的に再実行されて結果が変わります**。

    ノートブック内のコードセルは独立しておらず、名前空間（変数）を共有しています。
    marimo は「どのセルがどの変数を使っているか」を追跡しているので、`a` や `b` を変えると、それを使っているセルがすべて再計算されます。
    このように、ノートブックではコードセル内の Python コードを対話的に修正・実行することができます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **変数は「1 つのセルで 1 回だけ」定義する**

    Jupyter では、別のセルで `a = 0.1` のように同じ変数を定義し直すことができました。
    その代わり「どのセルを何番目に実行したか」によって結果が変わってしまい、混乱のもとになっていました。

    marimo では、**同じ変数を複数のセルで定義することはできません**（エラーになります）。
    試しに、以下のセルの `a = 0.1` の行頭にある `# ` を消して実行してみてください。
    """)
    return


@app.cell
def _():
    # a = 0.1
    # b = 123 ** 99
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    「`a` が複数のセルで定義されている」というエラーになったはずです。
    値を変えたいときは、**最初に定義したセルを書き換える**のが marimo の流儀です。
    こうすることで「上から順に読めば、いま表示されている結果になる」ことが常に保証されます。

    セル内だけで使う一時的な変数には、`_tmp` のように名前の先頭に `_` を付けると、他のセルと衝突しなくなります。
    """)
    return


if __name__ == "__main__":
    app.run()
