from ddgs import DDGS
import re

class SearchHandler:
    def __init__(self):
        self.ddgs = DDGS()

    def search_vinfast_info(self, query):
        """
        Tìm kiếm thông tin VinFast dựa trên query.
        Trả về chuỗi tóm tắt kết quả.
        """
        results = self.ddgs.text(f"VinFast {query}", max_results=3)
        if not results:
            return "Không tìm thấy thông tin cụ thể trên mạng."
        
        info_summary = []
        for r in results:
            info_summary.append(f"- {r['title']}: {r['body']}")
            
        return "\n".join(info_summary)

    def get_car_image(self, model_name):
        """
        Tìm kiếm ảnh xe. (Trong prototype này, trả về URL ảnh mô phỏng nếu không tìm được)
        """
        # Thử tìm ảnh thật qua DDG Images
        try:
            results = self.ddgs.images(f"VinFast {model_name} white background", max_results=1)
            if results:
                return results[0]['image']
        except:
            pass
        
        # Fallback ảnh mẫu
        return "https://vinfastauto.com/themes/custom/vinfast_v2/images/logo.png"
