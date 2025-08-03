# clone_repo.py
# Trích xuất và clone GitHub repository từ URL

import os
import re
import subprocess
import shutil
from urllib.parse import urlparse

def extract_repo_url(github_url: str) -> str:
    """
    Trích xuất URL của GitHub repository gốc từ bất kỳ URL GitHub nào.
    """
    match = re.match(r"https?://github\.com/([^/]+/[^/]+)", github_url)
    if match:
        return f"https://github.com/{match.group(1)}.git"
    raise ValueError(f"❌ Không thể trích xuất repository từ URL: {github_url}")

def clone_temp_repo_from_link(github_url: str, temp_base_dir: str = "temp_repos") -> str:
    """
    Clone GitHub repo về thư mục tạm (temporary directory).
    Nếu đã tồn tại thì bỏ qua. Trả về đường dẫn local tới repo.
    """
    repo_url = extract_repo_url(github_url)
    repo_name = repo_url.rstrip(".git").split("/")[-1]
    owner = repo_url.split("/")[-2]
    repo_local_path = os.path.join(temp_base_dir, f"{owner}__{repo_name}")

    os.makedirs(temp_base_dir, exist_ok=True)

    if not os.path.exists(repo_local_path):
        try:
            subprocess.run(["git", "clone", "--depth=1", repo_url, repo_local_path], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"❌ Lỗi khi clone repo: {e}")
    else:
        print(f"✅ Repo đã tồn tại ở {repo_local_path}, bỏ qua clone.")

    return repo_local_path

def cleanup_temp_repo(path: f"temp_repos") -> None:
    """
    Xóa toàn bộ thư mục repo tạm sau khi phân tích.
    """
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"🧹 Đã xóa thư mục tạm: {path}")
    else:
        print(f"⚠️ Thư mục không tồn tại: {path}")