# Prototype — VinFast EV Sales Consultant

## Mô tả
Chatbot tích hợp Telegram phục vụ tư vấn bán xe điện VinFast. Bot có khả năng từ chối các câu hỏi ngoài lề, lái chủ đề từ đối thủ (Tesla, BYD) về VinFast, tra cứu giá/ảnh/mô tả thực tế từ web và đánh giá khả năng tài chính của người dùng trước khi chuyển giao cho nhân viên Sales.

## Level: Working Prototype
- **AI chạy thật**: Sử dụng mô hình **Qwen3 (5.2 GB)** chạy local qua Ollama.
- **Tương tác thật**: Người dùng nhắn tin trực tiếp trên Telegram và nhận phản hồi thực tế.
- **Dữ liệu thật**: Tích hợp Search engine (ddgs) để lấy thông tin giá và ảnh xe thực tế từ Internet.

## Links
- **GitHub Repo**: [Link tới repo nhóm]
- **Script chính**: `bot.py`
- **Logic LLM**: `llm_handler.py`
- **Web Search**: `search_handler.py`

## Tools và API
- **LLM Engine**: Ollama (model Qwen3:latest)
- **Telegram SDK**: `python-telegram-bot`
- **Search API**: `ddgs` (DuckDuckGo Search)
- **Environment**: Python 3.13, `python-dotenv`

## Phân công
| Thành viên | Vai trò | Đóng góp cụ thể |
|-----------|------|--------|
| **AI Lead** | Architecture & AI | Thiết kế logic LLM, System Prompt xử lý kịch bản 6 bước và tích hợp Ollama. |
| **Developer** | Integration | Xây dựng Telegram Bot, quản lý session người dùng và xử lý các sự kiện (typing, reply photo). |
| **Product/Data** | Search & Spec | Xây dựng module Search thông tin xe, tinh chỉnh dữ liệu đầu vào và viết SPEC tài liệu. |
