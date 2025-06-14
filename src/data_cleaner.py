import pandas as pd
class DataCleaner:
    '''
        Lớp xử lý làm sạch, ép kiểu dữ liệu
''' 
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def drop_nulls(self, columns: list = None):
        """
        Xóa các hàng có giá trị null trong DataFrame.
        Nếu columns được cung cấp, chỉ xóa các hàng có giá trị null trong các cột đó.
        """
        if columns:
            self.df.dropna(subset=columns, inplace=True)
        else:
            self.df.dropna(inplace=True)