import os

def get_output_dir(base_dir: str = "output", cve_id: str = "CVE-XXXX-YYYY") -> str:
    """
    Trả về đường dẫn output chuẩn theo format output/{cve_id}
    và tạo thư mục nếu chưa tồn tại.
    """
    # Normalize CVE ID (vd: CVE_2025_1974 nếu cần)
    folder_name = cve_id.replace("-", "_").upper()

    # Đường dẫn tương đối từ root
    output_dir = os.path.join(base_dir, folder_name)

    # Tạo thư mục nếu chưa có
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


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