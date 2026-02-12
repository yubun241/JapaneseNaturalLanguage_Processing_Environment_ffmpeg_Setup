## Japanese Natural Language Processing Environment Setup (MeCab + Python)
pythonを使って日本語テキストを自然言語処理するための基本環境構築手順
形態素解析エンジン MeCab を Python から利用することを前提とし、必要な依存関係として FFmpeg の導入までを記載する。

## 必要環境
macOS / Linux / Windows
Python 3.9以上
MeCab
mecab-ipadic（標準辞書）または mecab-ipadic-NEologd
FFmpeg（音声 → テキスト変換などを行う場合に必要）

## FFmpeg の導入
https://www.ffmpeg.org/
こちらをダウンロード実績ありのものはこちらにアップロードしておきますのでご確認ください。
ローカルディスクに保存

WINDOWSの場合
ffmpegのbinフォルダーのPathを通す
システムのプロパティ → 環境変数（N）... →
→ ユーザーの環境変数 → path
こちらに以下を追記
C:\ffmpeg\bin

## ライブラリの導入


