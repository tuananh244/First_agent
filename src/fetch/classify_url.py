# classify_url.py
# Hàm phân loại các liên kết trong dữ liệu CVE

from urllib.parse import urlparse
import re

# Phân loại các liên kết trong báo cáo CVE
# Trả về một dict chứa các liên kết đã phân loại
def classify_links_for_json(references: list[str]) -> dict:
    """
    Phân loại các liên kết trong báo cáo CVE.
    Trả về một dict chứa các liên kết đã phân loại.
    """
    github_links = []
    poc_links = []
    remaining_refs = []

    def classify_link(url: str) -> str:
        if not url or not isinstance(url, str):
            return "invalid"

        url = url.strip()
        parsed = urlparse(url)
        netloc = parsed.netloc.lower()
        path = parsed.path.lower()

        if "github.com" in netloc:
            if re.fullmatch(r'/[^/]+/[^/]+/?', path):
                return "github_repo"
            if "/commit/" in path or "/pull/" in path:
                return "github_code"
            return "github_other"

        if any(x in netloc for x in [
            "exploit-db.com", "packetstormsecurity.com", "0day.today",
            "cxsecurity.com", "exploit.in", "exploit"
        ]):
            return "exploit"

        if any(x in netloc for x in [
            "cve.org", "nvd.nist.gov", "mitre.org", "osv.dev", "openwall.com"
        ]) or any(x in path for x in [
            "docs", "documentation", "manual", "report", "changelog"
        ]):
            return "ignore"

        return "reference"

    for url in references:
        link_type = classify_link(url)
        if link_type in ["github_repo", "github_code"]:
            github_links.append(url)
        elif link_type == "exploit":
            poc_links.append(url)
        elif link_type == "reference":
            remaining_refs.append(url)
        elif link_type == "ignore":
            continue
        else:
            remaining_refs.append(url)  # fallback

    return {
        "github_links": list(set(github_links)),  # loại trùng nếu có
        "poc_links": list(set(poc_links)),
        "references": list(set(remaining_refs)),
    }
