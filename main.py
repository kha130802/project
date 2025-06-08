from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.data_splitter import DataSplitter
from src.visualizer import Visualizer

def main():
    loader = DataLoader("api")
    # df = loader.load_from_api("https://api.example.com/data")
    file_path = r'ĐƯỜNG DẪN CỦA BẠN demo.csv'
    df = loader.load_from_csv(file_path)
    
    cleaner = DataCleaner(df)
    cleaner.drop_nulls()
    cleaner.convert_types({'price': float, 'date': 'datetime64'})
    df_clean = cleaner.get_clean_data()

    df_clean.to_csv("data/processed/clean_data.csv", index=False)

    visualizer = Visualizer(df_clean)
    visualizer.plot_histogram("price")
    visualizer.plot_time_series("date", "price")

if __name__ == "__main__":
    main()
