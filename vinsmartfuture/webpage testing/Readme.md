# Yêu cầu công việc
- Thực hiện các nội dung kiểm thử có trong testcases_check_conflicts.csv thông qua sử dụng thư viện automation test dùng agent
- Trang web cần kiểm thử: https://vin-service-platform.hotavn.com/auth/login
  
# Kết quả công việc
- Đã sử dụng LLM để sinh các nội dung kiểm thử chi tiết phù hợp với framework browser_use từ testcases_check_conflicts.csv
- Đã thực hiện việc sử dụng framework browser_use để kiểm thử 1 số trường hợp
- Kết quả lưu tại testing_result.txt

# Vấn đề và nguyên nhân của app hiện tại
- Vấn đề: Agent rất dễ bị sập.
- Nguyên nhân: cấu hình mô hình chạy local qua Ollama với mô hình gemma4:e2b.
  - browser-use đòi hỏi mô hình ngôn ngữ lớn (LLM) phải có khả năng hiểu cấu trúc cây DOM cực kỳ tốt và sinh ra định dạng JSON/Tool call chuẩn xác.
  - Các mô hình SLM (Small Language Model) hoặc Local Model nhỏ chạy qua Ollama rất hay bị hiện tượng trả về chuỗi rỗng, không thể gọi tool, hoặc gặp vòng lặp vô hạn (Infinite Loop) dẫn tới timeout 180 giây ngay ở bước 1.
- Cách giải quyết:
  - Cần có nguồn lực máy tính đủ mạnh để có thể chạy được mô hình LLM với lượng tham số đủ lớn.


--------------------------

4:15 chiều thứ 4 1-7-2026
