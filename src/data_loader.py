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
        
    def load_from_api(self, url: str) -> pd.DataFrame:
        # xử lý trả về dạng DataFrame
        pass

    def crawl_from_web(self, url: str) -> pd.DataFrame:
        # xử lý trả về dạng DataFrame
        pass
