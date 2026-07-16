import os

from src.loaders.pdf_loader import PDFLoader
from src.loaders.docx_loader import DocxLoader
from src.loaders.txt_loader import TxtLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return PDFLoader(file_path)

        elif extension == ".docx":
            return DocxLoader(file_path)

        elif extension == ".txt":
            return TxtLoader(file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )