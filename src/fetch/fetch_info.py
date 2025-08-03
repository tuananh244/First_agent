# src/fetch_info.py
# Lấy thông tin CVE từ CVE-ORG

import requests
import normalize
import fetch.classify_url as classify_url

# Hàm lấy dữ liệu CVE từ CVE-ORG API
def fetch_cve_json(cve_id: str) -> dict:
    """
    Lấy dữ liệu CVE từ CVE-ORG API.
    Trả về một dict chứa thông tin CVE.
    """
    url = f"https://cveawg.mitre.org/api/cve/{cve_id}"
    url_normalized = normalize.convert_cveawg_to_cveorg(url)
    headers = {"Accept": "application/json"}
    
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"❌ Lỗi lấy dữ liệu CVE: {res.status_code}")
    
    data = res.json()

    # Trích xuất mô tả (tiếng Anh)
    descriptions = data.get("containers", {}).get("cna", {}).get("descriptions", [])
    description = next((d["value"] for d in descriptions if d["lang"] == "en"), "")

    # Lấy CWE
    cwe_ids = []
    problem_types = data.get("containers", {}).get("cna", {}).get("problemTypes", [])
    for pt in problem_types:
        for desc in pt.get("descriptions", []):
            if desc.get("type") == "CWE" and "cweId" in desc:
                cwe_ids.append(desc["cweId"])


    # Lấy tham chiếu
    raw_references = {
        normalize.normalize_url(ref["url"])
        for ref in data.get("containers", {}).get("cna", {}).get("references", [])
        if isinstance(ref, dict) and isinstance(ref.get("url"), str) and ref["url"].startswith("http")
    }


    # CVSS và CNA
    metrics = data.get("containers", {}).get("cna", {}).get("metrics", [])
    cvss_score, cvss_version, cvss_vector, cvss_severity = None, None, None, None
    for metric in metrics:
        if "cvssV3_1" in metric:
            cvss = metric["cvssV3_1"]
            cvss_score = cvss.get("baseScore")
            cvss_vector = cvss.get("vectorString")
            cvss_severity = cvss.get("baseSeverity")
            cvss_version = "3.1"
            break
        elif "cvssV3_0" in metric:
            cvss = metric["cvssV3_0"]
            cvss_score = cvss.get("baseScore")
            cvss_vector = cvss.get("vectorString")
            cvss_severity = cvss.get("baseSeverity")
            cvss_version = "3.0"
            break
        elif "cvssV2_0" in metric:
            cvss = metric["cvssV2_0"]
            cvss_score = cvss.get("baseScore")
            cvss_vector = cvss.get("vectorString")
            cvss_severity = cvss.get("baseSeverity")
            cvss_version = "2.0"
            break

    # CNA
    cna_name = data.get("cveMetadata", {}).get("assignerShortName", "Unknown")

    # Affected
    affected_info = []
    repos = set()

    affected = data.get("containers", {}).get("cna", {}).get("affected", [])
    for item in affected:
        vendor = item.get("vendor", "")
        product = item.get("product", "")
        versions = []

        # Lấy repo (nếu có) và chuẩn hóa
        repo_url = item.get("repo")
        if isinstance(repo_url, str) and repo_url.startswith("http"):
            raw_references.add(normalize.normalize_url(repo_url))

        version_data = item.get("versions", [])
        for v in version_data:
            ver_info = []

            if "version" in v:
                ver_info.append(v["version"])
            if "lessThanOrEqual" in v:
                ver_info.append(f"<= {v['lessThanOrEqual']}")
            if "lessThan" in v:
                ver_info.append(f"< {v['lessThan']}")

            if ver_info:
                versions.append(" ".join(ver_info))

        affected_info.append({
            "vendor": vendor,
            "product": product,
            "versions": versions,
        })

    classified_links = classify_url.classify_links_for_json(list(raw_references))

    return {
        "cve_id": cve_id,
        "description": description,
        "cwe": cwe_ids,
        "github_links": classified_links["github_links"],
        "poc_links": classified_links["poc_links"],
        "references": classified_links["references"],
        "cvss_score": cvss_score,
        "cvss_vector": cvss_vector,
        "cvss_severity": cvss_severity,
        "cvss_version": cvss_version,
        "cna": cna_name,
        "url": url_normalized,
        "affected": affected_info,
    }
