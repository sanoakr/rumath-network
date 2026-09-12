# ネットワーク及び演習 2026

**後期 金曜 4・5 限 ＠ 1-608**（担当: 佐野 彰）

Python を使って、ソケット通信・HTTP・スレッドといったネットワークプログラミングの基礎を、
実際にクライアント／サーバを書きながら学びます。

!!! info "この科目での質問方法"
    質問は Teams の科目チーム **「★ 質問用チャネル」** に投稿してください。
    他の受講者にも役立つ質問・回答は共有します。

## 講義内容と演習課題

各回のページは講義に合わせて順次公開します。

| 回 | 日付 | 内容（予定） | ページ |
|:--:|:--:|---|:--:|
| ex0 | — | （事前課題）Python プログラミング環境の準備 | [ex0](ex0.md) |
| ex1 | 09/18 | イントロと Python 入門 | [ex1](ex1.md) |
| ex2 | 09/25 | 計算機ネットワークの基礎、Python のデータ型 | 準備中 |
| ex3 | 10/02 | echo クライアント・サーバ、Python の関数 | 準備中 |
| ex4 | 10/09 | echoClient.py と echoServer.py を読む | 準備中 |
| ex5 | 10/16 | HTTP プロトコルと httpServer.py | 準備中 |
| ex6 | 10/23 | スレッドとネットワーク通信の暗号化 | 準備中 |
| — | 10/30 | お休み（龍谷祭・全学休講） | |
| ex7 | 11/06 | hey と HTTP サーバの負荷テスト | 準備中 |
| ex8 | 11/13 | まとめの小テスト ＠ 1-608 | 準備中 |

## 評価

演習 60%・小テスト 40% に、任意提出のレポート課題（第 8 回以降に案内）の評価を加えて科目評価とします。

## 関連情報

### 環境構築

- [Python のインストール](https://app.notion.com/p/Python-3a4108b3ef12408bbb7a34c90fd86716?pvs=21)
- Visual Studio Code のインストール（中野）: [Windows](http://www602.math.ryukoku.ac.jp/Prog1/vscode-win.html) / [macOS](http://www602.math.ryukoku.ac.jp/Prog1/vscode-mac.html)
- [VS Code で Jupyter 環境を構築](https://app.notion.com/p/VS-Code-Jupyter-f5da3200b013495c88d3e9aa5b176a85?pvs=21)
- [paiza ラーニングでクーポンコードを使う](https://app.notion.com/p/paiza-63b4f5a2d9c8477e9d15d3787dbdb7c6?pvs=21)
- [GitHub Copilot の有効化・無効化](https://app.notion.com/p/GitHub-Copilot-288f727ec89580d49ef4d509e9cc4af6?pvs=21)

### 教材・ツール

- [Jupyter Notebook 教材（このリポジトリ）](https://github.com/sanoakr/rumath-network) — `jupyter.ipynb`, `python_tutorial.ipynb` など
- [サンプルコード](https://github.com/sanoakr/rumath-network/tree/main/samples)
- [hey](https://github.com/rakyll/hey) — HTTP 負荷テストツール（第 7 回で使用）

### Python 3.13 ドキュメント

- [Python 3.13 ドキュメント](https://docs.python.org/ja/3.13/index.html)
    - [Python のセットアップと利用](https://docs.python.org/ja/3.13/using/index.html)
    - [Python チュートリアル](https://docs.python.org/ja/3.13/tutorial/index.html)
    - [組み込み関数](https://docs.python.org/ja/3.13/library/functions.html)
    - [sys --- システムパラメータと関数](https://docs.python.org/ja/3.13/library/sys.html)
    - [socket --- 低水準ネットワークインターフェース](https://docs.python.org/ja/3.13/library/socket.html)
    - [http.server --- HTTP サーバ](https://docs.python.org/ja/3.13/library/http.server.html)
    - [threading --- スレッドベースの並列処理](https://docs.python.org/ja/3.13/library/threading.html)
    - [turtle --- タートルグラフィックス](https://docs.python.org/ja/3.13/library/turtle.html)
