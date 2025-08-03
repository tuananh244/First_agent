# build_cve_report_json.py

import json
import fetch.fetch_info as fetch_info
import fetch.search_patched_ver as spv

def build_cve_report_json(cve_id: str) -> str:
    """
    Tạo báo cáo CVE dưới dạng JSON từ CVE ID.
    Trả về chuỗi JSON chứa thông tin chi tiết.
    """
    # 🔍 Lấy dữ liệu CVE từ fetch_info
    cve_data = fetch_info.fetch_cve_json(cve_id)
    if not cve_data:
        raise ValueError(f"❌ Không tìm thấy dữ liệu cho CVE ID: {cve_id}")

    # 📦 Trích xuất affected version range
    version_ranges = []
    if "affected" in cve_data:
        for item in cve_data["affected"]:
            if "versions" in item:
                version_ranges.extend(item["versions"])

    # 🤖 Gọi Gemini để suy ra các patched versions
    patched_versions = []
    if version_ranges:
        patched_versions = spv.extract_patched_versions_with_gemini(version_ranges)

    # 📋 Tạo báo cáo JSON
    report = {
        "cve_id": cve_data.get("cve_id", cve_id),
        "description": cve_data.get("description", ""),
        "severity": cve_data.get("cvss_severity", ""),
        "cvss_score": cve_data.get("cvss_score", 0.0),
        "cvss_vector": cve_data.get("cvss_vector", ""),
        "cvss_version": cve_data.get("cvss_version", ""),
        "cna": cve_data.get("cna", ""),
        "references": cve_data.get("references", []) + cve_data.get("poc_links", []) + cve_data.get("github_links", []),
        "github_links": cve_data.get("github_links", []),
        "poc_links": cve_data.get("poc_links", []),
        "affected_versions": version_ranges,
        "patched_versions": patched_versions,
        "weaknesses": cve_data.get("cwe", []),
        "source_url": cve_data.get("url", "")
    }

    return json.dumps(report, indent=2, ensure_ascii=False)

