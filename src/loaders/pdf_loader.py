import os

from langchain_community.document_loaders import PyPDFLoader

from src.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not self.file_path.lower().endswith(".pdf"):
            raise ValueError(
                "Only PDF files are supported."
            )
    def load(self):
        self.validate_file()

        loader = PyPDFLoader(self.file_path)

        documents = loader.load()

        return documents
        