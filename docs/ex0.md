# ex0 — 事前課題: Python プログラミング環境の準備

この科目では、プログラミング言語として Python を使います。
**初回（9/18）までに**、このページを参考にして、自分の PC に Python のプログラミング環境を準備してください。

## Python のインストール（必須） {: .exercise }

Python の実行環境を用意してください。数理情報演習など、ほかのプログラミング科目ですでに
Python の環境を構築している場合は、その環境をそのまま使って構いません。
Python 3 の最新バージョンは 3.14 系です。この科目の内容は Python 3 であれば扱えるので、
最新バージョンでなくても構いません。

!!! tip "Python 2 と Python 3"
    Python には、2020 年にサポートが終了した Python 2 と、現行の Python 3 があります。
    使用するバージョンが **3 系** であることを確認してください。
    Windows PowerShell やターミナルなどの CUI で、`python`（または `python3`）コマンドを
    `--version` または `-V` オプションを付けて実行すると、使用している Python のバージョンを確認できます。

```console
$ python --version
Python 3.14.7
$ python -V
Python 3.14.7
```

Python は、WSL、Microsoft Store、Anaconda、Homebrew など、さまざまな方法でインストールできます。
Python の実行環境を使えるようになれば、どの方法でインストールしても構いません。

[python.org](https://www.python.org/) からインストールする方法を次のページで説明しています。
まだ環境を用意していない人は参考にしてください。

- [Python のインストール](setup/python-install.md)

## プログラミング用エディタの準備（必須） {: .exercise }

C 言語のときと同様に、Python のプログラムを書くためのテキストエディタを用意してください。
特にこだわりがなければ、C 言語のプログラミング科目でも使った Visual Studio Code を推奨します。

- Visual Studio Code のインストール（中野）: [Windows](http://www602.math.ryukoku.ac.jp/Prog1/vscode-win.html) / [macOS](http://www602.math.ryukoku.ac.jp/Prog1/vscode-mac.html)

!!! note "ノートブック環境の準備は不要です"
    この科目では、Python のコードを対話的に実行できるノートブック（marimo）を講義資料として使います。
    [教材ノートブック](notebooks.md) は科目 Web ページからブラウザで開くだけで実行できるので、
    ノートブック環境（Jupyter など）を自分の PC にインストールする必要はありません。
