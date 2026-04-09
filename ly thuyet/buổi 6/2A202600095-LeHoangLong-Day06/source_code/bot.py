import logging
import re
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
from llm_handler import LLMHandler
from search_handler import SearchHandler
from dotenv import load_dotenv

# Tải cấu hình từ .env
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Cấu hình logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

llm = LLMHandler()
searcher = SearchHandler()

# Lưu trữ hội thoại của người dùng
user_sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_sessions[user_id] = llm.get_initial_messages()
    await update.message.reply_text("Chào mừng bạn đến với VinFast EV Consultant! Tôi có thể giúp gì cho bạn về các dòng xe điện VinFast?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    
    # Gửi thông báo đang xử lý
    await update.message.reply_text("Nhân viên tư vấn đang suy nghĩ về câu hỏi của bạn, chúng tôi dùng CPU nên tốc độ khá chậm.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    if user_id not in user_sessions:
        user_sessions[user_id] = llm.get_initial_messages()
    
    messages = user_sessions[user_id]
    messages.append({"role": "user", "content": user_text})
    
    # Gửi tới LLM lần 1
    response_text = llm.get_response(messages)
    
    # Kiểm tra nếu LLM yêu cầu tìm kiếm
    match = re.search(r"\[SEARCH:\s*(.*?)\]", response_text)
    if match:
        query = match.group(1)
        # Thông báo đang tìm kiếm
        await update.message.reply_text(f"🔍 Đang tìm kiếm thông tin về '{query}' trên mạng...")
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        
        search_results = searcher.search_vinfast_info(query)
        
        # Cập nhật context với kết quả tìm kiếm
        messages.append({"role": "assistant", "content": response_text})
        messages.append({"role": "user", "content": f"Kết quả tìm kiếm cho '{query}':\n{search_results}\n\nHãy tổng hợp lại và trả lời người dùng. Nhớ kèm ảnh nếu là thông tin về mẫu xe."})
        
        # Gửi tới LLM lần 2 để tổng hợp
        await update.message.reply_text("✨ Đang tổng hợp thông tin để trả lời bạn...")
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        final_response = llm.get_response(messages)
        messages.append({"role": "assistant", "content": final_response})
    else:
        final_response = response_text
        messages.append({"role": "assistant", "content": final_response})

    # Xử lý gửi ảnh nếu LLM nhắc tới các mẫu xe VF
    car_models = ["VF e34", "VF 3", "VF 5", "VF 6", "VF 7", "VF 8", "VF 9"]
    for model in car_models:
        if model.lower() in final_response.lower() and "định dạng" not in final_response.lower():
            image_url = searcher.get_car_image(model)
            try:
                await update.message.reply_photo(photo=image_url, caption=f"Hình ảnh minh họa {model}")
            except Exception as e:
                logging.error(f"Error sending photo: {e}")
            break

    # Gửi phản hồi văn bản cuối cùng
    await update.message.reply_text(final_response)

if __name__ == '__main__':
    if not BOT_TOKEN:
        print("Vui lòng cung cấp TELEGRAM_BOT_TOKEN trong file .env")
    else:
        application = ApplicationBuilder().token(BOT_TOKEN).connect_timeout(60).read_timeout(60).build()
        
        start_handler = CommandHandler('start', start)
        msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
        
        application.add_handler(start_handler)
        application.add_handler(msg_handler)
        
        print("Bot đang chạy...")
        application.run_polling()
