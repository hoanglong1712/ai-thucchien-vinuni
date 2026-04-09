# SPEC — AI Product Hackathon

**Nhóm:** VinFast EV Experts
**Track:** 🔘 VinFast · ☐ Vinmec · ☐ VinUni-VinSchool · ☐ XanhSM · ☐ Open
**Problem statement (1 câu):** Khách hàng mua xe điện VinFast thường lo lắng về giá cả và hạ tầng sạc, đồng thời dễ bị phân tâm bởi các hãng đối thủ; giải pháp là một "Trợ lý ảo bán hàng" cung cấp thông tin thời gian thực và khéo léo định hướng người dùng quay lại với thế mạnh của VinFast.

---

## 1. AI Product Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi** | Ai? Pain gì? AI giải gì? | Khi AI sai thì sao? User sửa bằng cách nào? | Cost/latency bao nhiêu? Risk chính? |
| **Trả lời** | Người mua xe VinFast cần thông tin nhanh, chính xác. AI giúp tra cứu giá/khuyến mãi tức thì và lái chủ đề từ hãng đối thủ về chủ đề VinFast. | AI có thể trả lời sai giá. User được khuyến cáo liên hệ Sales để "chốt đơn". Hệ thống thu thông tin qua việc tìm kiếm trên mạng để giảm ảo giác, cung  cấp thông tin sai sự thật. | Độ trễ ~10-20s (local model). Chi phí thấp (chạy CPU). Risk: Lỗi kết nối khi tìm kiếm thông tin trực tuyến hoặc LLM phản hồi chậm. |

**Automation hay augmentation?** ☐ Automation · 🔘 Augmentation
Justify: AI đóng vai trò là "phễu" lọc khách hàng tiềm năng và cung cấp thông tin sơ bộ trước khi chuyển giao cho nhân viên tư vấn thật ("Augmentation" hỗ trợ cho đội ngũ bán hàng).

**Learning signal:**

1. User correction đi vào đâu? Nhật ký hội thoại (Logs) được dùng để tinh chỉnh System Prompt.
2. Product thu signal gì để biết tốt lên hay tệ đi? Tỷ lệ người dùng chấp nhận chuyển thông tin cho Sales.
3. Data thuộc loại nào? 🔘 Domain-specific · 🔘 Real-time · ☐ Human-judgment
   Có marginal value không? Có, mô hình cần liên tục cập nhật giá xe và trạm sạc mới nhất qua việc tìm kiếm trên mạng viễn thông.

---

## 2. User Stories — 4 paths

### Feature: Tra cứu thông tin xe & Lái chủ đề (Pivot)

**Trigger:** Người dùng hỏi về giá xe VinFast hoặc so sánh với hãng xe điện khác.

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | User hỏi giá VF8, AI kết nối web, trả về giá đúng kèm ảnh. User hài lòng và hỏi tiếp về sạc. |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? | AI báo "Tôi đang tìm kiếm thêm thông tin..." và yêu cầu tìm kiếm lại với từ khóa khác nếu kết quả đầu tiên mờ nhạot. |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | AI báo sai giá xe cũ. User thấy khác biệt so với thông tin chính thức → AI xin lỗi và đề xuất gọi đường dây nóng cho nhân viên bán hàng. |
| Correction — user sửa | User sửa bằng cách nào? | User nhắn: "Giá này sai rồi, hiện tại đang giảm 50tr". AI nhận thông tin, xác nhận lại qua thông tin tìm kiếm trên mạng và cập nhật hội thoại. |

---

## 3. Eval metrics + threshold

**Optimize precision hay recall?** 🔘 Precision · ☐ Recall
Tại sao? Trong bán hàng, việc đưa ra thông tin sai về giá hoặc khuyến mãi gây mất lòng tin nghiêm trọng hơn việc nói "Tôi sẽ kiểm tra lại".

| Metric | Threshold | Red flag (dừng khi) |
|--------|-----------|---------------------|
| Tỷ lệ trích xuất đúng giá xe từ Web Search | ≥ 90% | < 70% |
| Tỷ lệ lái chủ đề thành công (Pivot rate) | ≥ 80% | < 50% |
| Thời gian phản hồi (Latency) | < 30s | > 60s (User sẽ bỏ cuộc) |

---

## 4. Top 3 failure modes

| # | Trigger | Hậu quả | Mitigation |
|---|---------|---------|------------|
| 1 | Web Search trả về kết quả từ trang tin cũ (2023) | AI cung cấp thông tin giá/khuyến mãi hết hạn | Thêm "current year" vào query search và hướng dẫn LLM kiểm tra kỹ mốc thời gian. |
| 2 | Người dùng cố tình hỏi về chính trị/tôn giáo | AI trả lời lạc đề, gây rủi ro thương hiệu | Cài đặt Guardrails nghiêm ngặt trong System Prompt để từ chối mọi chủ đề ngoài ô tô điện. |
| 3 | LLM bị lặp từ hoặc lag do CPU quá tải | Trải nghiệm người dùng cực tệ, bot không phản hồi | Thêm thông báo "Nhân viên đang suy nghĩ..." và tối ưu hóa model (Quantization). |

---

## 5. ROI 3 kịch bản

|   | Conservative | Realistic | Optimistic |
|---|-------------|-----------|------------|
| **Assumption** | 10 user/ngày, 1 người quan tâm thật | 50 user/ngày, 5 người quan tâm thật | 200 user/ngày, 20 người quan tâm thật |
| **Cost** | 0$ (Chạy local CPU) | 20$/tháng (Cloud nhỏ) | 100$/tháng (GPU dedicated) |
| **Benefit** | Giảm 1h/ngày cho Sales | Giảm 4h/ngày, tăng 5% lead | Giảm 10h/ngày, tăng 15% lead |
| **Net** | Tiết kiệm thời gian | ROI dương sau 1 tháng | Đột phá doanh số lead |

**Kill criteria:** Chi phí vận hành Cloud vượt quá giá trị của 1 đơn hàng mang lại hoặc tỷ lệ ảo giác về giá xe vượt quá 30%.

---

## 6. Mini AI spec (1 trang)

### 6.1. Tầm nhìn Sản phẩm (Product Vision)
VinFast AI Consultant không chỉ đơn thuần là một chatbot hỗ trợ khách hàng, mà là một **"Lead Generation & Preservation Engine"** (Công cụ tạo và giữ chân khách hàng tiềm năng). Trong thị trường xe điện (EV) đầy sôi động với sự thâm nhập mạnh mẽ của các thương hiệu quốc tế như Tesla và BYD, rào cản lớn nhất của khách hàng không chỉ là giá cả mà còn là sự tin tưởng vào hệ sinh thái sạc và dịch vụ hậu mãi. Sản phẩm này ra đời để trở thành điểm chạm đầu tiên 24/7, giúp giải quyết tức thì các "điểm đau" (pain points) của người dùng về thông tin trước khi họ có cơ hội bị lôi kéo bởi những thông tin tiếp thị từ đối thủ cạnh tranh.

### 6.2. Chiến lược xử lý phản đối & Kỹ thuật "Lái chủ đề" (Pivot Logic)
Điểm khác biệt cốt lõi của giải pháp nằm ở **Chiến lược Pivot thông minh**. Thay vì phủ định các ưu điểm của đối thủ cạnh tranh một cách trực diện (dễ gây phản cảm và thiếu khách quan), AI được thiết kế để tuân thủ quy trình xử lý phản đối chuyên nghiệp:
1.  **Xác nhận (Acknowledge)**: Đồng ý với những điểm mạnh mang tính toàn cầu của đối thủ (ví dụ: công nghệ tự lái của Tesla hoặc chuỗi cung ứng pin của BYD).
2.  **Chuyển hướng (Pivot)**: Khéo léo dẫn dắt người dùng về các giá trị "độc bản" mà chỉ VinFast mới có thể cung cấp tại thị trường Việt Nam (Hệ thống hơn 150.000 cổng sạc trên toàn bộ 63 tỉnh thành, xưởng dịch vụ rộng khắp, cứu hộ 24/7 tận nơi).
3.  **Chốt đơn (Conversion)**: Đưa ra lời đề nghị hỗ trợ tài chính hấp dẫn (vay 80%, trả góp 8 năm) và kết nối trực tiếp với chuyên viên tư vấn con người khi cảm thấy người dùng đã sẵn sàng mua xe.

### 6.3. Kiến trúc RAG thời gian thực & Kiểm soát ảo giác
Để đảm bảo tính **Feasibility (Khả thi)** và **Trust (Tin cậy)**, hệ thống sử dụng kiến trúc **Real-time RAG** (Retrieval-Augmented Generation) thay vì chỉ dựa vào kiến thức tĩnh của mô hình:
-   **Local LLM (Qwen3)**: Đảm bảo quyền riêng tư tuyệt đối cho dữ liệu khách hàng và tối ưu hóa chi phí vận hành cho doanh nghiệp (0$ chi phí API hàng tháng).
-   **Dynamic Search Integration**: Tích hợp công cụ tìm kiếm trực tiếp trên mạng để lấy thông tin giá lăn bánh, thông số các dòng xe mới nhất (VF3, VF6, VF7). Điều này giúp loại bỏ hoàn toàn rủi ro AI "hallucinate" (ảo giác) về giá xe cũ hoặc các chương trình khuyến mãi đã hết hạn - vấn đề nan giải nhất của các chatbot AI hiện nay.

### 6.4. Chiến lược UX cho phần cứng giới hạn (CPU Optimization)
Nhận diện rào cản về tốc độ xử lý khi chạy mô hình ngôn ngữ lớn (5.2GB) trên phần cứng CPU thông thường, chúng tôi triển khai chiến lược **"Minh bạch hóa quá trình suy nghĩ"**:
-   Hệ thống liên tục gửi các tin nhắn trạng thái trung gian (Đang tìm kiếm thông tin..., Đang tổng hợp câu trả lời...) kết hợp với trạng thái "Typing..." của Telegram. 
-   Kỹ thuật này biến "thời gian chờ đợi" thành một trải nghiệm có tương tác, giúp người dùng cảm thấy chatbot đang làm việc thực sự nghiêm túc và chuyên nghiệp thay vì cảm giác bị treo máy hoặc phản hồi chậm.

### 6.5. Bánh đà dữ liệu & Lộ trình tương lai
Mỗi cuộc hội thoại là một tín hiệu học tập (Learning Signal) vô giá cho doanh nghiệp. Trong tương lai, hệ thống sẽ tự động tổng hợp các "phản đối" (objections) phổ biến nhất của người dùng từ logs để cập nhật lại Knowledge Base cho toàn bộ đội ngũ bán hàng. Đây chính là "bánh đà" (flywheel) giúp VinFast không ngừng tối ưu hóa kịch bản chốt đơn, biến AI từ một công cụ hỗ trợ kỹ thuật thành một tài sản tri thức chiến lược, giúp hiện thực hóa sứ mệnh xanh hóa giao thông tại Việt Nam.
