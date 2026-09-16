# ex0 — 事前課題: Python プログラミング環境の準備

この科目ではプログラミング言語として Python を利用します。
**初回（9/18）までに**、以下を参考にして自分の PC 上に Python プログラミング環境を準備してください。

## Python のインストール（必須） {: .exercise }

Python の実行環境を用意してください。すでに数理情報演習など他のプログラミング科目で
Python 環境を構築済みの場合は、それをそのまま利用して構いません。
最新の Python3 のバージョンは 3.14 系ですが、この科目で扱う内容は Python3 であれば
必ずしも最新のバージョンでなくても大丈夫です。

!!! tip "Python 2 と Python 3"
    Python には、すでに 2020 年にサポートが切れている Python 2 と、現行の Python 3 があります。
    利用するバージョンが **3 系** であることを確認してください。
    Windows PowerShell やターミナルなどの CUI 上で、`python`（または `python3`）コマンドを
    `--version` や `-V` オプション付きで実行すると、利用している Python のバージョンを確認できます。

```console
$ python --version
Python 3.14.7
$ python -V
Python 3.14.7
```

Python は、WSL や Microsoft Store、Anaconda や Homebrew など様々な方法でインストールが可能です。
Python の実行環境が利用できれば、いずれの方法を利用しても構いません。

[python.org](https://www.python.org/) からのインストール方法を以下に説明していますので、
未整備の方は参考にしてください。

- [Python のインストール](setup/python-install.md)

## プログラミング用エディタの準備（必須） {: .exercise }

C 言語と同様に、Python プログラミングを行うためのテキストエディタを準備してください。
とくに拘りがなければ、C 言語プログラミング科目でも利用した Visual Studio Code を推奨します。

- Visual Studio Code のインストール（中野）: [Windows](http://www602.math.ryukoku.ac.jp/Prog1/vscode-win.html) / [macOS](http://www602.math.ryukoku.ac.jp/Prog1/vscode-mac.html)

!!! note "ノートブック環境の準備は不要です"
    この科目では、講義資料として Python コードをインタラクティブに実行できる**ノートブック**（marimo）を利用しますが、
    [教材ノートブック](notebooks.md) は科目 Web ページからブラウザで開くだけで実行できます。
    ノートブック環境（Jupyter など）を自分の PC にインストールする必要はありません。
