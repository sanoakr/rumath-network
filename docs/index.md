# ネットワーク及び演習 2026

**後期 金曜 4・5 限 ＠ 1-608**（担当: 佐野 彰）

[:fontawesome-brands-microsoft: Teams 科目チームを開く](https://teams.microsoft.com/l/team/19%3AhdLY9JyAjCPHaz7TKT_s27WitrXc9H3J61BfNoUVtEU1%40thread.tacv2/conversations?groupId=95ea40f3-3431-4f38-94f9-95bab4b39489&tenantId=23b65fdf-a4e3-4a19-b03d-12b1d57ad76e){ .md-button .md-button--primary }
[:material-gavel: aiJudge（オンラインジャッジ）を開く](https://judge.math.ryukoku.ac.jp/){ .md-button }

Python を使って、ソケット通信・HTTP・スレッドといったネットワークプログラミングの基礎を、
実際にクライアント／サーバを書きながら学びます。

!!! info "この科目での質問方法"
    詳しくは [この科目での質問方法](how-to-ask.md) を読んでください。
    質問は [Teams の科目チーム](https://teams.microsoft.com/l/team/19%3AhdLY9JyAjCPHaz7TKT_s27WitrXc9H3J61BfNoUVtEU1%40thread.tacv2/conversations?groupId=95ea40f3-3431-4f38-94f9-95bab4b39489&tenantId=23b65fdf-a4e3-4a19-b03d-12b1d57ad76e)の **「★ 質問用チャネル」** に投稿してください。
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

## 関連情報

### 環境構築

- [Python のインストール](setup/python-install.md)
- Visual Studio Code のインストール（中野）: [Windows](http://www602.math.ryukoku.ac.jp/Prog1/vscode-win.html) / [macOS](http://www602.math.ryukoku.ac.jp/Prog1/vscode-mac.html)

### ツール・サービス

- [aiJudge（オンラインジャッジ）](https://judge.math.ryukoku.ac.jp/) — 演習課題の提出・自動採点
    （[使い方ガイド](https://sanoakr.github.io/aijudge/student/)）
- [PC 画面のスクリーンショットを撮る](setup/screenshot.md)
- [PC のデスクトップ録画](setup/screen-recording.md)
- [Visual Studio Code と（日本語）文字コード](setup/vscode-encoding.md)
- [paiza ラーニングでクーポンコードを使う](setup/paiza-coupon.md)
- [GitHub Copilot の有効化・無効化](setup/github-copilot.md)

### 教材・ツール

- [教材ノートブック（marimo）](notebooks.md) — ブラウザ内で Python を実行しながら学べる
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
