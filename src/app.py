# streamlit_app.py
import streamlit as st
import time
import json
import os
from analyze import extract_diff, repo, gemini_analyze, git_diff
from fetch import search_patched_ver
import path_utils
import write_report
import normalize
import version_resolver

st.set_page_config(
    page_title="CVE Analyzer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Phân tích CVE")

st.sidebar.markdown("""
### Hướng dẫn sử dụng:
- Nhập mã CVE vào ô bên dưới.
- Nhấn nút "Phân tích" để bắt đầu.
- Kết quả sẽ hiển thị sau khi phân tích hoàn tất.
""")

text_input = st.text_input("🔡 Nhập mã CVE:", placeholder="VD: CVE-2025-1974")
cve_id = normalize.normalize_cve_id(text_input)

if st.button("🔍 Phân tích"):
    if not cve_id:
        st.error("❌ Vui lòng nhập lại mã CVE hợp lệ.")
        st.stop()

    st.info(f"🔍 Bắt đầu phân tích: {cve_id}...")
    with st.spinner("🔍 Đang tải dữ liệu..."):
        try:
            report_json = write_report.build_cve_report_json(cve_id)
            if isinstance(report_json, str):
                report_json = json.loads(report_json)

            github_url = report_json.get("github_links", [None])[0]
            if not github_url:
                st.error("❌ Không tìm thấy liên kết GitHub trong báo cáo CVE.")
                st.stop()

            output_path = path_utils.get_output_dir(cve_id=cve_id)
            repo_path = repo.clone_temp_repo_from_link(github_url)
            st.success(f"✅ Đã clone repository: {repo_path}")

            old_ver_expr = report_json.get("affected_versions", [None])[0]
            new_ver_raw = report_json.get("patched_versions", [None])[0]

            old_ver = version_resolver.resolve_version_from_exprort(repo_path, old_ver_expr)
            new_ver = version_resolver.find_closest_tag(repo_path, new_ver_raw)

            
            md_path = os.path.join(output_path, "log_and_summary_diff.md")
            result = git_diff.generate_markdown_report(repo_path, old_ver, new_ver, md_path)
            if not result:
                st.error("❌ Không tìm thấy thông tin bảo mật.")
                st.stop()
            st.success(f"✅ Đã trích xuất log và summary vào {md_path}.")
            
            ### Gọi Gemini để phân tích Log và Summary
            gemini_analyse_path = os.path.join(output_path, "gemini_analysis.md")

            try:
                gemini_result = gemini_call.run_gemini_analysis_on_diff_report(result, gemini_analyse_path)
            except ValueError as e:
                st.error(f"❌ {str(e)}")
                st.stop()

            st.success(f"✅ Đã lưu kết quả của Gemini vào {gemini_analyse_path}.")
            st.write(gemini_result)

            # Đoạn phân tích code diff
            code_diff_path = os.path.join(output_path, "code_diff.md")
            # Dùng kết quả từ phân tích log và diff thay vì đọc lại từ markdown
            git_log, diff_summary = extract_diff.generate_security_diff_report(repo_path, old_ver, new_ver, gemini_analyse_path, code_diff_path)
            st.success(f"✅ Đã lưu kết quả của code diff vào {code_diff_path}.")

            ### Gọi Gemini để xử lý các thông tin code
            summary_path = os.path.join(output_path, "summary_of_CVE.md")
            gemini_call.run_diff_analysis(code_diff_path, summary_path)
            st.success(f"✅ Đã lưu kết quả của Gemini vào {summary_path}.")
            st.markdown(Path(summary_path).read_text(), unsafe_allow_html=True)

            st.success("✅ Phân tích hoàn tất!")
            st.json(report_json, expanded=True)
        except Exception as e:
            st.error(f"❌ Lỗi trong quá trình phân tích: {str(e)}")
