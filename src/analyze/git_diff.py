import os
import subprocess
from pathlib import Path
from datetime import datetime

def fetch_tags(repo_path):
    subprocess.run(["git", "fetch", "--tags"], cwd=repo_path, check=True)

def get_git_log(repo_path, old_tag, new_tag):
    result = subprocess.run(
        ["git", "log", "--pretty=format:%h|%an|%ad|%s", "--date=short", f"{old_tag}..{new_tag}"],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def get_diff_tree(repo_path, old_tag, new_tag):
    result = subprocess.run(
        ["git", "diff", "--name-status", old_tag, new_tag],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def generate_markdown_report(repo_path, old_tag, new_tag, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 🔍 Code Diff Analysis: `{old_tag}` → `{new_tag}`\n")
        f.write(f"📅 Generated at: {datetime.now().isoformat()}\n\n")

        # Git log summary
        f.write("## 📌 Git Log Summary\n")
        f.write("```bash\n")
        f.write(get_git_log(repo_path, old_tag, new_tag) + "\n")
        f.write("```\n\n")

        # Diff summary
        f.write("## 🧩 Diff Summary (all files changed)\n")
        f.write("```diff\n")
        f.write(get_diff_tree(repo_path, old_tag, new_tag) + "\n")
        f.write("```\n\n")

        f.write("\n✅ End of Report\n")

    return output_path

def extract_log_and_diff_info(repo_path, old_tag, new_tag, output_path):
    """
    Lấy thông tin Git log và diff giữa 2 tag, lưu vào file Markdown,
    và trả lại nội dung đã trích xuất.

    Args:
        repo_path (str): Đường dẫn đến repository.
        old_tag (str): Tag cũ (bên trái).
        new_tag (str): Tag mới (bên phải).
        output_path (str): Đường dẫn để lưu file markdown.

    Returns:
        dict: {
            "log": <git log summary>,
            "diff": <diff summary>,
            "report_path": <path to saved .md file>
        }
    """
    # Sinh markdown file
    report_path = generate_markdown_report(repo_path, old_tag, new_tag, output_path)

    # Đọc lại nội dung vừa sinh
    log_summary = get_git_log(repo_path, old_tag, new_tag)
    diff_summary = get_diff_tree(repo_path, old_tag, new_tag)

    return {
        "log": log_summary,
        "diff": diff_summary,
    }

