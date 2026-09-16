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
    # **Python のデータ型：数・文字列・リスト**
    ## **はじめに**
    ここでは、Python の 3 つの基本的なデータ型「数」「文字列」「リスト」の骨子を、C 言語と比べながら確認します。
    書き方の詳細は paiza ラーニング「新・Python入門編」で学び、ここでは**動かして確かめる**ことを目的にしてください。

    | Python | C 言語 | 内容 |
    |---|---|---|
    | `int`, `float` | `int`, `double` | 数 |
    | `str` | `char[]` | 文字列 |
    | `list` | 配列（`int[]` など） | 要素の並び |

    このノートブックのコードセルでは、`_a` のように先頭に `_` を付けた変数名を使っています。
    marimo では同じ変数を複数のセルで定義できないため、セル内だけで使う一時的な変数にはこの書き方をします。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **数（`int` 型・`float` 型）**
    整数は `int`、実数（浮動小数点数）は `float` です。C 言語の `int` と `double` に対応します。
    """)
    return


@app.cell
def _():
    _a = 12
    _x = 3.14
    print(_a, type(_a))
    print(_x, type(_x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    C 言語の `int` は 32 ビット環境で -2147483648 〜 2147483647 の範囲しか扱えませんが、Python の `int` には**桁数の上限がありません**。

    **試してみよう**: `range(10)` を `range(20)` にしても、桁あふれせずに計算できます。
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
    C 言語には無い演算子として、べき乗の `**` と整数の割り算 `//` があります。`/` は常に `float` を返します。
    """)
    return


@app.cell
def _():
    print(2 ** 10)          # べき乗
    print(7 / 2)            # 3.5  （/ は常に float）
    print(7 // 2, 7 % 2)    # 3 1  （整数の商と余り）
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **文字列（`str` 型）**
    C 言語では文字列を `char` の配列と終端文字 `'\0'` で表しましたが、Python には文字列そのものを表す `str` 型があります。
    リテラルはシングルクォート `'` かダブルクォート `"` で囲みます。終端文字は不要です。

    `+` で連結、`*` で繰り返しができます。C 言語の `strcat()` などを呼ぶより簡潔です。
    """)
    return


@app.cell
def _():
    _s1 = 'Hello, my '
    _s2 = 'Python!!'
    print(_s1 + _s2)            # + で連結
    print(_s1 * 3 + _s2 * 2)    # * で繰り返し
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    添字 `[ ]` で 1 文字を取り出せます。C 言語の配列と同じく先頭が 0 です。
    Python では**負の添字**が使え、`-1` が末尾の文字を指します。長さは `len()` で得られます。

    **試してみよう**: `text[14]` のように範囲外を指定するとどうなるでしょうか（C 言語なら何が起きるか思い出してください）。
    """)
    return


@app.cell
def _():
    text = 'Hello, Python!'
    print(text[0], text[1], text[-1])   # H e !
    print(len(text))                    # 14
    return (text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **リスト（`list` 型）**
    要素の並びを扱う型です。C 言語の配列に相当しますが、**長さが可変**で、要素の追加・削除ができます。
    リテラルは角括弧 `[ ]` で囲み、要素をカンマで区切ります（C 言語の初期化子 `{ }` とは違うので注意）。

    添字・負の添字・`len()` は文字列と同じように使えます。要素への代入もできます。
    """)
    return


@app.cell
def _():
    nums = [1, 2, 3, 4, 5]
    print(nums[0], nums[-1])   # 1 5
    print(len(nums))           # 5
    nums[2] = 99               # 要素の書き換え
    print(nums)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `append()` で末尾に追加できます。「空のリストを作り、`for` で回しながら追加する」は課題でよく使う形です。
    """)
    return


@app.cell
def _():
    squares = []
    for _i in range(5):
        squares.append(_i * _i)
    print(squares)             # [0, 1, 4, 9, 16]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `for` はリストの要素を**順に取り出す**構文です。C 言語のように添字で回す必要はありません。
    """)
    return


@app.cell
def _():
    fruits = ['Apple', 'Banana', 'Orange']
    for _f in fruits:
        print(_f)
    return (fruits,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    逆順にする方法は 3 つあります。**元のリストを変えるかどうか**が違います。

    | 書き方 | 元のリスト | 用途 |
    |---|---|---|
    | `reversed(a)` | 変わらない | `for` で逆順に回すとき |
    | `a[::-1]` | 変わらない | 逆順の**新しいリスト**が欲しいとき |
    | `a.reverse()` | **逆順に書き換わる** | そのリスト自体を逆順にしたいとき |

    **試してみよう**: 最後の `print(fruits)` を見て、`reverse()` だけが元のリストを変えていることを確かめてください。
    """)
    return


@app.cell
def _(fruits):
    for _f in reversed(fruits):      # 逆順に取り出す（fruits はそのまま）
        print(_f)
    print(fruits[::-1])              # 逆順の新しいリスト（fruits はそのまま）
    print(fruits)                    # ['Apple', 'Banana', 'Orange']

    _copy = list(fruits)             # コピーを作ってから
    _copy.reverse()                  # そのものを逆順に書き換える
    print(_copy)                     # ['Orange', 'Banana', 'Apple']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **スライス — 範囲を指定して取り出す**
    添字の代わりに `開始:終了:刻み` を書くと、その範囲を新しいリスト（または文字列）として取り出せます。
    **終了の位置は含みません**（`range()` と同じ感覚です）。開始・終了・刻みはどれも省略できます。

    | 書き方 | 意味 |
    |---|---|
    | `a[2:5]` | 添字 2, 3, 4 |
    | `a[2:]` | 添字 2 から最後まで |
    | `a[:5]` | 最初から添字 4 まで |
    | `a[::2]` | 全体を 1 つおきに |
    | `a[::-1]` | 全体を**逆順**に |

    **試してみよう**: `a[1:-1]` は何が取り出せるでしょうか。`a[::3]` は？
    """)
    return


@app.cell
def _():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a[2:5])      # [3, 4, 5]
    print(a[2:])       # [3, ..., 10]
    print(a[:5])       # [1, 2, 3, 4, 5]
    print(a[::2])      # [1, 3, 5, 7, 9]
    print(a[::-1])     # [10, 9, ..., 1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    スライスは文字列にもそのまま使えます。**文字列を逆順にする `s[::-1]`** や **n 文字おきに取り出す `s[::n]`** は今回の課題で使います。
    """)
    return


@app.cell
def _(text):
    print(text[7:13])   # Python
    print(text[::2])    # Hlo yhn
    print(text[::-1])   # !nohtyP ,olleH
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **入力をリストにする**
    課題では「1 行に空白区切りで並んだ数」を読むことがよくあります。`split()` で空白で分割し、`map(int, ...)` で各要素を整数にし、`list()` でリストにします。
    このセルは入力を受け取れないので、`input()` の代わりに文字列を直接置いています。
    """)
    return


@app.cell
def _():
    _line = '3 1 4 1 5'                 # input() で読んだ 1 行のつもり
    _nums = list(map(int, _line.split()))
    print(_nums)                        # [3, 1, 4, 1, 5]
    print(sum(_nums), max(_nums), min(_nums))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## **発展（課題では使わない）**
    以下は Python のデータ型についての補足です。読み飛ばして構いません。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **`float` の誤差と `Decimal`**
    計算機は 0.1 のような小数を正確に表せないため、`0.1` を 10 回足しても `1.0` になりません。正確な 10 進計算が必要なときは `Decimal` を使います。
    """)
    return


@app.cell
def _():
    _a = 0
    for _i in range(10):
        _a = _a + 0.1
    print(_a)                    # 0.9999999999999999

    from decimal import Decimal
    _d = Decimal('0')
    for _i in range(10):
        _d = _d + Decimal('0.1')
    print(_d)                    # 1.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **複素数**
    虚数単位は `j` で書きます。`complex` 型として四則演算ができます。
    """)
    return


@app.cell
def _():
    _c1 = 2 + 3j
    _c2 = 3 + 4j
    print(_c1 + _c2, _c1 * _c2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **要素の削除**
    `pop()` は取り出して返す、`remove()` は値を指定して消す、`del` は添字やスライスで消す、と使い分けます。
    """)
    return


@app.cell
def _():
    _b = [10, 20, 30, 40, 50]
    _last = _b.pop()        # 末尾を取り出す（戻り値あり）
    print(_last, _b)        # 50 [10, 20, 30, 40]
    _b.remove(20)           # 値 20 を消す
    print(_b)               # [10, 30, 40]
    del _b[0]               # 添字 0 を消す
    print(_b)               # [30, 40]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **型の混在**
    Python のリストには異なる型の要素を混ぜられますが、扱いにくくなるので推奨されません。
    以下のセルで `# ` を外して実行すると、`int` と `str` の足し算で `TypeError` になります。
    """)
    return


@app.cell
def _():
    mixed = [1, 2, 3, 'Apple', 'Banana']
    _sum = 0
    # for _i in mixed:
    #     _sum = _sum + _i         # ← TypeError
    for _i in mixed:
        if type(_i) is int:      # 型を確かめてから足す
            _sum = _sum + _i
    print(_sum)                  # 6
    return


if __name__ == "__main__":
    app.run()
