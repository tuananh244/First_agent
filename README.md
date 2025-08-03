# 🔍 CVE Technical Analysis Pipeline

Hệ thống này hỗ trợ phân tích kỹ thuật các lỗ hổng bảo mật (CVE) bằng cách tự động hóa các bước sau:

## 🚦 Pipeline Phân Tích

## 🔁 Pipeline Phân Tích Tự Động Từ CVE ID

```mermaid
graph TD

    A[CVE ID] --> B[📥 fetch_info: Lấy thông tin từ CVE.org]
    B --> C[🔗 Phân loại reference (repo, PoC, patch...)]
    C --> D[🐙 repo.py: Clone repository từ GitHub]
    D --> E[📜 git_diff.py: Phân tích git log + git diff]
    E --> F[🧠 gemini_analyze: Gọi Gemini phân tích log + diff]
    F --> G[📁 extract_diff.py: Trích xuất code của file bị ảnh hưởng từ 2 phiên bản]
    G --> H[🧠 gemini_ans.py: Phân tích code diff với Gemini]
    H --> I[📝 Tạo báo cáo kỹ thuật Markdown + Output]

    style A fill:#e3f2fd
    style I fill:#fff3e0
```

