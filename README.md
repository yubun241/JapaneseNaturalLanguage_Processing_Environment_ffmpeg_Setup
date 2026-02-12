## Japanese Natural Language Processing Environment Setup (Python)
pythonを使って日本語テキストを自然言語処理するための基本環境構築手順
音声の録音データの文字お越しになっています

## 必要環境
macOS / Linux / Windows
Python 3.9以上
MeCab
mecab-ipadic（標準辞書）または mecab-ipadic-NEologd
FFmpeg（音声 → テキスト変換などを行う場合に必要）

## FFmpeg の導入
こちらからダウンロード
https://www.ffmpeg.org/
ローカルディスクに保存

WINDOWSの場合
ffmpegのbinフォルダーのPathを通す
システムのプロパティ → 環境変数（N）... →
→ ユーザーの環境変数 → path
こちらに以下を追記
C:\ffmpeg\bin

## テストプログラム
こちらは音声認識を行うプログラムになっています。
音声認識した言語データをテキストデータに格納しています
入力する音声データ
今回は.m4aファイルを../dataフォルダに格納してほしいです。
そこから読み込めるpath構造にてこちらを実行してください。
結果は../resultに格納されます。


