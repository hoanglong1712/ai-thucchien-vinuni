
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
## Tạo ra 1 điểm số để đánh giá tổng quan conflict pipeline có tốt không
 - Nguồn dữ liệu mẫu đầu vào được cung cấp tại : https://devel-coretech-bucket.s3.ap-southeast-1.amazonaws.com/sonnh95/intern/ResearchMetrics.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS2XOJSZJDY7MOLUX%2F20260615%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20260615T104527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d2d4ae5dc33f328b5eeb7f5d9e45c5c3b9a9e5f23ebde57e939edafd78912522
 - Phương pháp đánh giá được mô tả tại: https://www.overleaf.com/project/6a350704055a29c6db5ff1be
 - Kết quả thu được từ nguồn dữ liệu mẫu:
   - Tập tin kết quả: https://docs.google.com/spreadsheets/d/1YBednFD8BcemORiXilwvjPq_diFgg_MiyRgkCPwLsvo/edit?usp=sharing
   - Tóm tắt kết quả: phát hiện 1 số khẳng định không có liên hệ ngữ nghĩa hay từ vựng với văn bản được trích dẫn. Đánh giá được chất lượng xung đột giữa 2 câu khẳng định thông qua độ liên quan từ vựng giữa 2 câu và mức xung đột ngữ nghĩa giữa 2 câu, phản ánh đúng và đủ chất lượng tìm kiếm xung đột của mô hình đang được sử dụng.
 - Các bước tiến hành bao gồm:
   - Phát hiện xem các khẳng định được trích dẫn có tồn tại bên trong tập tin được trích dẫn và tại dòng được trích dẫn hay không.
   - Tính "overlap score" thông qua lấy trung bình cộng của khoảng cách cosin giữa 2 khẳng định và giá trị IoU "Intersection over Union, aka Jaccard Index" cho unigram.
   - Tính điểm xung đột giữa 2 khẳng định và tính điểm giải thích nguyên nhân xung đột thông qua sử dụng mô hình Qwen2.5-14B-Instruct-GGUF
   - Tổng hợp điểm vào điểm số cuối cùng
 - Các tập tin mã nguồn
   - Chuyển đổi tập tin xlsx thành tập tin json: https://www.kaggle.com/code/lvttct/vsf-benchmark-conflict-xlsx-to-json
   - Sử dụng mô hình gemma-2-2b-it-GGUF để kiểm tra xem khẳng định có thực sự tòn tại trong tập tin văn bản hay không, dù dưới dạng từ vựng hay dưới dạng ngữ nghĩa nhằm xác định các trích dẫn sai lầm: https://www.kaggle.com/code/lvttct/vsf-benchmark-conflict-text-in-data-source
   - Sử dụng mô hình SBERT "dangvantuan/vietnamese-embedding" dành riêng cho Tiếng Việt để tính độ lệch cosine giữa cac khẳng định: https://www.kaggle.com/code/lvttct/vsf-benchmark-conflicted-similarity-23-6-2026
   - Sử dụng mô hình Qwen2.5-14B-Instruct-GGUF để điểm xung đột giữa 2 khẳng định và tính điểm giải thích nguyên nhân xung đột: https://www.kaggle.com/code/lvttct/vsf-benchmark-conflicted-text-testing-22-6-2026
   - Tổng hợp thông tin và xuất ra tập tin xlsx
    - https://www.kaggle.com/code/lvttct/vsf-benchmark-conflicted-iou-24-6-2026
    - https://www.kaggle.com/code/lvttct/vsf-conflicted-benchmarking-conclusion-24-6-2026
    - https://www.kaggle.com/code/lvttct/vsf-conflicted-benchmarking-to-xlsx-24-6-2026

## Yêu cầu điểm số dạng BLEU
 - Qua khảo sát thực tế nhận thấy điểm cốt lõi khiến BLEU (Bilingual Evaluation Understudy) không phù hợp cho các tập dữ liệu chứa các cặp văn bản xung đột (conflicted text pairs) nằm ở bản chất thuật toán của nó: BLEU được thiết kế để đo lường độ trùng lặp bề mặt (n-gram overlap), chứ không phải ngữ nghĩa (semantics).
 - Giải pháp thay thế: Metric dựa trên Embedding (Ngữ nghĩa) đã được ứng dụng trong mục trên.

##  Một số paper trong industry tìm các cách phát hiện conflict phù hợp với yêu cầu hiện tại
### Joint Semantic Analysis with Knowledge Graphs for Fact-Checking 
   - Thay vì chỉ so khớp văn bản, hướng xử lý này trích xuất văn bản thành các cặp Thực thể - Quan hệ - Thực thể (S-P-O triples) rồi đối chiếu trên Đồ thị tri thức (Knowledge Graph). Nếu hai quan hệ của cùng một thực thể xung đột lẫn nhau (ví dụ: [A, sinh_tại, B] và [A, sinh_tại, C]), hệ thống sẽ cắm cờ xung đột ngay lập tức. https://arxiv.org/html/2505.14714v1
   - Cơ chế hoạt động:
     - Phân tách thông qua ngữ nghĩa: sử dụng mô hình ngôn ngữ lớn để phân tách các khẳng định thành dạng Subject-Predicate-Object. https://arxiv.org/html/2312.11785v1
     - Kết nối các thực thể với nhau trên đồ thị tri thức, nhóm các thực thể diễn đạt 1 đối tượng vào 1 đỉnh. Ví dụ : TP Hồ Chí Minh = Sài Gòn = Gia Định = Phiên An.  

