import os

from langchain_community.document_loaders import Docx2txtLoader

from src.loaders.base_loader import BaseLoader


class DocxLoader(BaseLoader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not self.file_path.lower().endswith(".docx"):
            raise ValueError(
                "Only DOCX files are supported."
            )

    def load(self):
        self.validate_file()

        loader = Docx2txtLoader(self.file_path)

        documents = loader.load()

        return documents
