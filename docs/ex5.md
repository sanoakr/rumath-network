# ex5 — HTTP プロトコルと httpServer.py

## 小テスト {: .exercise }

小テストは 4 講時の講義パートのあとに行います。問題は前回の aiJudge 課題の内容に沿っています。受験できるのは **1-608 の教室だけ**で、オンラインでは受験できません。

小テストの問題文には `echoClient4.py` のコードを載せてあります。**16:30〜16:45** の 15 分間で、aiJudge の次の課題に取り組んでください。

<!-- aijudge:begin test5 -->
- echoClient5.py
<!-- aijudge:end -->

## 演習課題 {: .exercise }

### 演習課題 1. aiJudge の ex5 に取り組む {: .exercise }

aiJudge の ex5 にある次の課題すべてで、**満点を取って**ください。

<!-- aijudge:begin ex5:httpServer2,httpServer3 -->
- httpServer2.py
- httpServer3.py
<!-- aijudge:end -->

これらの課題のプログラムは、[httpServer.py](https://github.com/sanoakr/rumath-network/blob/main/samples/httpServer.py) をもとに作成してください。
動作を確認するときは、クライアント（[httpTestClient.py](https://github.com/sanoakr/rumath-network/blob/main/samples/httpTestClient.py) や Web ブラウザ）を自分で動かしてください。
aiJudge は、提出されたプログラムをサーバとして起動し、httpTestClient.py からアクセスして採点します。

!!! note "server.html と HTML ファイルの文字コード"
    動作確認に使う [server.html](https://github.com/sanoakr/rumath-network/blob/main/samples/server.html) は、GitHub のページの「Download raw file」ボタンでダウンロードして、そのまま使ってください。server.html は文字コード UTF-8 で保存してあり、httpServer.py も応答のヘッダで `charset=utf-8` を送ります。

    自分で HTML ファイルを作成する場合や、server.html を編集する場合は、文字コードを **UTF-8** にして保存してください。Windows の「ANSI」や Shift_JIS など、ほかの文字コードで保存すると、ブラウザで日本語が文字化けします。VS Code では、画面右下に表示される文字コードが `UTF-8` になっていることを確かめてください。

<!-- aijudge:begin ex5/paiza5 -->
### 認定証提出（paiza「新・Python入門編」23〜24） {: .exercise }

[paiza ラーニング](https://paiza.jp/works/) の講座
[「新・Python入門編」](https://paiza.jp/works/python/new-primer)
の、次の 2 つのレッスンに取り組み、各レッスンの「認定証」を取得してください。

- [「新・Python入門編 23: モジュールを理解しよう」](https://paiza.jp/works/python/new-primer/python-new-primer-23)
- [「新・Python入門編 24: 例外処理を理解しよう」](https://paiza.jp/works/python/new-primer/python-new-primer-24)

取り組み方は、「演習問題のみ」「コードと説明のみ読みながら」「動画も視聴しながら」から、自分のレベルに合わせて選んでください。

2 つのレッスンの認定証の画面キャプチャは、**まとめて 1 回で**この課題に提出してください。認定証に表示されるニックネームには、必ず自分の学籍番号を含めてください。

得点率は、提出に含まれる認定証が 2 レッスンのうち何レッスン分かで決まります（1 レッスンで 50%、2 レッスンで 100%）。

すべての演習問題をクリアしても認定証が表示されない場合は、最後の演習問題をもう一度クリアすると取得できます。
<!-- aijudge:end -->

## メモ：httpServer.py の setsockopt() について

サーバプログラムを続けて実行すると、次のようなエラーが表示され、サーバを起動できないことがあります。

```
OSError: [Errno 48] Address already in use
```

エラー番号は状況によって異なる場合があります。このエラーは、以前に実行したサーバプログラムが使ったアドレスとポートを、OS がプログラムの終了後すぐには解放せず、再利用できないために発生します。

この場合は、別のポート番号でサーバプログラムを実行すると、以前に使ったポートと衝突せずにサーバを起動できます。

また、作成したソケットに次のオプションを設定しても、この問題を回避できます。`httpServer.py` には、このオプションを設定済みです。

```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
```

!!! note "macOS でポート 5000 が使えないとき"
    macOS では「AirPlay レシーバー」がポート 5000 と 7000 を使っているため、これらのポートではサーバを起動できないことがあります。別のポート番号（5050 や 8080 など）を使ってください。
