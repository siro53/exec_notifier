# exec_notifier
プログラムの実行の開始/終了をslackに通知するコマンドツール。

<img width=400 src="https://i.imgur.com/ySucvpK.png">

## 環境構築
1. `pip3 install -r requirements.txt` で依存パッケージをインストールする。

2. `config.py` の `SLACK_WEBHOOK_URL` に incoming webhook url を追記する。
    1.  [ここ](https://slackbot-test-shiro.slack.com/apps/A0F7XDUAZ--incoming-webhook-?next_id=0&tab=settings)にアクセスし、右上のプルダウンタブから通知したい slack のワークスペースを指定して「Slackに追加」を選択。
    2. 「チャンネルの投稿」という項目から、bot を追加したいワークスペースのチャンネルを指定し、「Incoming Webhook インテグレーションの追加」を選択。
    3. 「Webhook URL」という項目にあるURLをコピーし、`config.py` の `SLACK_WEBHOOK_URL` にコピペする。

## 使い方

```
usage: main.py [-h] [-dpath DEFAULT_OUTPUT_PATH] [-epath ERROR_OUTPUT_PATH] commands

プログラムの実行をslackに通知するコマンドラインツール.

positional arguments:
  commands              実行したいプログラムのコマンドを指定する. ex) "python3 main.py", "./a.out"

optional arguments:
  -h, --help            show this help message and exit
  -dpath DEFAULT_OUTPUT_PATH, --default_output_path DEFAULT_OUTPUT_PATH
                        標準出力をファイルに書き込む場合は、この引数にそのファイルのパスを指定する. 指定しない場合はターミナルに出力される.
  -epath ERROR_OUTPUT_PATH, --error_output_path ERROR_OUTPUT_PATH
                        エラー出力をファイルに書き込む場合は、この引数にそのファイルのパスを指定する. 指定しない場合はターミナルに出力される.
```

↑は `python3 main.py -h` を実行することで見ることも出来ます。

(例)
    
`exec_notifier` ディレクトリ内で、
```
$ python3 main.py "<実行したいコマンド>"
```
を実行する。
