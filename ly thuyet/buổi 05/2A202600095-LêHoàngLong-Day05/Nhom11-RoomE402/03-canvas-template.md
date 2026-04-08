# AI Product Canvas — template

Điền Canvas cho product AI của nhóm. Mỗi ô có câu hỏi guide — trả lời trực tiếp, xóa phần in nghiêng khi điền.

---

## Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi guide** | User nào? Pain gì? AI giải quyết gì mà cách hiện tại không giải được? | Khi AI sai thì user bị ảnh hưởng thế nào? User biết AI sai bằng cách nào? User sửa bằng cách nào? | Cost bao nhiêu/request? Latency bao lâu? Risk chính là gì? |
| **Trả lời** | Khách hàng Vietnam Airlines cần tra cứu chuyến bay nhanh, 24/7. Pain: hotline quá tải, website khó tra cứu. AI chatbot giúp trả lời tức thì, tiện lợi. | Nếu AI sai → user có thể lỡ chuyến, mất niềm tin. User nhận ra khi thông tin không khớp. Hiện tại phải gõ lại hoặc gọi hotline để sửa. | Chi phí thấp (text query), latency vài giây. Risk: thông tin sai lệch gây mất uy tín, ảnh hưởng trải nghiệm khách hàng. |


---

## Automation hay augmentation?

**Augmentation:** — AI gợi ý, user quyết định cuối cùng.
**Justify:** Nếu AI sai mà user không biết → automation nguy hiểm. Augmentation cho phép AI đưa gợi ý, nhưng user vẫn xác nhận qua nhân viên hoặc hệ thống chính thức.



---

## Learning signal

| # | Câu hỏi | Trả lời |
|---|---------|---------|
| 1 | User correction đi vào đâu? | Khi user chọn “chuyển sang nhân viên” hoặc sửa câu hỏi, hệ thống ghi lại để cải thiện. |
| 2 | Product thu signal gì để biết tốt lên hay tệ đi? | Tỷ lệ user bỏ cuộc, số lần fallback sang hotline, mức độ hài lòng. |
| 3 | Data thuộc loại nào? ☐ User-specific · ☐ Domain-specific · ☐ Real-time · X Human-judgment · ☐ Khác: ___ | |

**Có marginal value không?** Có. Vì dữ liệu hội thoại khách hàng của Vietnam Airlines mang tính domain-specific, không phải ai cũng thu được.
___

Tóm lại: Chatbot NEO hiện mạnh ở khả năng trả lời đúng, nhưng yếu ở việc xử lý khi không chắc. Giải pháp là minh bạch hơn (confidence score, gợi ý, fallback rõ ràng) và coi AI như công cụ augmentation thay vì automation.

---


*AI Product Canvas — Ngày 5 — VinUni A20 — AI Thực Chiến · 2026*
