import sys
from pathlib import Path
import re

# Thêm root vào sys.path để import gemini module ở thư mục cha
sys.path.append(str(Path(__file__).resolve().parent.parent))
import gemini  # Đảm bảo bạn đã có module này: gemini.call_gemini(prompt)


def extract_sections_from_markdown(file_path):
    """
    Extract Git Log Summary and Diff Summary from a Markdown file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = {}

    log_match = re.search(r"## 📌 Git Log Summary\n```bash\n(.*?)```", content, re.DOTALL)
    if log_match:
        sections['git_log'] = log_match.group(1).strip()

    diff_match = re.search(r"## 🧩 Diff Summary \(all files changed\)\n```diff\n(.*?)```", content, re.DOTALL)
    if diff_match:
        sections['diff_summary'] = diff_match.group(1).strip()

    return sections

def analyze_with_gemini(git_log, diff_summary):
    """
    Send Git log and diff summary to Gemini for initial security-related analysis.
    """
    prompt = f"""
You are a security-focused code reviewer.

Below is the Git commit log and diff summary between two software versions.

--- Git Log ---
{git_log}

--- Diff Summary ---
{diff_summary}

Please answer the following in a structured markdown format with clear sections and bullet points:

## 1. 🛡️ Security-Relevant Files/Paths
List the files or paths in the diff that are likely related to:
- Security patches (e.g., auth, crypto, input validation, WAF, etc.)
- Sensitive functionality (e.g., configuration, certificate handling)

## 2. 🔐 Security-Relevant Commits
List any commits (with hash and message) that suggest:
- Security fixes
- Vulnerability patches
- Updates to sensitive dependencies (e.g., cryptographic libraries)

## 3. 🧠 Initial Security Hypothesis
Provide a concise technical hypothesis:
- What kind of vulnerabilities are being addressed?
- Are there signs of misconfiguration, injection risks, permission issues, or insecure defaults?
- Any components worth deep manual review?

Use bullet points or numbered lists wherever helpful.
Be concise, technical, and structured.
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

def run_gemini_analysis_on_diff_report(input_markdown_path: str, output_markdown_path: str) -> str:
    """
    Phân tích bảo mật với Gemini từ file markdown chứa Git log và diff.

    Args:
        input_markdown_path (str): Đường dẫn tới file markdown chứa git log và diff.
        output_markdown_path (str): Đường dẫn tới file để lưu kết quả phân tích.

    Returns:
        str: Kết quả phân tích từ Gemini.
    """
    # Bước 1: Trích xuất Git log và Diff từ markdown
    sections = extract_sections_from_markdown(input_markdown_path)
    
    git_log = sections.get("git_log")
    diff_summary = sections.get("diff_summary")

    if not git_log and not diff_summary:
        raise ValueError("❌ Không tìm thấy cả Git Log Summary và Diff Summary trong file markdown.")
    if not git_log:
        raise ValueError("❌ Không tìm thấy mục '## 📌 Git Log Summary' trong file markdown.")
    if not diff_summary:
        raise ValueError("❌ Không tìm thấy mục '## 🧩 Diff Summary (all files changed)' trong file markdown.")

    # Bước 2: Gửi prompt cho Gemini
    gemini_result = analyze_with_gemini(git_log, diff_summary)

    # Bước 3: Ghi kết quả phân tích ra file
    save_analysis_to_md(gemini_result, output_markdown_path)

    return gemini_result