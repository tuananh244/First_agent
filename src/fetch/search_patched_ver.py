from typing import List
import gemini

def extract_patched_versions_with_gemini(version_ranges: List[str]) -> List[str]:
    """
    Sử dụng Gemini để suy ra các patched version từ danh sách version bị ảnh hưởng.
    """
    prompt = f"""
You are given a list of version ranges that are affected by a security vulnerability in a software product:

{chr(10).join("- " + v for v in version_ranges)}

For each range, identify the first version that falls outside the affected range — that is, the version in which the vulnerability is patched.

Only return lines in the following format:
Patched version: x.y.z
Do not include any additional text or explanations.
Make sure to extract the version numbers correctly, even if they are in a range format.
For example, if the affected range is "1.0.0 - 1.2.3", the patched version might be "1.2.4" or "1.3.0".
"""
    response = gemini.call_gemini(prompt)
    patched_versions = []

    for line in response.strip().splitlines():
        if "patched version" in line.lower():
            version = line.split(":")[-1].strip()
            patched_versions.append(version)

    return patched_versions
