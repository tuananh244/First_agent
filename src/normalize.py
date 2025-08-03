# Chuẩn hóa thông tin cho ứng dụng CVE Analyzer
# normalize.py

import re
from urllib.parse import urlparse, urlunparse

# -------------------- #
# Hàm chuẩn hóa CVE ID
# -------------------- #

### Kiểm tra chuẩn của CVE ID
def is_valid_cve_id(cve_id):
    """
    Kiểm tra xem CVE ID có hợp lệ hay không.
    Định dạng hợp lệ: CVE-YYYY-NNNN, ví dụ: CVE-2025-1974
    """
    pattern = r'^CVE-\d{4}-\d{4,7}$'
    return bool(re.match(pattern, cve_id.strip().upper()))

### Chuẩn hóa CVE ID
def normalize_cve_id(cve_input):
    """
    Chuẩn hóa input CVE ID về dạng CVE-YYYY-NNNN, ví dụ:
    'Cve 2025 1974' -> 'CVE-2025-1974'
    '2025 1974' -> 'CVE-2025-1974'
    'cve-2025-1974' -> 'CVE-2025-1974'
    """
    # Tìm năm và số thứ tự
    match = re.search(r'(\d{4})\D*(\d{4,7})', cve_input)
    if match:
        year, number = match.groups()
        # Đảm bảo đúng với định dạng CVE-YYYY-NNNN
        if is_valid_cve_id(f"CVE-{year}-{number}"):
            # Trả về định dạng chuẩn
            return f"CVE-{year}-{number}"
        else:
            return ""
    if is_valid_cve_id(cve_input):
        # Nếu đã là định dạng chuẩn, chỉ cần trả về
        return cve_input.strip().upper()
    
    # Nếu không khớp với định dạng nào, trả về chuỗi rỗng
    return ""


# -------------------- #
# Hàm chuẩn hóa URL
# -------------------- #

### Chuẩn hóa các URL cho đúng định dạng http/https://abc...
def normalize_url(url):
    """
    Chuẩn hóa URL về định dạng chuẩn.
    Nếu URL không bắt đầu bằng http:// hoặc https://, thêm http:// vào đầu.
    """
    # Loại bỏ khoảng trắng ở đầu và cuối
    url = url.strip()

    # Kiểm tra nếu URL đã có http:// hoặc https://
    if not re.match(r'^https?://', url):
        url = 'http://' + url

    # Phân tích URL
    parsed_url = urlparse(url)

    # Tạo lại URL chuẩn
    normalized_url = urlunparse((
        parsed_url.scheme.lower(),
        parsed_url.netloc.lower(),
        parsed_url.path,
        parsed_url.params,
        parsed_url.query,
        parsed_url.fragment
    ))

    return normalized_url

### Chuyển đổi URL từ CVE-ORG dạng json sang CVE-ORG dạng chuẩn
def convert_cveawg_to_cveorg(api_url):
    # Chuyển đổi URL từ CVE-ORG dạng json sang CVE-ORG dạng chuẩn
    # Ví dụ: https://cveawg.mitre.org/api/cve/CVE-2025-1974
    # Chuyển thành: https://www.cve.org/CVERecord?id=CVE-2025-1974
    if not api_url:
        return ""
    
    api_url = api_url.strip()
    
    # Kiểm tra nếu URL là dạng CVE-ORG API
    if not api_url.startswith("https://cveawg.mitre.org/api/cve/"):
        return normalize_url(api_url)
    
    # Chuyển đổi sang dạng chuẩn CVE-ORG
    cve_id = api_url.split("/")[-1].upper()
    cve_org_url = f"https://www.cve.org/CVERecord?id={cve_id}"
    
    return normalize_url(cve_org_url)