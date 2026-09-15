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
    # **Python の数値リテラルと型**

    ここでは Python で利用できる特徴的な数値演算の例を紹介します。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1．基本的な数値リテラルと型**
    Pythonで利用できる数値型が整数型（int）と浮動小数点型（float）の2種類であることは前述の通りです。動的型付けされた変数がどの型を持つかは、type() 関数で確認できます。
    """)
    return


@app.cell
def _():
    _a = 1  # aに1を代入（a は整数型の変数として自動的に定義される）
    _x = 1.0  # xに1.0を代入（x は浮動小数点型の変数として自動的に定義される）
    print(f'a = {_a}', type(_a))
    print(f'x = {_x}', type(_x))  # aの型を表示  # xの型を表示
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    また、C言語などでは扱うことのできる整数型のサイズが限られているのに対し、Pythonでは整数型のサイズに制限はありません（多倍長整数）。そのため、Pythonでは整数型の変数に大きな値を代入することができます。
    """)
    return


@app.cell
def _():
    _a = 123456789012345678901234567890
    _a = _a ** 10
    print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    一方で、浮動小数点型（float）は、C言語などと同様に、倍精度（64ビット）の浮動小数点数として扱われます。したがって、Python でも計算機イプシロン（機械イプシロン）が存在します。計算機イプシロンは $1+\epsilon \neq 1$ となる最小の正の値であり、Python では、以下のように確認できます。
    """)
    return


@app.cell
def _():
    import sys
    print(sys.float_info.epsilon)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    また、実数を浮動小数点数として扱うため、Pythonでも実数の扱いでは誤差を生じます。例えば、以下のように、0.1を10回足しても、その値は1.0にはなりません。
    """)
    return


@app.cell
def _():
    _x = 0.0
    for _i in range(10):
        _x += 0.1
    print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **2．Pythonでのいくつかの特殊な数値演算**
    このようにPythonでも実数を扱う場合には、誤差が生じることに注意する必要があります。しかし、Pythonにはより正確に実数を扱うための機能がいくつかあります。
    上記の例では、0.1を10回足しても、その値は 1.0になりませんでした。これは、0.1を有限桁の2進数で表現できないことが原因です。Pythonでは、このような有限桁の2進数で表現できない実数を扱うために、decimalモジュールを利用できます。decimalモジュールでは、有限桁の10進数で実数を扱うことができます。以下の例では、数値を Decimal として扱うことで、0.1を10回足した値が正しく 1.0 になっています。
    """)
    return


@app.cell
def _():
    from decimal import Decimal
    _x = Decimal('0.0')
    for _i in range(10):
        _x += Decimal('0.1')
    print(_x)
    return (Decimal,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    さらに別の例を見てみましょう。Decimal() を利用することで、有限桁の10進数を正確に扱うことができましたが、Decimal オブジェクト同士の演算は正しく行われるとは限りません。例えば、以下の例では、Decimal オブジェクト同士の演算結果が正しくないことがわかります（$\frac{1}{99}$ の逆数は 99）。
    """)
    return


@app.cell
def _(Decimal):
    print(1/(1/99))
    print(Decimal('1')/ (Decimal('1')/Decimal('99')))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    このような整数同士の比として表現できる有理数を扱う場合は、Fraction オブジェクトとして扱うことができます。以下の例では、Fraction オブジェクトによって有理数の演算が正しく行われているます。
    """)
    return


@app.cell
def _():
    from fractions import Fraction
    _x = Fraction('0.1') + Fraction('0.1') + Fraction('0.1')
    print(_x)
    print(float(_x))
    y = Fraction('1.0') / (Fraction('1.0') / Fraction('99.0'))
    print(y)
    print(float(y))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    その他、Python では、複素数を扱うための機能も用意されています。複素数は、実数と虚数の積で表されます。例えば、以下のように、複素数を表す文字列を complex() 関数に渡すことで、複素数を扱うことができたりします。
    """)
    return


@app.cell
def _():
    import cmath
    _a = 1 + 2j
    b = 3 + 4j
    print(_a.real, _a.imag)
    print(b.real, b.imag)
    print(_a + b)
    return


if __name__ == "__main__":
    app.run()
