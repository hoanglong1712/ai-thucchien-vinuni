# Nội dung đã thực hiện từ ngày 24-6-2026
- https://github.com/hoanglong1712/ai-thucchien-vinuni/tree/main/vinsmartfuture/conflicted%20content%20benchmarking
# Kết quả đã thực hiện trong ngày 25-6-2028
- Tập tin excel chứa kết quả tính điểm các cặp xung đột https://docs.google.com/spreadsheets/d/1T0RwtSTbgz2AIF4g4AlWhPBlImrMFPzGAz45g8NXVTs/edit?usp=sharing
- Tập tin excel đầu vào: https://devel-coretech-bucket.s3.ap-southeast-1.amazonaws.com/sonnh95/intern/conflict_report_23c1a89c-5d17-4a64-b68b-072c440a4273.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS2XOJSZJDY7MOLUX%2F20260625%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20260625T044554Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f5eb94506bc7ba14b12cdec178835c7fdc14715170e7fc7e17eda9007d6d189a
- Ý tưởng xây dựng pipeline
  - Các đoạn xung đột cần có lượng từ vựng gần như nhau và chỉ khác nhau ở những từ chốt nhằm tạo ra hiện tượng hiểu nhầm của người đọc -> càng chung nhiều từ càng tốt -> giá trị cosine similarity và và IoU càng cao càng tốt -> đánh giá qua "rule-based"
  -  Các đoạn xung đột cần có ngữ nghĩa mâu thuẫn với nhau -> đánh giá qua "LLM"
- Pipeline:   https://github.com/hoanglong1712/ai-thucchien-vinuni/blob/main/vinsmartfuture/conflicted%20content%20benchmarking/c%E1%BA%ADp%20nh%E1%BA%ADt%2025-6-2026/pipeline.md
