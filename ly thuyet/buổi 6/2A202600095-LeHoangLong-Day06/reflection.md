# Individual reflection — Lê Hoàng Long (2A202600095)

Tôi có tham gia làm bài tập nhóm và có thực hiện 1 bài riêng về cũng chủ đề.
với 1 cách tiếp cận mà tôi cho là phù hợp hơn với nội dung thực chiến AI,


## 1. Role
**AI Lead & Prompt Engineer.** Phụ trách thiết kế "bộ não" của chatbot, xây dựng kịch bản 6 bước và tích hợp mô hình ngôn ngữ Qwen3 cục bộ.

## 2. Đóng góp cụ thể
- **Thiết kế System Prompt**: Xây dựng kịch bản hội thoại thông minh giúp bot tự động phân loại ý định: hỏi ngoài lề, hỏi đối thủ, hay hỏi về VinFast.
- **Tích hợp Web Search (RAG)**: Viết Handler sử dụng thư viện `ddgs` để cho phép LLM truy cập Internet lấy giá xe và ảnh thực tế, giúp bot không bị ảo giác về giá cả.
- **Tối ưu hóa UI/UX**: Thêm các thông báo trạng thái "Đang suy nghĩ...", "Đang tìm kiếm..." để cải thiện trải nghiệm người dùng khi chạy model trên CPU có tốc độ xử lý chậm.

## 3. SPEC mạnh/yếu
- **Mạnh nhất**: Phần **Failure Modes**. Tôi đã lường trước được việc dữ liệu search có thể cũ và thiết kế cơ chế nhắc LLM kiểm tra mốc thời gian, cũng như cơ chế Guardrails để bot không bị dẫn dắt vào các chủ đề nhạy cảm.
- **Yếu nhất**: Phần **ROI**. Các chỉ số về lợi ích (Benefit) hiện tại vẫn dựa trên giả định. Cần có thêm dữ liệu thực tế về chi phí vận hành Cloud nếu scale-up thay vì chạy local.

## 4. Đóng góp khác
- Tham gia debug lỗi `ModuleNotFoundError` và lỗi kết nối mạng (Timeout) trong quá trình cài đặt thư viện trên máy local.
- Hỗ trợ viết hướng dẫn lắp đặt trong `prototype-readme.md`.

## 5. Điều học được
Tôi học được cách kết hợp giữa **Prompt Engineering** và **API Tools** (Searching). AI không cần biết tất cả mọi thứ; chỉ cần biết cách hỏi và tra cứu thông tin đúng nguồn là có thể cung cấp câu trả lời cực kỳ chính xác và thực tế theo thời gian thực.

## 6. Nếu làm lại
Tôi sẽ triển khai cơ chế **Vector Database** (như ChromaDB) để lưu trữ tài liệu kỹ thuật chi tiết của xe VinFast thay vì chỉ phụ thuộc vào Web Search. Điều này sẽ giúp câu trả lời chuyên sâu hơn về thông số kỹ thuật (như loại pin, công nghệ ADAS) mà web search đôi khi trả lời chưa đủ chi tiết.

## 7. AI giúp gì / AI sai gì
- **AI giúp**: Dùng AI (Antigravity/Gemini) để sinh nhanh mã nguồn mẫu cho Telegram Bot và brainstorm các logic xử lý kịch bản "Pivot" từ hãng đối thủ về VinFast rất sáng tạo.
- **AI sai/mislead**: Ban đầu AI gợi ý dùng thư viện `duckduckgo_search` bản cũ đã đổi tên, gây lỗi "import". Ngoài ra, AI cũng đề xuất dùng Async hoàn toàn cho search nhưng thực tế cần xử lý đồng bộ trong một số bước của handler để tránh treo hệ thống do xung khắc trong phiên làm việc "session conflict".
