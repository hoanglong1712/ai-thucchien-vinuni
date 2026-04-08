# UX exercise — Vietnam Airlines Chatbot NEO

## Sản phẩm: Vietnam Airlines Chatbot NEO (hỗ trợ khách hàng, tra cứu chuyến bay)

## 4 paths

### 1. AI đúng
- User hỏi thông tin chuyến bay Hà Nội → Đà Nẵng
- Chatbot trả lời chính xác giờ bay, hiển thị rõ ràng
- User yên tâm, không cần thao tác thêm
- UI: hội thoại đơn giản, thông tin rõ ràng


### 2. AI không chắc
- User hỏi thông tin phức tạp (ví dụ: đổi vé, hành lý đặc biệt)
- Chatbot trả lời chung chung hoặc im lặng, không hiển thị confidence
- Thường chuyển hướng sang menu cố định
- Vấn đề: thiếu minh bạch, user không biết AI có chắc hay không


### 3. AI sai
- User hỏi giờ bay → chatbot trả lời sai lệch so với website
- User phát hiện khi kiểm tra lại thông tin chính thức
- Sửa: phải gõ lại hoặc gọi hotline → mất thời gian
- Vấn đề: recovery flow tốn công, không có cơ chế sửa nhanh trong chat

### 4. User mất niềm tin
- Sau vài lần chatbot trả lời sai hoặc mơ hồ, user không tin tưởng nữa
- Có fallback: gợi ý gọi tổng đài, nhưng nút exit không nổi bật
- User phải tự tìm cách thoát → trải nghiệm kém


## Path yếu nhất: Path 2 + 3
- Khi AI không chắc hoặc sai, hệ thống không minh bạch và recovery flow mất nhiều bước
- Không có confidence score, không có gợi ý rõ ràng
- User dễ bỏ cuộc hoặc phải chuyển sang hotline


## Gap marketing vs thực tế
- Marketing: “Trợ lý ảo 24/7 thông minh, hỗ trợ nhanh chóng”
- Thực tế: chatbot vẫn khá kịch bản, ít cá nhân hóa, chưa thể hiện rõ AI tự học
- Gap lớn nhất: kỳ vọng “thông minh” nhưng trải nghiệm thực tế còn hạn chế, đặc biệt khi AI không chắc hoặc sai


## Sketch
(Ảnh đính kèm: sketch.jpg)
As-is:
- User hỏi thông tin phức tạp → chatbot trả lời chung chung hoặc im lặng
- User phải thử lại nhiều lần hoặc gọi hotline → mất thời gian
To-be:
- Khi AI không chắc → chatbot hiển thị 2–3 gợi ý kèm confidence %
- Có nút “Chuyển sang nhân viên hỗ trợ” rõ ràng ngay trong khung chat
- Thêm disclaimer: “Thông tin này có thể chưa chính xác, vui lòng xác nhận”
