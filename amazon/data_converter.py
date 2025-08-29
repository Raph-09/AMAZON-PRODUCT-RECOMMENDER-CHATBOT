import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self,file_path:str):
        self.file_path = file_path

    def convert(self):
        df = pd.read_csv(self.file_path)[["title_y","text"]]   

        docs = [
            Document(page_content=str(row['text']) if pd.notna(row['text']) else "" , metadata = {"product_name" : row["title_y"]})
            for _, row in df.iterrows()
        ]

        return docs




