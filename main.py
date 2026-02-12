import whisper
import glob
import os
from tqdm import tqdm

# プロキシ設定（必要に応じて）
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""

# ffmpegのログレベルを上げる（詳細ログを取得）
os.environ["FFMPEG_LOGLEVEL"] = "info"  # "debug" にしても可

def transcribe_japanese_files_in_folder(input_folder: str, output_folder: str):
    print("Whisperモデルの読み込み中...")
    model = whisper.load_model("base")
    print("モデル読み込み完了。")
    
    # 出力フォルダがなければ作成
    os.makedirs(output_folder, exist_ok=True)
    
    # M4Aファイルをすべて取得
    files = glob.glob(f"{input_folder}/*.m4a")
    print(f"対象ファイル数: {len(files)} 件")
    
    for file_path in tqdm(files):
        print(f"\n=== ファイル: {file_path} の文字起こし開始 ===")
        print("→ モデルにファイルを読み込ませています...")
        result = model.transcribe(file_path, language="ja")
        print("→ 文字起こし完了、テキスト抽出中...")
        text = result["text"]
        
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_folder, f"{base_name}_result.txt")
        
        print(f"→ 出力ファイルに保存中: {output_path}")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        print(f"=== 文字起こし結果を保存しました: {output_path} ===")
        print("-" * 40)

if __name__ == "__main__":
    input_folder = "../data"
    output_folder = "../result"
    transcribe_japanese_files_in_folder(input_folder, output_folder)
