# data_loader.py
import pandas as pd
class DataLoader:
    '''
        Lớp đọc và load dữ liệu từ web/api/csv
        Chọn hình thức thích hợp để có được dữ liệu thô
        Có thể chọn nhiều cách để có dữ liệu thích hợp
    '''

    def __init__(self, source: str):
        self.source = source

    def load_from_csv(self, path: str) -> pd.DataFrame:
        # xử lý trả về dạng DataFrame
        # ví dụ
        try:
            df = pd.read_csv(path)
            print(f"Đã tải thành công dữ liệu từ: {path}")
            return df
        except FileNotFoundError:
            print(f"Lỗi: Không tìm thấy file tại đường dẫn '{path}'")
            return pd.DataFrame() # df rỗng
