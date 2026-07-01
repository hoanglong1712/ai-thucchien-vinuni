import asyncio
import logging
from dotenv import load_dotenv

# import các thành phần cốt lõi từ package gốc browser_use
from browser_use import Agent, Browser, BrowserProfile, ChatOllama

load_dotenv()

# ====================== CẤU HÌNH LOGGING ======================
logger = logging.getLogger("CheckConflictsTest")
logger.setLevel(logging.INFO)
if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s'))
    logger.addHandler(console_handler)

# ====================== CẤU HÌNH LLM (OLLAMA) ======================
# Giữ nguyên cấu hình kết nối local model gemma4:e2b
llm = ChatOllama(
    model="gemma4:e2b",
    host="http://localhost:11434",
    timeout=360,
    ollama_options={"num_ctx": 81952}
)

async def run_test_suite():
    logger.info("Đang khởi tạo cấu hình Trình duyệt với BrowserProfile...")
    
    # 1. Khởi tạo BrowserProfile để lưu trữ session, cookies, giúp ghi nhớ trạng thái đăng nhập
    profile = BrowserProfile(
        headless=False,  # Mở trình duyệt có giao diện trực quan để dễ kiểm tra luồng chạy
        extra_chromium_args=["--window-size=1280,720"],
        page_readiness_timeout=60.0
    )
    
    # 2. Khởi tạo Browser và truyền đối tượng profile vào
    browser = Browser(browser_profile=profile)

    # Danh sách các kịch bản kiểm thử ánh xạ theo tệp Excel 
    test_cases = [
        {
            "name": "01_LOGIN_PRECONDITION",
            "task": """
            Go to https://vin-service-platform.hotavn.com/auth/login
            Nhập email 'lamviectaivinsmartfuture@gmail.com' vào ô nhập email.
            Nhập mật khẩu 'this_is_not_a_password' vào ô nhập mật khẩu.
            Click nút 'Đăng nhập' hoặc 'Login'.
            Chờ cho đến khi trang quản lý Knowledge Base tải xong hoàn toàn.
            """
        },
        {
            "name": "02_BUTTON_CHECK_POSITION",
            "task": """
            Đảm bảo trình duyệt đang ở giao diện màn hình Knowledge Base sau khi đã đăng nhập thành công.
            Tìm xem ở khu vực góc trên bên phải màn hình có nút mang tên 'Check conflicts' hay 'Kiểm tra xung đột' không.
            Nếu có, hãy trả về kết quả có chữ 'SUCCESS'.
            """
        },
        {
            "name": "03_PERFORM_SCAN_FULL_SCOPE",
            "task": """
            Tại giao diện Knowledge Base, hãy chắc chắn KHÔNG tích chọn bất kỳ ô checkbox nào của các file.
            Nhấn thẳng trực tiếp vào nút 'Check conflicts' hoặc 'Kiểm tra xung đột'.
            Xác nhận xem hệ thống có bắt đầu tiến trình quét toàn bộ file hay không.
            """
        }
    ]

    results = {}

    for tc in test_cases:
        logger.info(f"🚀 [RUNNING] Test Case: {tc['name']}")
        
        # Tạo Agent: Khi truyền 'browser=browser' đã được gán Profile, 
        # Agent sẽ tự động kế thừa và chia sẻ Session/Cookies của toàn bộ các bước trước đó.
        agent = Agent(
            task=tc['task'],
            llm=llm,
            browser=browser,
            use_thinking=True,
            llm_timeout=360,
            max_actions_per_step=1,
            max_failures=1,
        )
        
        try:
            # Thực thi tác vụ
            history = await agent.run()
            
            # Đánh giá kết quả thực tế từ lịch sử chạy của AgentHistory
            if history.is_done():
                final_res = history.final_result()
                if final_res and any(x in final_res.lower() for x in ["fail", "error", "not found"]):
                    results[tc['name']] = f"FAIL ({final_res})"
                    logger.error(f"❌ [FAILED] {tc['name']} gặp lỗi nghiệp vụ giao diện.")
                else:
                    results[tc['name']] = "PASS"
                    logger.info(f"✅ [PASSED] {tc['name']}")
            else:
                results[tc['name']] = "FAIL (Agent chưa hoàn thành chuỗi hành động và bị ngắt giữa chừng)"
                logger.error(f"❌ [FAILED] {tc['name']} bị dừng giữa chừng.")
                
        except Exception as e:
            results[tc['name']] = f"FAIL (Hệ thống gặp ngoại lệ: {str(e)})"
            logger.error(f"💥 [ERROR] {tc['name']} lỗi thực thi code: {str(e)}")
            
        await asyncio.sleep(2)  # Nghỉ ngắn giữa các bước giúp giao diện web ổn định trạng thái

    # ====================== XUẤT BÁO CÁO CUỐI CÙNG ======================
    logger.info("=" * 80)
    logger.info("TỔNG HỢP KẾT QUẢ KIỂM THỬ THỰC TẾ TRÊN HỆ THỐNG VSF")
    logger.info("=" * 80)
    for name, status in results.items():
        logger.info(f"{name:<30} → {status}")
    logger.info("=" * 80)

    # Đóng trình duyệt, giải phóng bộ nhớ RAM một cách an toàn
    await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test_suite())