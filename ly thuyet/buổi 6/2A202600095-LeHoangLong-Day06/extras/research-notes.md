# Research Notes — VinFast AI Sales Assistant

Ghi chép quá trình nghiên cứu, khảo sát và ra quyết định thiết kế cho AI Sales Assistant (Dùng để xét Bonus điểm).

---

## 1. Nghiên cứu thị trường & Đối thủ (Scoping)

### VinFast vs Tesla vs BYD
- **Tesla Model Y**: Mạnh về công nghệ tự lái (FSD) và hiệu suất, nhưng trạm sạc tại Việt Nam hầu như không có. Giá thành cao do thuế nhập khẩu.
- **BYD Atto 3**: Giá cạnh tranh, nội thất phá cách, nhưng cũng gặp vấn đề tương tự về hạ tầng sạc công cộng tại VN.
- **VinFast (VF6/7/8/9)**: Lợi thế tuyệt đối về trạm sạc (độ phủ 63 tỉnh thành). Dịch vụ hậu mãi 24/7 và chính sách thuê pin giúp giá xe dễ tiếp cận hơn.
- **Quyết định thiết kế**: Tập trung vào kỹ thuật **Pivot (lái chủ đề)** từ "Công nghệ pin/tự lái" sang "Hạ tầng trạm sạc & Hậu mãi" khi so sánh.

## 2. Khảo sát dữ liệu thực tế (Data Sourcing)

Dữ liệu giá xe VinFast thay đổi liên tục theo các chiến dịch (Mãnh liệt tinh thần Việt, VinPoint...).
- **Nguồn dữ liệu**: Website chính thức `vinfastauto.com`, các trang tin ô tô lớn (Oto.com.vn, Autodaily).
- **Thử nghiệm AI**: LLM có kiến thức đến 2023 (với Qwen3) nên thường báo giá sai các dòng VF6/VF7 hoặc VF3.
- **Giải pháp**: Tích hợp **Web Search (ddgs)** để lấy dữ liệu realtime. 
  - *Query ví dụ*: `VinFast VF3 giá lăn bánh tháng 4/2026`.

## 3. Thử nghiệm Mô hình ngôn ngữ (AI Feasibility)

Chúng tôi đã thử nghiệm 3 cấu hình:
1. **Cloud API (Gemini/OpenAI)**: Nhanh, thông minh nhưng phụ thuộc Internet và có chi phí hàng tháng.
2. **Local Qwen3 (CPU)**: An toàn dữ liệu, 0$ vận hành, nhưng tốc độ phản hồi chậm (2-3 tokens/s trên i5 laptop).
3. **Local Qwen3 + Web Search**: Kết quả tốt nhất cho prototype. 
- **Learning**: Cần thêm Typing status và các thông báo "Đang suy nghĩ" để người dùng không cảm thấy bot bị treo.

## 4. Tinh chỉnh kịch bản hội thoại (Prompt Engineering)

Quá trình Iterate System Prompt:
- **v1**: Chỉ trả lời thông tin xe. (Bot quá thụ động).
- **v2**: Thêm yêu cầu "Lái chủ đề". (Bot bắt đầu chủ động hơn nhưng đôi khi quá thô lỗ khi chê đối thủ).
- **v3 (Final)**: Đồng ý điểm mạnh của đối thủ trước, sau đó mới đưa ra lợi thế của VinFast. Thêm bước "Đánh giá tài chính" giúp lọc Lead chất lượng.

## 5. Case Study: Xử lý Failure Mode

**Vấn đề**: Search trả về kết quả từ năm 2022 khi giá VF8 còn cao.
**Giải pháp**: Trong System Prompt, yêu cầu LLM luôn đính kèm câu: *"Lưu ý: Đây là thông tin tham khảo từ Internet, vui lòng liên hệ nhân viên để có giá chính xác nhất tại thời điểm này."*

---
*Người thực hiện: Lê Hoàng Long - 2A202600095 - Nhóm 11 phòng E402*
