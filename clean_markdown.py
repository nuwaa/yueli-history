import re
from pathlib import Path
import shutil

def clean_markdown(content):
    # 【1. ○○】→ ## ○○
    #content = re.sub(r'【\d+\. ([^】]+)】', r'## \1', content)

    # 修正後（番号を残す）
    content = re.sub(r'【(\d+\. [^】]+)】', r'## \1', content)

    # 全角スペースを半角に
    content = content.replace('　', ' ')

    # 複数行の空行を1つにまとめる（2行以上 → 1行）
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 表示崩れしがちな "│" を Markdown表に置き換える用のフラグを立ててもOK（今回は簡略化）

    return content.strip()

def process_files(base_dir, backup=True):
    md_files = list(Path(base_dir).rglob("*.md"))
    print(f"🔍 対象ファイル数: {len(md_files)} 件")

    for mdfile in md_files:
        content = mdfile.read_text(encoding='utf-8')

        # バックアップ（任意）
        if backup:
            shutil.copy(mdfile, mdfile.with_suffix(mdfile.suffix + ".bak"))

        cleaned = clean_markdown(content)
        mdfile.write_text(cleaned, encoding='utf-8')
        print(f"✅ 整形完了: {mdfile}")

# 使用方法
if __name__ == "__main__":
    process_files("content/questions", backup=True)  # backup=False にすれば上書きのみ
