# Design Iterations — VinFast AI Sales Assistant

Tài liệu ghi lại các bước thay đổi trong thiết kế (UI/UX, Luồng hội thoại, Prompt) để đạt được kết quả cuối cùng.

---

## 1. Tiến hóa của Luồng Hội thoại (Conversation Flow)

### V1: Q&A Cơ bản
- **Thiết kế**: User hỏi -> Bot tìm thông tin -> Trả lời.
- **Vấn đề**: Người dùng cảm thấy bot "vô hồn", chỉ là một bộ máy tra cứu thông tin.

### V2: Bổ sung trạng thái xử lý (UX Improvement)
- **Thay đổi**: Thêm tin nhắn "Nhân viên đang suy nghĩ...", "Đang tìm kiếm...".
- **Kết quả**: Giảm bớt sự khó chịu của người dùng khi phải chờ đợi 20-30s do LLM chạy trên CPU. Người dùng hiểu bot đang làm việc chứ không phải bị treo.

### V3: Chi tiết hóa quy trình (Final UX)
- **Thay đổi**: Phân tách rõ ràng các bước: Search -> Suy nghĩ -> Chốt đơn. Bổ sung trạng thái "Typing..." của Telegram.
- **Kết quả**: Trải nghiệm mượt mà, chuyên nghiệp như đang chat với tư vấn viên thật.

---

## 2. Iteration của System Prompt (Brain Design)

| Phiên bản | Thay đổi chính | Kết quả |
|-----------|----------------|---------|
| **Draft 1** | Chỉ cung cấp thông số xe. | Bot trả lời máy móc, không biết "bán hàng". |
| **Draft 2** | Thêm quy tắc "Pivot" (lái chủ đề hãng khác). | Bot bắt đầu bảo vệ thương hiệu VinFast tốt hơn khi bị so sánh với Tesla/BYD. |
| **Final** | Thêm bước "Đánh giá tài chính" + "Chốt đơn". | Bot chủ động dẫn dắt người dùng đến bước mua hàng thay vì chỉ cung cấp thông tin. |

---

## 3. Thiết kế Poster & Slides (Visual Design)

### Giai đoạn 1: Sketch & Markdown
- **Ý tưởng**: Chỉ trình bày Text trên Markdown.
- **Nhận xét**: Khó thu hút sự chú ý tại phiên trình bày.

### Giai đoạn 2: HTML/CSS High-Fidelity (Final)
- **Ý tưởng**: Dùng phong cách Dark Mode cao cấp của ngành ô tô. 
- **Cải tiến**: 
  - Sử dụng hình ảnh Hero thiết kế riêng (VF8).
  - Typography cực lớn để đọc được từ xa 2 mét.
  - Sử dụng các lớp phủ (Glassmorphism) để tạo cảm giác công nghệ cao.

---

## 4. Lựa chọn Công cụ & Công nghệ

1. **Ban đầu**: Định dùng Cloud API. -> **Thay đổi**: Dùng LLM tại chỗ (Ollama) để chứng minh khả năng bảo mật dữ liệu và tiết kiệm chi phí cho doanh nghiệp.
2. **Ban đầu**: Chỉ dùng dữ liệu nạp sẵn. -> **Thay đổi**: Tích hợp tìm kiếm trên mạng do dữ liệu ô tô biến động theo từng ngày (khuyến mãi/giá lăn bánh).

---
*Người thực hiện: Lê Hoàng Long - 2A202600095 - Nhóm 11 phòng E402*
