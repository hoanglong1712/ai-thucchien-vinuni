
# Yêu cầu
## Nguyễn Việt Phương (VSF-AITB-AICRB) 6/15 4:50 PM

1 - tạo ra 1 điểm số để đánh giá tổng quan conflict pipeline có tốt không

2 - bỏ hightlight theo char, hight light theo line thôi

3- đọc thêm paper trong industry tìm các cách phát hiện conflict

## Nguyễn Việt Phương (VSF-AITB-AICRB) 6/15 5:13 PM

Anh em nhớ ưu tiên có điểm số dạng như BLEU nha, vì LLM as a judge dễ hallucinate, có thể có 2 bộ điểm khác nhau cũng được nha, 1 cái dạng truyền thống 1 cái dạng dùng LLM Everyone

## Nguyễn Việt Phương (VSF-AITB-AICRB) 6/16 10:35 AM

Nguyen Ngoc Cuong (S.AI.20K)
6/16/2026 10:03 AM
từ input trên, mình cần làm gì ạ?

là em dùng nó để nghĩ ra 1 metric đánh giá xem các conflict được phát hiện ra có đúng k?
 
ví dụ em có chunk A, và chunk B conflict với nhau, đúng thì điểm sao, sai thì điểm sao.
nhưng cái câu conflict có tồn tại ở 2 chunk đó k? chunk A overlap chunk B đủ để phát hiện k? Điểm số?
 
Lý do conflict có ok ko? Có giúp người dùng phát hiện được vị trí conflict k? Điểm số?
 
--> Mục đích là để làm sao chúng ta có cái nhìn tổng quan, so sánh các lõi pipeline phát hiện conflict, trước khi người vào verify

# Kết quả công việc đã tiến hành
## tạo ra 1 điểm số để đánh giá tổng quan conflict pipeline có tốt không
 - Nguồn dữ liệu mẫu đầu vào được cung cấp tại : https://devel-coretech-bucket.s3.ap-southeast-1.amazonaws.com/sonnh95/intern/ResearchMetrics.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS2XOJSZJDY7MOLUX%2F20260615%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20260615T104527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d2d4ae5dc33f328b5eeb7f5d9e45c5c3b9a9e5f23ebde57e939edafd78912522
 - Phương pháp đánh giá được mô tả tại: https://www.overleaf.com/project/6a350704055a29c6db5ff1be
 - Kết quả thu được từ nguồn dữ liệu mẫu: https://docs.google.com/spreadsheets/d/1YBednFD8BcemORiXilwvjPq_diFgg_MiyRgkCPwLsvo/edit?usp=sharing
 - Các bước tiến hành bao gồm:
   - Phát hiện xem các khẳng định được trích dẫn có tồn tại bên trong tập tin được trích dẫn và tại dòng được trích dẫn hay không.
   - 
