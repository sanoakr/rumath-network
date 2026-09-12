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
    # Python の関数
    ## はじめに
    ここでは、Python の関数について概観します。関数という概念自体は、C言語のものと大きな違いはありませんが、動的型付け言語である Python では、関数の引数や戻り値の型を指定する必要がありません。その他にも、Python の関数にはC言語の関数にはない特徴があります。ここでは、Python の関数の定義や呼び出し方、引数の渡し方、戻り値の受け取り方などについて説明します。より詳しい内容は、本日の演習課題や公式マニュアルなどを通して学んで下さい。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 関数の定義と呼び出し
    Python の関数は、**def** キーワードによって定義されます。
    以下は、2つの引数の和を返す add 関数の定義です。Python ですので、インデントブロックによって関数の中身が定義されます。
    """)
    return


@app.function
def add(a, b):
    return a + b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C言語と異なり、関数の引数の型や戻り値の型を指定する必要はありません。この関数 add() の呼び出し方法は C言語と同様です。
    """)
    return


@app.cell
def _():
    a = 2
    b = 3
    print(add(a, b))
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ただし、Python では自動で型付けが行われるため、関数の引数には、数値以外の型の値を渡すことができます。以下の例では、文字列を引数に渡していますが、Python では文字列の加算が定義されているので、文字列の連結が行われます。
    """)
    return


@app.cell
def _():
    s1 = 'Hello '
    s2 = 'Python!'
    print(add(s1, s2))
    return (s1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    加算が定義されていない型の値を引数に渡すとエラーになります。引数や返り値の型を把握するのはプログラマの責任です。
    """)
    return


@app.cell
def _(a, s1):
    print(add(a, s1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    もちろん、引数の型の一致をチェックする関数を定義することも可能です（ノートブックでは同じ名前の関数を別のセルで定義し直せないので、ここでは add_checked() という別の名前にします）。
    """)
    return


@app.cell
def _(a, s1):
    def add_checked(a, b):
        if type(a) == type(b):
            return a + b
        else:
            return 'Type missmatch!'
    print(add_checked(a, s1))
    return (add_checked,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    リストを渡すことも可能です。
    """)
    return


@app.cell
def _(add_checked):
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(add_checked(l1, l2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    その他にも、Python の関数では複数の戻り値を返したりもできます。
    """)
    return


@app.cell
def _():
    def calc(a, b):
        return a+b, a-b, a*b, a/b

    wa, sa, seki, jo = calc(2,3)
    print(wa, sa, seki, jo)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## デフォルト引数値
    Python の関数定義では、引数にデフォルトの値を設定することができます。デフォルトの値を設定した引数は、呼び出し時に引数指定を省略することができます。以下の関数 greet() では、引数 lang と n にデフォルト値が設定されています。この関数を呼び出すときには、引数 n、または、lang と n を省略することができます。
    """)
    return


@app.cell
def _():
    def greet(greeting, lang='Python', n=1):
        return greeting + ' ' + lang + '!' * n

    print(greet('Hello'))
    print(greet('Hello', 'World'))
    print(greet('Hello', 'World', 7))
    return (greet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## キーワード引数
    ここまでの関数定義では、C言語と同様に関数定義と呼び出しの引数の順番が一致している必要がありました。しかし、Python では、関数をキーワード指定して呼び出すことができます。デフォルト引数値で定義した関数 greet() をキーワードを用いて呼び出してみましょう。
    """)
    return


@app.cell
def _(greet):
    print(greet(greeting='Hi!', n=3, lang='Python'))
    print(greet(n=9, greeting='Hi!'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1つ目の呼び出しでは、引数 lang と n の順番を入れ替えていますが、キーワード指定することで正しく引数が与えられています。2つ目の呼び出しでは、引数 lang だけを省略してデフォルト値を使っています。Python の関数呼び出しでは、このように引数をキーワード指定して呼び出すことで引数の順番を気にする必要がなくなります。

    C言語の関数呼び出しでは、引数の順番を間違えるとエラーやバグの原因になります。一方で、Python では引数も動的に片付けされるため、引数の順番を間違えても必ずしもエラーにはなりません。したがって、引数のキーワード指定を用いることで引数の対応付けを明確にすることができ、エラーやバグを予防することができます。
    """)
    return


if __name__ == "__main__":
    app.run()
