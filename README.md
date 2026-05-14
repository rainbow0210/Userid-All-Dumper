# Discord_Userid-All-Dumper

# Japanese
# 概要
Discord 上で動作する Bot です。サーバー内メンバーのユーザー名と ID を CSV ファイルとして出力します。

# 使用技術
- 言語: Python
- ライブラリ/フレームワーク: discord.py, python-dotenv
- データベース: なし
- その他: Discord Bot, CSV, dotenv

# 使い方
## 前提条件
- Python 3.10.10 以上
- Discord Bot のトークン
- Discord サーバーでメンバー情報を取得できる権限
- Bot アプリで Members Intent を有効化していること

## インストール方法
```bash
git clone https://github.com/rainbow0210/Userid-All-Dumper.git
cd Userid-All-Dumper
pip install discord.py python-dotenv
```

## 基本的な使い方
1. プロジェクトルートに `.env` ファイルを作成し、Bot トークンを設定します。

```env
token=YOUR_BOT_TOKEN
```

2. Bot を起動します。

```bash
python main.py
```

3. Discord でスラッシュコマンドを実行します。

```bash
/member_dump
```

Bot を除外して出力したい場合は、次のコマンドを使用します。

```bash
/user_dump
```

# 主な機能
- サーバー内メンバーの名前と ID を CSV に出力します。
- Bot を除外したユーザー一覧を CSV に出力できます。
- 生成した CSV はそのまま Discord に添付ファイルとして返します。
- スラッシュコマンドのみで操作できます。

# 設定
`.env` に Bot トークンを設定してください。

```env
token=YOUR_BOT_TOKEN
```

補足:
- `main.py` は `dotenv` で `.env` を読み込みます。
- メンバー一覧の取得には Discord 側で Members Intent の有効化が必要です。
- 出力ファイルは一時的に CSV を作成し、送信後に削除されます。

# 参考サイト

- discord.py | API Reference: https://discordpy.readthedocs.io/en/stable/api.html
- Python Get Member from User ID Discord.py: A Comprehensive Guide: https://copyprogramming.com/howto/python-get-member-from-user-id-discord-py-a-comprehensive-guide
- discord.pyでmembersが取れるようにする: https://qiita.com/izmktr/items/6667e5f9148c48e61da4
- サーバー内のメンバー数を取得【discord.py】: https://discordbot.jp/blog/3/
- python for文を初心者向けに解説！for文基礎はこれで完璧: https://udemy.benesse.co.jp/development/python-work/python-for.html
- 【Python入門】if文の論理演算子notの使い方をやさしく解説！: https://www.sejuku.net/blog/65070
- 【Python】リスト(list)をcsvへ出力する方法【csvモジュール、pandas】: https://python-academia.com/list-csv/
- discord.py V2のスラッシュコマンドを使えるようにする: https://qiita.com/Luapy/items/3abff9575e132e2955ec
- DiscordのBotでのファイル添付の仕方など【Python】: https://qiita.com/chatrate/items/aa6625f6663fa2ca33d6
- Pythonでファイル・ディレクトリを削除するos.remove, shutil.rmtreeなど: https://note.nkmk.me/python-os-remove-rmdir-removedirs-shutil-rmtree/
- teratail - リストをCSVに出力する際にエラーが発生しました。: https://teratail.com/questions/261502
- teratail - 【Python 】.csvファイルの書き込みが上手くいきません: https://teratail.com/questions/300532
- PythonでCSVファイルの文字コードを変換する方法【初心者向け】: https://magazine.techacademy.jp/magazine/21128

# ライセンス
MIT License

# English
## Overview
This bot runs on Discord and exports server member names and IDs to a CSV file.

## Technology Stack
- Language: Python
- Library/Framework: discord.py, python-dotenv
- Database: None
- Other: Discord Bot, CSV, dotenv

## Quick Start
### Requirements
- Python 3.10.10 or later
- A Discord bot token
- Permission to access member information in the Discord server
- Members Intent enabled for the bot application

### Installation
```bash
git clone https://github.com/rainbow0210/Userid-All-Dumper.git
cd Userid-All-Dumper
pip install discord.py python-dotenv
```

### Basic Usage
1. Create a `.env` file in the project root and set your bot token.

```env
token=YOUR_BOT_TOKEN
```

2. Start the bot.

```bash
python main.py
```

3. Run the slash command in Discord.

```bash
/member_dump
```

To export only non-bot users, use the following command.

```bash
/user_dump
```

## Main Features
- Exports server member names and IDs to CSV.
- Exports a CSV file containing only non-bot users.
- Returns the generated CSV as a Discord attachment.
- Operates only through slash commands.

## Configuration
Set your bot token in `.env`.

```env
token=YOUR_BOT_TOKEN
```

Notes:
- `main.py` loads `.env` with `dotenv`.
- Discord Members Intent must be enabled to retrieve member lists.
- The CSV file is created temporarily and deleted after it is sent.

## API Reference / Documentation
References used in this project:

- discord.py | API Reference: https://discordpy.readthedocs.io/en/stable/api.html
- Python Get Member from User ID Discord.py: A Comprehensive Guide: https://copyprogramming.com/howto/python-get-member-from-user-id-discord-py-a-comprehensive-guide
- discord.pyでmembersが取れるようにする: https://qiita.com/izmktr/items/6667e5f9148c48e61da4
- サーバー内のメンバー数を取得【discord.py】: https://discordbot.jp/blog/3/
- python for文を初心者向けに解説！for文基礎はこれで完璧: https://udemy.benesse.co.jp/development/python-work/python-for.html
- 【Python入門】if文の論理演算子notの使い方をやさしく解説！: https://www.sejuku.net/blog/65070
- 【Python】リスト(list)をcsvへ出力する方法【csvモジュール、pandas】: https://python-academia.com/list-csv/
- discord.py V2のスラッシュコマンドを使えるようにする: https://qiita.com/Luapy/items/3abff9575e132e2955ec
- DiscordのBotでのファイル添付の仕方など【Python】: https://qiita.com/chatrate/items/aa6625f6663fa2ca33d6
- Pythonでファイル・ディレクトリを削除するos.remove, shutil.rmtreeなど: https://note.nkmk.me/python-os-remove-rmdir-removedirs-shutil-rmtree/
- teratail - リストをCSVに出力する際にエラーが発生しました。: https://teratail.com/questions/261502
- teratail - 【Python 】.csvファイルの書き込みが上手くいきません: https://teratail.com/questions/300532
- PythonでCSVファイルの文字コードを変換する方法【初心者向け】: https://magazine.techacademy.jp/magazine/21128

## License
MIT License