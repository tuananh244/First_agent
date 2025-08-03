# run.py
# Chạy ứng dụng Streamlit từ src/app.py

import subprocess
import sys
import os

def run_ui():
    """
    Chạy giao diện Streamlit từ src/app.py
    """
    ui_path = os.path.join(os.path.dirname(__file__), "src", "app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", ui_path])

if __name__ == "__main__":
    run_ui()