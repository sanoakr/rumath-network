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
    # **Python 入門**
    ## **はじめに**
    この科目ではネットワークプログラミングのための言語として Python を利用します。 Python は、様々なプログラミング言語の中でも比較的簡単に学ぶことができる言語です。このノートブックでは、 Python の特徴を学びます。

    Python の特徴の一つとして、豊富な標準ライブラリ（C 言語の stdio.h のような言語の標準仕様に含まれている関数ライブラリ）を持っていることが挙げられます。標準ライブラリには、数値計算やタートルグラフィクスなど、さまざまな機能が含まれています。しかし、この科目で学ぶ内容は Python の基本的な文法とネットワークプログラミングに必要な最低限の内容に限定します。
    このノートブックのコードセルでは、`_a` のように先頭に `_` を付けた変数名を使っています。marimo では同じ変数を複数のセルで定義できないため、セル内だけで使う一時的な変数にはこの書き方をします（詳しくは「ノートブックとは」を参照）。

    Python のより広範な内容については、[Python の公式ドキュメントのチュートリアル](https://docs.python.org/ja/3.14/tutorial/index.html)や、[paizaラーニング](https://paiza.jp/works)などのオンラインコンテンツなどを利用して学習してください。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Python の位置付け**
    プログラミング言語には様々なものがありますが、 Python は現在もっとも人気のあるプログラミング言語の一つです。

    * [RedMonk Top 20 Languages Over Time: January 2026](https://redmonk.com/rstephens/2026/04/14/top20-jan2026/)（世界でどのくらい使われている？GithubとStackOverflowの質問数から算出）

        1.JavaScript, 2.**Python**, 3.Java, 4.PHP, 4.C#（同順位）

    * [PYPL PopularitY of Programming Language: Sept 2026](https://pypl.github.io/PYPL.html)（世界でどのくらい使われている？Google検索数から算出）

        1.**Python 52.08%(+22.7%)**, 2.Java 13.34%(-0.7%), 3.C/C++ 7.99%(-3.5%), 4.R 3.83%(-2.1%), 5.JavaScript 3.28%(-3.1%)

    * [「実際に仕事で使われているプログラミング言語」ランキング」](https://qiita.com/mmake/items/68cc8f07331e0ef8ce50)（日本国内中心にいろんな視点からのまとめ）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Python の特徴**
    Python の特徴を、みなさんが学んできた C 言語と比較しながら紹介したいと思います。ここでは Python の特徴として、
    1. インタプリタ型言語である
    1. 動的な型付け言語である
    1. インデントブロック構文をもつ

    について説明します。
    他にも、ガベージコレクション、オブジェクト指向、などなど、 C 言語と比較しても様々な特徴がありますがここでは取り扱いません。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **1. インタプリタ言語である**
    C 言語ではプログラムを実行する前に「コンパイル」によってソースコードを機械語に変換する必要がありました。この変換を行うプログラムをコンパイラと呼びます。コンパイラは、プログラムを機械語に変換する前に、プログラムの文法をまとめてチェックし、プログラムが正しければ機械語に変換してプログラムの実行ファイルを生成します。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$\fbox{C 言語ソースコード} \rightarrow \text{コンパイラ} \rightarrow \fbox{機械語実行ファイル} \rightarrow \text{実行}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    一方、 Python はコンパイルを行わずにプログラムを実行することができます。 Python のプログラムは、インタプリタと呼ばれるプログラムによってソースコードから直接実行されます。インタプリタは、ソースコードを逐次変換しながら実行します。したがって Python では、未定義の変数を使うといった誤りがあってもプログラムは動き始め、実行がその箇所に到達してはじめてエラーメッセージとともに停止します（文法の誤りは実行前に検出されます）。

    Python では実行ファイルを生成する必要がなく、ソースコードを編集したらそのまますぐに実行することができます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$\fbox{Python ソースコード} \rightarrow (\text{インタプリタ}) \rightarrow \text{実行}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **2. 動的な型付け言語である**
    C 言語では、変数には必ず型を宣言する必要がありました。変数の型を宣言することで、その変数がどのような値を扱うことができるかをコンパイラに伝えます。したがって、変数の型を宣言するとその変数には指定した型をもつ値しか代入することができません。変数の型を宣言することを変数の型付けと呼び、 C 言語のように変更できない形で変数型を宣言する言語を **静的な型付け言語** と呼びます。

    ```c
    int a = 1;          // aは整数型の変数
    double x = 1.0;     // xは実数型の変数

    a = 2.1;            // 整数型の変数に実数を代入：エラーにはならないが小数部が切り捨てられ a は 2 になる
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    一方、 Python では変数の型を宣言する必要がありません。変数の型は、変数に代入された値によって自動的に決定されます。 Python のように変数の型を明示的に宣言しない言語を **動的な型付け言語** と呼びます。

    以下の Python コードを実行して、変数の型を宣言しないこと、変数には既存の型と異なる型の値も代入できることを確認してみましょう。

    **試してみよう**: `a = 2.0` を `a = 'hello'` や `a = True` に変えると `type(a)` はどうなるでしょうか。
    """)
    return


@app.cell
def _():
    a = 1       # aに1を代入（a は整数型の変数として自動的に定義される）
    x = 1.0     # xに1.0を代入（x は浮動小数点型の変数として自動的に定義される）

    print(f'a = {a}', type(a))  # aの型を表示
    print(f'x = {x}', type(x))  # xの型を表示

    a = 2.0     # aに2.0を代入（a は浮動小数点型の変数として自動的に再定義される）
    x = 'abc'   # xに'abc'を代入（x は文字列型の変数として自動的に再定義される）

    print(f'a = {a}', type(a))  # aの型を表示
    print(f'x = {x}', type(x))  # xの型を表示
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    このように Python では、変数の型を宣言する必要がなく、変数にはどのような型の値でも代入することができます。これは便利な特徴ではありますが、一方で各変数にどのような型の値が入っているかはプログラムを書く人間がチェックしなければならず、プログラムのバグを生みやすいという欠点もあります。

    たとえば、以下の Python コードで、コメントアウトされている2回目の `a + b` の演算を実行すると、定義されていない「整数と文字列の足し算」が実行されようとしてエラーとなります。
    """)
    return


@app.cell
def _():
    _a = 1     # aに1を代入（a は整数型の変数として自動的に定義される）
    _b = 2     # bに2を代入（b は整数型の変数として自動的に定義される）
    print(f'a + b = {_a + _b}')  # a + b の計算結果を表示

    _b = 'abc' # bに'abc'を代入（b は文字列型の変数として自動的に再定義される）
    # print(f'a + b = {_a + _b}')  # ← この行の # を外して実行すると TypeError になる
    c = 'XYZ'
    print(_b + c)  # 文字列同士の + は連結
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **3. インデントによるブロック構文をもつ**
    C 言語では、if文やfor文などのブロック構文を表現するために、波括弧 `{` と `}` を使います。波括弧は、ブロック構文の開始と終了を表していました。

    ```c
    if (a > 0) {
        printf("aは正の数です。\n");
    }
    ```

    したがって、この C 言語のソースコードは以下のように書いてもまったく同じ意味になります。

    ```c
    if (a > 0) {printf("aは正の数です。\n");}
    ```

    あるいは、以下のように書いても同じです。

    ```c
    if (a > 0) {
    printf("aは正の数です。\n");
    }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    一方、 Python では、ブロック構文を表現するためにインデント（字下げ）を使います。 C 言語のソースコードでのインデントは、単なる読みやすさのためのものであり、実際にはインデントを入れても入れなくても同じ意味になります。

    しかし、 Python のインデントは、ブロック構文の開始と終了を表しています。
    たとえば、以下の Python コードは、上記の C 言語コードと同様に、if文のブロック構文の中にある print 文を実行します。
    """)
    return


@app.cell
def _():
    _a = 10
    if _a > 0:
        print('a は正の数です。')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python ではインデントがプログラムの「意味」を表現するため、インデントが正しくないとエラーになります。

    **試してみよう**: 以下のセルで `print` の行頭にある空白 4 つを消して実行してみてください。
    """)
    return


@app.cell
def _():
    _a = 10
    if _a > 0:
        print('a は正の数です。')   # ← この行の先頭の空白を消すと IndentationError
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `IndentationError: expected an indented block` — 「if ブロックの中身が無い」というエラーになったはずです。
    C 言語なら波括弧の中に何も無くてもコンパイルは通りますが、 Python ではインデントされた行が無いと文法として成立しません。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    入れ子になったブロック構文の場合、インデントの深さが増えます。たとえば、以下の Python コードは、for 文のブロックの中にある if 文のブロックの中の print 文を実行します。

    **試してみよう**: `range(10)` を `range(1, 6)` に、`i % 2` を `i % 3` に変えると出力はどう変わるでしょうか。
    """)
    return


@app.cell
def _():
    for i in range(10):
        if i % 2 == 0:
            print(f'{i}は偶数です。')
        else:
            print(f'{i}は奇数です。')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    これを C 言語で書くと以下のようになります。

    ```c
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) {
            printf("iは偶数です。\n");
        } else {
            printf("iは奇数です。\n");
        }
    }
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
