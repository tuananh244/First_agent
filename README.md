# 🔍 CVE Technical Analysis Pipeline

Hệ thống này hỗ trợ phân tích kỹ thuật các lỗ hổng bảo mật (CVE) bằng cách tự động hóa các bước sau:

## 🚦 Pipeline Phân Tích

## 🔁 Pipeline Phân Tích Tự Động Từ CVE ID

```mermaid
graph LR

    A[CVE ID] --> B[📥 fetch_info.py]
    B --> C[🔗 classify_url.py ]
    C --> D[🐙 repo.py]
    D --> E[📜 git_diff.py]
    E --> F[🧠 gemini_analyze.py]
    F --> G[📁 extract_diff.py]
    G --> H[🧠 gemini_ans.py]
    H --> I[📝 write_report.py]

```

