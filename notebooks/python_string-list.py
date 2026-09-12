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
    # Python のデータ型：数・文字列・リスト
    ## はじめに
    ここでは、Pythonの3つの基本的で重要なデータ型「数」「文字列」「リスト」について概観します。より詳しい内容は、本日の演習課題を通して学んで下さい。

    「数」では、整数 int型と実数 float型について説明します。C言語での int型と double型にそれぞれ対応します。

    「文字列」では、文字列を扱う string型について説明します。C言語での文字型配列 char[]がこれに対応します。

    「リスト」では、1次元の要素の並びを扱う list型について説明します。C言語での int[] や char[] などの配列変数に対応しますが、動的型付けをもつ Python では1つのリスト型に異なる型の要素を含むことができます。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 数（int型・float型）
    Python で数を扱うための基本的なデータ型は以下の2つです。
    1. 整数型 int
    1. 浮動小数点型（実数型） float

    それぞれ、C言語での int型と double型に対応します。
    """)
    return


@app.cell
def _():
    _a = 12
    print(_a)
    print(type(_a))
    _x = 3.14
    print(_x)
    print(type(_x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C言語では、int型が保持できる整数の範囲は、-2147483648 から 2147483647 までです(32ビット環境の場合）。Python の int型は、この範囲を超える整数を保持することができます。
    """)
    return


@app.cell
def _():
    _a = 3
    for _i in range(10):
        _a = _a ** 2
        print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    また、C言語と同様に整数型と浮動小数点型を含む演算は、自動的に浮動小数点型に変換されて計算されます。
    """)
    return


@app.cell
def _():
    _a = 123
    _x = 4.56
    print(type(_a), type(_x))
    y = _a + _x
    print(type(y), y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C言語にはない演算子としては、べき乗を表す ** や、整数の割り算を表す // があります。
    """)
    return


@app.cell
def _():
    print(2 ** 10)
    print(10 // 3, 10 % 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ここでは詳しく説明しませんが、Pythonでは他にも標準で用意されている数値型があります。たとえば、10進数を正確に表現できる Decimal型や、複素数を扱う complex型などです。
    """)
    return


@app.cell
def _():
    # 計算機は浮動小数点数を正確に扱えないため、0.1 を 10 回足しても　1 にならないが、
    _a = 0
    for _i in range(10):
        _a = _a + 0.1
    print(_a)
    from decimal import Decimal
    # Decimal を使うと、正確に計算できる
    _a = 0
    for _i in range(10):
        _a = _a + Decimal('0.1')
    print(_a)
    return


@app.cell
def _():
    # 複素数, 虚数単位は j
    c1 = 2 + 3j
    c2 = 3 + 4j
    print(type(c1), type(c2))
    print(c1 + c2)
    print(c1 * c2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 文字列（string型）
    C言語で文字列を扱う場合、文字型配列 char[] と文字列の終わりを表すヌル文字 '\0'（終端文字） を用いて文字列を表現しました。Pythonでは、文字列を表すための string型が用意されています。

    文字列を表すリテラルは、シングルクォート ' かダブルクォート " で囲みます。文字列の終わりを表すヌル文字は不要です。
    """)
    return


@app.cell
def _():
    _s1 = 'Hello'
    _s2 = 'Python'
    print(type(_s1), type(_s2))
    print(_s1, _s2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    文字列リテラルは、三連引用符 \"\"\" で囲むこともできます。改行文字を含む長い文字列を表現するのに便利です。
    """)
    return


@app.cell
def _():
    s = '''Good morning Python
    Hello Python
    Good night Python'''
    print(s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    string型は、文字列の結合や繰り返しを演算として表現することができます。C言語で、文字列操作関数（string.h の strcat() など）を呼び出していたことに比べると、とても簡潔に文字列を扱うことができます。
    """)
    return


@app.cell
def _():
    _s1 = 'Hello, my '  # 文字列リテラルは勝手に連結される
    _s2 = 'Python!!'
    print(_s1 + _s2)
    print(_s1 * 3 + _s2 * 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    また、文字列の一部を取り出すための添字演算子 [] も用意されています。C言語で、文字列を文字型配列として扱っていたときと同様の添字演算が可能です。これは Python のリストとも共通の機能です。リストについては次の節で説明します。
    """)
    return


@app.cell
def _():
    text = 'Hello, Python!'
    print(text[0])
    print(text[1])
    print(text[2])
    print(text[-1])  # 負のインデックスは末尾からの位置
    return (text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    文字列の長さは、len() 関数で取得できます。
    """)
    return


@app.cell
def _(text):
    print(text)
    print(len(text))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## リスト（list型）
    Python では、1次元の要素の並びを扱う list型が用意されています。C言語で、配列変数を用いて1次元の要素の並びを扱っていたときと同様の機能を持ちます。

    list型のリテラルは、角括弧 [ ] で囲みます。要素の並びは、カンマで区切ります。C言語では、配列変数の初期化リテラルとして、要素の並びを波括弧 { } で囲むことが表現しました。Python の { } 表現は、他の型（辞書型や集合型）のリテラル表現となりますので注意が必要です。
    """)
    return


@app.cell
def _():
    l = [1, 2, 3, 4, 5]
    print(l)
    return (l,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    リストの要素へは、添字演算子 [] を用いてアクセスします。C言語で、配列変数を用いて1次元の要素の並びを扱っていたときと同様の機能を持ちます。

    Python で添字番号に負の数を指定すると、リスト末尾からの相対位置を指定したことになります。（C言語で添字番号に負の数を指定すると（大抵の場合）Segmentation fault などのエラーとなります。）

    また、string型と同様に、リストの長さは len() 関数で取得できます。
    """)
    return


@app.cell
def _(l):
    print(l[0], l[-1])  # 最初の要素と最後の要素
    for _i in range(len(l)):  # 0 から len(l) - 1 までのループ
        print(l[_i])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C言語と同様に要素への代入も可能です。
    """)
    return


@app.cell
def _():
    nums = [1, 2, 3, 4, 5]
    nums[2] = 99
    nums[-1] = 555
    print(nums)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    その他、Python のリストでは個別の要素のみではなく、スライスと呼ばれる範囲指定による要素の取り出しや代入も可能です。スライスでは、添字番号の代わりに、コロン : を用いて範囲を指定します。範囲指定は、開始位置:終了位置:ステップ という形式で指定します。開始位置と終了位置は省略可能です。ステップは省略すると 1 となります。ステップが負の値の場合、終了位置は開始位置よりも小さくなるように指定します。
    """)
    return


@app.cell
def _():
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums2[2:5])  # 2 から 4 までの要素
    print(nums2[2:])  # 2 から最後までの要素
    print(nums2[:5])  # 最初から 4 までの要素
    print(nums2[:])  # 全要素
    print(nums2[::2])  # 全要素を 2 つ飛ばしで
    print(nums2[::-1])  # 全要素を逆順に
    nums2[1:3] = [100, 200, 300]
    print(nums2)  # スライスに代入
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    このスライス記法は文字列にも適用できます。文字列のスライスは、文字列の一部を取り出すための機能です。
    """)
    return


@app.cell
def _():
    text2 = 'Hello, Python!'
    print(text2[2:5])  # 2 から 4 までの文字
    print(text2[2:])  # 2 から最後までの文字
    print(text2[:5])  # 最初から 4 までの文字
    print(text2[:])  # 全文字
    print(text2[::2])  # 全文字を 2 つ飛ばしで
    print(text2[::-1])  # 全文字を逆順に
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C言語では通常、配列変数のサイズは固定です。C言語で配列変数のサイズを変更しようとすると realloc() などの関数を用いて、メモリの再割り当てを行う必要があります。

    一方、Python のリストはサイズ可変です。リストのサイズを変更するには、append() などのメソッドを用いて要素を追加したり、pop() や del(), remove() などのメソッドを用いて要素を削除することができます。
    """)
    return


@app.cell
def _():
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums3.append(11)
    print(nums3)  # 末尾に追加
    nums3.pop(-2)
    print(nums3)  # 末尾から 2 番目の要素を削除
    nums3.remove(7)
    print(nums3)  # 7 を削除
    del nums3[1]
    print(nums3)  # 1 番目の要素を削除
    del nums3[1:4]
    print(nums3)  # 1 から 3 番目の要素を削除
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ここまででも、Python のリスト型はC言語の配列と比較して、柔軟な機能を持っていることがわかります。しかし、Python が動的型付けをもつ言語であることから想像されるように、実はリストの要素には、異なる型の要素を混在させることができます。これは、C言語の配列変数にはできないことです。

    ただし、1つのリストに異なる型を混在させると、バグの温床になったり、そのリストの要素を取り出す際に要素の型を判別する必要があります。要素の型が混在したリストを利用は、Python のプログラムを書く上であまり推奨されません。
    """)
    return


@app.cell
def _():
    li = [1, 2, 3, 4, 5]
    ls = ['Apple', 'Banana', 'Orange']

    # リストの連結
    list = li + ls
    print(list)
    return (list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    このような要素型が混在したリストに対して、以下のような処理を行うと、
    """)
    return


@app.cell
def _(list):
    _sum = 0
    for _i in list:
        _sum = _sum + _i
    print(_sum)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    数値と文字列の + 演算は定義されていないため、当然エラーとなります。したがって、こういった型のチェックが必要となります。Pythonでは、変数にどのような型が入っているかを把握するのはプログラマの責任です。
    """)
    return


@app.cell
def _(list):
    _sum = 0
    for _i in list:
        if type(_i) is int:
            _sum = _sum + _i
    print(_sum)
    return


if __name__ == "__main__":
    app.run()
