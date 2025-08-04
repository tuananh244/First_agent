# version_selector.py

import subprocess
import re
from packaging import version

def list_git_tags(repo_path):
    """Trả về danh sách tất cả các tag từ repo."""
    result = subprocess.run(["git", "-C", repo_path, "tag"], capture_output=True, text=True)
    tags = result.stdout.strip().split("\n")
    return [tag for tag in tags if tag]

def extract_version_number(tag):
    """
    Trích version từ tag (ví dụ: 'or-1.2.3' -> '1.2.3')
    Nếu không tìm thấy version hợp lệ, trả về None.
    """
    match = re.search(r"\d+(?:\.\d+)+", tag)
    return match.group(0) if match else None

def parse_version_condition(condition: str):
    """
    Phân tích chuỗi điều kiện như '<= 1.11.4, > 1.0.0'
    Trả về list [(op, version_string)]
    """
    parts = re.split(r',\s*', condition)
    parsed = []
    for part in parts:
        match = re.match(r"(<=?|>=?)\s*([\d\.]+)", part)
        if match:
            op, ver = match.groups()
            parsed.append((op, ver))
        else:
            # Hỗ trợ '0 <= 1.11.4' kiểu so sánh trái phải
            match = re.match(r"(\d+)\s*(<=?|>=?)\s*([\d\.]+)", part)
            if match:
                _, op, ver = match.groups()
                parsed.append((op, ver))
    return parsed

def filter_versions(tags, conditions):
    """
    Lọc tag gốc theo điều kiện version.
    Trả về danh sách tag gốc phù hợp.
    """
    valid = []
    for tag in tags:
        tag_ver_str = extract_version_number(tag)
        if not tag_ver_str:
            continue
        try:
            tag_ver = version.parse(tag_ver_str)
        except:
            continue

        ok = True
        for op, cond_ver_str in conditions:
            cmp_ver = version.parse(cond_ver_str)
            if op == "<" and not tag_ver < cmp_ver: ok = False
            elif op == "<=" and not tag_ver <= cmp_ver: ok = False
            elif op == ">" and not tag_ver > cmp_ver: ok = False
            elif op == ">=" and not tag_ver >= cmp_ver: ok = False
        if ok:
            valid.append((tag_ver, tag))  # lưu cả version và tag gốc
    return valid

def find_matching_version(repo_path, version_condition: str, latest=True):
    """Trả về tên tag phù hợp nhất theo điều kiện"""
    tags = list_git_tags(repo_path)
    conds = parse_version_condition(version_condition)
    matched = filter_versions(tags, conds)
    if not matched:
        return None
    sorted_tags = sorted(matched, key=lambda x: x[0])  # sắp theo version
    return sorted_tags[-1][1] if latest else sorted_tags[0][1]  # trả về tag gốc

def find_tag_by_exact_version(repo_path, target_version: str):
    """
    Tìm tag có version khớp chính xác với target_version (ví dụ '1.11.5'),
    bất kể prefix là gì (controller-v1.11.5, v1.11.5, etc.)
    """
    tags = list_git_tags(repo_path)
    for tag in tags:
        tag_ver = extract_version_number(tag)
        if tag_ver == target_version:
            return tag
    return None