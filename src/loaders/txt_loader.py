import os

from langchain_community.document_loaders import TextLoader

from src.loaders.base_loader import BaseLoader


class TxtLoader(BaseLoader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not self.file_path.lower().endswith(".txt"):
            raise ValueError(
                "Only TXT files are supported."
            )

    def load(self):
        self.validate_file()

        loader = TextLoader(self.file_path)

        documents = loader.load()

        return documents