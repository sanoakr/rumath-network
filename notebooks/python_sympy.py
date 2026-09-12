# /// script
# dependencies = ["sympy"]
# ///

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
    # Python の数式処理（数式処理 Sympy モジュール)

    Python には Mathematica や Maple などの数式処理ソフトウェアと同様に、数式処理を行うためのモジュール Sympy が用意されています。Sympy モジュールを使うと、数式を Python のコードで表現し、数式として微分・積分などの計算を行うことができます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sympy モジュールを使うには、まず Sympy モジュールのインポートが必要です。自分のPC上で実行する場合は Sympy モジュールのインストールも必要です。Google Colaboratory であれば Sympy モジュールがインストール済みなので、インポートのみで利用できます。
    """)
    return


@app.cell
def _():
    from sympy import symbols, init_printing, expand, factor, solve, diff, integrate, Matrix, det
    init_printing(use_unicode=True)
    return Matrix, det, diff, expand, factor, init_printing, integrate, solve, symbols


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    上記の2行目 init_printing() を実行すると、数式が LaTeX 形式で表示されるようになります。init_printing() を実行しない場合は、数式は文字列として表示されます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    x，y を数式の変数として定義します。
    """)
    return


@app.cell
def _(symbols):
    x, y = symbols('x y')
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    x を変数として使った数式 eq を定義します。数式は文字列として定義します。
    """)
    return


@app.cell
def _(x):
    eq = x**2 + x + 1
    return (eq,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    eq の2乗を展開します。
    """)
    return


@app.cell
def _(eq, expand):
    expand(eq**2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    eq を99乗した数式 eq99 を定義して、それを因数分解します。ちゃんと eq の99乗として因数分解されています。
    """)
    return


@app.cell
def _(eq, expand, factor):
    eq99 = expand(eq**99)
    print(eq99)
    factor(eq99)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    eq の解を求めましょう。複数の解がリストとして返されます。
    """)
    return


@app.cell
def _(eq, solve):
    solve(eq)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    微分。
    """)
    return


@app.cell
def _(diff, eq):
    diff(eq)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    積分。
    """)
    return


@app.cell
def _(eq, integrate):
    integrate(eq)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    x について 0 から 1 まで積分します。
    """)
    return


@app.cell
def _(eq, integrate, x):
    integrate(eq, (x, 0, 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    M を4字の正方行列とします。
    """)
    return


@app.cell
def _(Matrix):
    M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
    M
    return (M,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    M の行列式。
    """)
    return


@app.cell
def _(M):
    M.det()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    逆行列。
    """)
    return


@app.cell
def _(M):
    M.inv()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    固有値。
    """)
    return


@app.cell
def _(M):
    M.eigenvals()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    固有ベクトル。
    """)
    return


@app.cell
def _(M):
    M.eigenvects()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    M を対角化します。
    """)
    return


@app.cell
def _(M):
    P, D = M.diagonalize()
    P, D, P.inv()
    return D, P


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ちゃんと M に戻ります。
    """)
    return


@app.cell
def _(D, P):
    P*D*P.inv()
    return


if __name__ == "__main__":
    app.run()
