# ex6 — スレッドとネットワーク通信の暗号化

## 小テスト {: .exercise }

小テストは 4 講時の講義パートのあとに行います。問題は前回の aiJudge 課題の内容に沿っています。受験できるのは **1-608 の教室だけ**で、オンラインでは受験できません。

**16:30〜16:45** の 15 分間で、aiJudge の次の課題に取り組んでください。

<!-- aijudge:begin test6 -->
- statusCode.py
<!-- aijudge:end -->

## 演習課題 {: .exercise }

### 演習課題 1. aiJudge の ex6 に取り組む {: .exercise }

aiJudge の ex6 にある次の課題すべてで、**満点を取って**ください。

<!-- aijudge:begin ex6 -->
- httpThreadServer.py
- httpThreadServer3.py
<!-- aijudge:end -->

スレッドの使い方は [thread.py](https://github.com/sanoakr/rumath-network/blob/main/samples/thread.py) を参考にしてください（読み方はこのページの[メモ](#thread-py)）。
aiJudge は、提出されたサーバに 1 つ目のクライアントを接続したまま待たせ、その間に 2 つ目のクライアントから要求を送ります。
aiJudge は、2 つ目の要求に応答が返ってくるか、つまりサーバが要求を並列に処理できているかを採点します。

## メモ：thread.py を読む {: #thread-py }

[thread.py](https://github.com/sanoakr/rumath-network/blob/main/samples/thread.py) は、同じ関数を「順に呼び出す」場合と「スレッドで動かす」場合を比べるサンプルです。

### 3 つの関数

```python
def f1():
    for i in range(Repeat):
        print("f1", i)
        sleep(0.5)
```

- `f1()` は `f1 0`〜`f1 4` を 0.5 秒おきに表示します（`Repeat = 5`）。`f2()` は 0.4 秒おきです
- `fx(n)` は、引数で受け取った `n` 秒おきに表示します。`fx(1)` は 1 秒おき、`fx(2)` は 2 秒おきです
- `sleep()` で待っている間、プログラムは何もしていません。サーバが `accept()` や `recv()` で相手を待っている状態と同じです

### 前半: 順に呼び出す

```python
f1()
f2()
fx(1)
fx(2)
```

1 つの関数が終わってから、次の関数が始まります。出力は `f1` の 5 行、`f2` の 5 行、… の順に並び、毎回同じです。
かかる時間は、それぞれの待ち時間の合計で、約 19.5 秒（2.5 + 2 + 5 + 10）です。

### 後半: スレッドで動かす

```python
thread1 = threading.Thread(target=f1)
thread1x = threading.Thread(target=fx, args=(1,))
...
thread1.start()
...
print("### end threads???")
thread1.join()
...
print("### end threads!!!")
```

- `threading.Thread(target=関数, args=引数のタプル)` で、関数を別のスレッドで動かす準備をします
    - `target=f1` のように、**関数そのもの**を渡します。`target=f1()` と書くと、その場で `f1` を呼び出してしまい（スレッドではなく、普通の呼び出しになる）、スレッドには戻り値の `None` が渡ります
    - `args=(1,)` の**カンマ**は必要です。`(1)` はただの整数 1 で、タプルになりません。`args=(1)` と書くと、スレッドの中で `TypeError: ... argument after * must be an iterable, not int` が発生します
- `start()` でスレッドが動き始めます。呼び出した側は終わりを待たずに、すぐ次の行へ進みます
    - そのため、`### end threads???` は、スレッドがまだ動いている途中で表示されます。`???` は「本当に終わった？」という意味です
- `join()` は、そのスレッドが終わるまで待ちます。4 つすべてを `join()` してから表示するので、`### end threads!!!` は本当に全部が終わった後に表示されます

4 つのスレッドは同時に待つので、かかる時間は一番長い `fx(2)` の約 10 秒です。前半の約 19.5 秒より短くなります。
計算が速くなったのではなく、**待ち時間を重ねた**ことで短くなっています（第 6 回のスライド「スレッドで気をつけること」）。

### 実行結果の読み方

後半の出力は、たとえば次のようになります。**順番は実行のたびに変わります。**

```
### start threads
f1f2fx  fx0
 2 0
 1 00

### end threads???
f2 1
f1 1
f2 2
fx 1 1
...
fx 2 4
### end threads!!!
```

- `f1` と `f2` と `fx` の行が混ざって表示されます。どのスレッドが先に動くかは OS が決めるので、決まった順番はありません
- `f1f2fx  fx0` のように、**1 行の中で文字が混ざる**ことがあります。`print("f1", i)` は、`f1`・区切りの空白・`0`・改行を別々に書き出すので、その間に別のスレッドの `print()` が割り込むためです
    - 複数のスレッドが同じもの（ここでは画面）を同時に使うと、こうした混ざりが起きます

### 試してみよう

1. 何回か実行して、後半の順番が毎回変わることを確かめる
2. `join()` の 4 行を消して実行する。`### end threads!!!` が、スレッドの途中ですぐに表示されることを確かめる（プログラム自体は、すべてのスレッドが終わるまで終了しません）
3. `httpThreadServer.py` では、`f1` の代わりに 1 つの接続を処理する関数を、`args` に `(conn, addr)` を渡してスレッドで動かします

    ```python
    th = threading.Thread(target=httpResponse, args=(conn, addr))
    th.start()
    ```
