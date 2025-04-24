# 簡易的な元戻しスクリプト例
from pathlib import Path
for bak in Path("content/questions").rglob("*.md.bak"):
    original = bak.with_suffix("")  # .md
    original.write_text(bak.read_text(encoding='utf-8'), encoding='utf-8')
    print(f"🔁 復元: {original}")
