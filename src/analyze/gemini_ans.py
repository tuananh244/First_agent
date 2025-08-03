import sys
from pathlib import Path

# Thêm root vào sys.path để import gemini module ở thư mục cha
sys.path.append(str(Path(__file__).resolve().parent.parent))
import gemini  # Đảm bảo bạn đã có module này: gemini.call_gemini(prompt)

def read_diff_markdown(md_path: str) -> str:
    """
    Đọc nội dung markdown từ file diff_report.md.

    Args:
        md_path (str): Đường dẫn đến file markdown.

    Returns:
        str: Nội dung file markdown.
    """
    path = Path(md_path)
    if not path.exists():
        raise FileNotFoundError(f"❌ File not found: {md_path}")
    print(f"📄 Reading markdown file: {path.read_text}")
    return path.read_text(encoding="utf-8")

def generate_gemini_prompt_for_diff_summary(md_content: str) -> str:
    """
    Sinh prompt để gửi tới Gemini nhằm tóm tắt lỗi bảo mật từ nội dung file diff_report.md.

    Args:
        md_content (str): Nội dung markdown của báo cáo phân tích git diff.

    Returns:
        str: Prompt hoàn chỉnh để gửi tới Gemini.
    """
    prompt = f"""
You are a security researcher specialized in Kubernetes and NGINX.

Below is a Git diff report or vulnerability analysis related to the Ingress-NGINX controller. Your task is to analyze the vulnerability and explain its root cause and patch.

Respond in the following format:

1. **Summary (≤80 words):**
Briefly summarize the core vulnerability and its impact using clear, technical terms (e.g., “RCE via path traversal in annotation parsing”).

2. **Analysis:**
Explain:
- Why the vulnerability existed (e.g., missing validation, unsafe file path construction).
- Which parts of the code were affected (file/function names).
- How an attacker could exploit it.
- How the patch mitigates the issue (e.g., new validation, filepath.Join usage, regex to block CRLF).
Use precise technical language. Avoid markdown or lists unless needed for clarity.

Here is the input report:
```markdown
{md_content}
```
"""
    return gemini.call_gemini(prompt)

def save_analysis_to_md(result: str, output_path):
    """
    Lưu kết quả phân tích Gemini vào file markdown.

    Args:
        result (str): Kết quả phân tích.
        output_path (str): Đường dẫn file lưu kết quả.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 🧠 Gemini Security Analysis\n\n")
        f.write(result.strip())
    print(f"✅ Gemini analysis saved to: {output_path}")

def run_diff_analysis(md_path: str, output_path: str):
    """
    Thực hiện toàn bộ pipeline: đọc file diff_report.md → phân tích với Gemini → lưu kết quả ra file markdown.

    Args:
        md_path (str): Đường dẫn đến file diff_report.md.
        output_path (str): Đường dẫn file kết quả để lưu phân tích Gemini.
    """
    # Bước 1: Đọc nội dung diff
    md_content = read_diff_markdown(md_path)

    # Bước 2: Sinh prompt và gửi tới Gemini
    result = generate_gemini_prompt_for_diff_summary(md_content)

    # Bước 3: Lưu kết quả
    save_analysis_to_md(result, output_path)

    return result