# version_selector.py

import subprocess
import os
import re
from packaging import version

def list_git_tags(repo_path):
    """Trả về danh sách tất cả các tag dạng version từ repo."""
    result = subprocess.run(["git", "-C", repo_path, "tag"], capture_output=True, text=True)
    tags = result.stdout.strip().split("\n")
    return [tag for tag in tags if tag]  # loại bỏ rỗng

def parse_version_condition(condition: str):
    """
    Từ điều kiện kiểu '0 <= 1.11.4' hoặc '>= 1.0.0, < 2.0.0' trả về list điều kiện [(op, version)]
    """
    parts = re.split(r',\s*', condition)
    parsed = []
    for part in parts:
        match = re.match(r"(<=?|>=?)\s*([\d\.]+)", part)
        if match:
            op, ver = match.groups()
            parsed.append((op, ver))
        else:
            # Xử lý dạng đặc biệt như '0 <= 1.11.4'
            match = re.match(r"(\d+)\s*(<=?)\s*([\d\.]+)", part)
            if match:
                _, op, ver = match.groups()
                parsed.append((op, ver))
    return parsed

def filter_versions(tags, conditions):
    """Lọc danh sách version theo điều kiện"""
    valid = []
    for tag in tags:
        try:
            tag_ver = version.parse(tag)
        except:
            continue

        ok = True
        for op, ver in conditions:
            cmp_ver = version.parse(ver)
            if op == "<" and not tag_ver < cmp_ver: ok = False
            elif op == "<=" and not tag_ver <= cmp_ver: ok = False
            elif op == ">" and not tag_ver > cmp_ver: ok = False
            elif op == ">=" and not tag_ver >= cmp_ver: ok = False
        if ok:
            valid.append(tag)
    return valid

def find_matching_version(repo_path, version_condition: str, latest=True):
    """Trả về version tag phù hợp nhất theo điều kiện"""
    tags = list_git_tags(repo_path)
    conds = parse_version_condition(version_condition)
    matched = filter_versions(tags, conds)
    if not matched:
        return None
    sorted_tags = sorted(matched, key=version.parse)
    return sorted_tags[-1] if latest else sorted_tags[0]
