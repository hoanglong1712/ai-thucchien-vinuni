# Nội dung đã thực hiện từ ngày 24-6-2026
- https://github.com/hoanglong1712/ai-thucchien-vinuni/tree/main/vinsmartfuture/conflicted%20content%20benchmarking
# Kết quả đã thực hiện trong ngày 25-6-2028
- File excel chứa kết quả tính điểm các cặp xung đột https://docs.google.com/spreadsheets/d/1T0RwtSTbgz2AIF4g4AlWhPBlImrMFPzGAz45g8NXVTs/edit?usp=sharing
- Ý tưởng xây dựng pipeline
  - Các đoạn xung đột cần có lượng từ vựng gần như nhau và chỉ khác nhau ở những từ chốt nhằm tạo ra hiện tượng hiểu nhầm của người đọc -> càng chung nhiều từ càng tốt -> giá trị cosine similarity và và IoU càng cao càng tốt -> đánh giá qua "rule-based"
  -  Các đoạn xung đột cần có ngữ nghĩa mâu thuẫn với nhau -> đánh giá qua "LLM"
- Pipeline:   https://github.com/hoanglong1712/ai-thucchien-vinuni/blob/main/vinsmartfuture/conflicted%20content%20benchmarking/c%E1%BA%ADp%20nh%E1%BA%ADt%2025-6-2026/pipeline.md
