import re
import os
import subprocess

def extract_security_file_paths(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm phần "## 1. 🛡️ Security-Relevant Files/Paths" → trước "## 2."
    section = re.search(r"## 1\..*?Files/Paths\s+(.*?)\n## 2", content, re.DOTALL)
    if not section:
        raise ValueError("❌ Không tìm thấy phần liệt kê file!")

    file_block = section.group(1)

    # Tìm các dòng dạng "*   `file_path`: mô tả"
    matches = re.findall(r"\*\s+`([^`]+)`", file_block)
    # Loại bỏ thư mục hoặc dòng không hợp lệ
    file_paths = [f.strip() for f in matches if f.strip() and "/" in f]

    print(f"[📁] Trích xuất {len(file_paths)} file từ markdown:")
    for f in file_paths:
        print(" -", f)

    return file_paths


def get_git_diff(repo_path, old_commit, new_commit, file_list):
    os.chdir(repo_path)
    diffs = {}
    for file_path in file_list:
        try:
            result = subprocess.run(
                ["git", "diff", old_commit, new_commit, "--", file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            diffs[file_path] = result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[⚠️] Lỗi khi diff {file_path}: {e.stderr.strip()}")
    return diffs


def write_diff_to_markdown(diffs, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 📄 Git Diff Report for Security-Relevant Files\n\n")
        for path, diff in diffs.items():
            f.write(f"## 🔸 {path}\n\n")
            f.write("```diff\n")
            f.write(diff if diff.strip() else "[No diff found]\n")
            f.write("```\n\n")
    print(f"[✅] Báo cáo Markdown đã tạo tại: {output_path}")


def generate_security_diff_report(repo_path, old_commit, new_commit, md_path, output_path):
    """
    - Trích xuất danh sách file bảo mật từ báo cáo Markdown.
    - Tạo diff cho từng file giữa 2 commit/tag.
    - Ghi kết quả vào file Markdown.
    - Trả về dict chứa nội dung diff.
    """
    # 1. Trích xuất danh sách file
    file_list = extract_security_file_paths(md_path)

    # 2. Sinh diff
    diffs = get_git_diff(repo_path, old_commit, new_commit, file_list)

    # 3. Ghi vào file markdown
    write_diff_to_markdown(diffs, output_path)

    return diffs
