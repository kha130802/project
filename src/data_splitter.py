import pandas as pd
class DataSplitter:
    '''
    (Tuỳ chọn) Tách thành từng bản nhỏ và lưu thành file. 
    Mục đích: lần sau không cần đọc và xử lý lại dữ liệu thô
    '''

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def split_columns_to_file(self, columns, output_dir, file_format='csv'):
        """
        Tách nhiều cột cùng lúc và lưu vào file với định dạng tùy chọn.
        Args:
            columns (list or str): Danh sách tên cột hoặc tên cột cần tách.
            output_dir (str): Thư mục để lưu file.
            file_format (str): Định dạng file ('csv', 'json', 'xlsx').
        """
