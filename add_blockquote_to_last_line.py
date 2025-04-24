from pathlib import Path
import shutil

def format_last_line_as_blockquote(content):
    lines = content.rstrip().split('\n')
    if not lines:
        return content

    last_line = lines[-1].strip()

    # すでに引用形式 or 空行なら無視
    if last_line.startswith('>') or last_line == '':
        return content

    # 最終行を強制的に引用化
    lines[-1] = f'> {last_line}'

    return '\n'.join(lines)

def process_files(base_dir="content/questions", backup=True):
    md_files = list(Path(base_dir).rglob("*.md"))
    print(f"🔍 対象ファイル数: {len(md_files)} 件")

    for mdfile in md_files:
        content = mdfile.read_text(encoding='utf-8')

        if backup:
            shutil.copy(mdfile, mdfile.with_suffix(mdfile.suffix + ".bak"))

        updated = format_last_line_as_blockquote(content)
        mdfile.write_text(updated, encoding='utf-8')
        print(f"✅ 最終行を引用化: {mdfile}")

if __name__ == "__main__":
    process_files()
