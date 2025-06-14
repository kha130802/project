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
    def convert_types(self, type_dict: dict):
        """
        Chuyển đổi kiểu dữ liệu của các cột trong DataFrame.
        
        Args:
            type_dict (dict): Từ điển với tên cột là khóa và kiểu dữ liệu là giá trị.
        """
        for column, dtype in type_dict.items():
            if column in self.df.columns:
                self.df[column] = self.df[column].astype(dtype)
            else:
                print(f"Cột {column} không tồn tại trong DataFrame.")