import requests
import subprocess
import argparse
import emoji
from config import *


def send_msg(msg: str) -> None:
    requests.post(SLACK_WEBHOOK_URL, json={'text': msg})


def main() -> None:
    arg_parser = argparse.ArgumentParser(description='プログラムの実行をslackに通知するコマンドラインツール.')

    arg_parser.add_argument('commands', help='実行したいプログラムのコマンドを指定する. ex) "python3 main.py", "./a.out"')
    arg_parser.add_argument('-dpath', '--default_output_path', help="""
    標準出力をファイルに書き込む場合は、この引数にそのファイルのパスを指定する.
    指定しない場合はターミナルに出力される.
    """)
    arg_parser.add_argument('-epath', '--error_output_path', help="""
    エラー出力をファイルに書き込む場合は、この引数にそのファイルのパスを指定する.
    指定しない場合はターミナルに出力される.
    """)

    args = arg_parser.parse_args()

    commands = args.commands.split()
    default_output_path = args.default_output_path if args.default_output_path != None else 'ターミナル'
    error_output_path = args.error_output_path if args.error_output_path != None else 'ターミナル'
    result = subprocess.run(commands)

    send_msg(f"`{args.commands}` の実行を開始しました.")

    if result.returncode == 0:
        send_msg(f"""
        *プログラムは正常に終了しました.* {emoji.emojize(' '.join([':tada:' for _ in range(3)]), language='alias')}
        標準出力は {args.default_output_path if hasattr(args, 'default_output_path') else 'ターミナル'} に出力されました.
        エラー出力は {args.error_output_path if hasattr(args, 'error_output_path') else 'ターミナル'} に出力されました.
        """)
    else:
        send_msg(f"""
        *プログラムは異常終了しました.* {emoji.emojize(' '.join([':scream:' for _ in range(3)]), language='alias')}
        標準出力は {default_output_path} に出力されました.
        エラー出力は {error_output_path} に出力されました.
        """)

if __name__ == '__main__':
    main()