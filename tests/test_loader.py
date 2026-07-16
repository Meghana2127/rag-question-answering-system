from src.loaders.loader_factory import LoaderFactory


file_path = "data/sample.pdf"

loader = LoaderFactory.get_loader(file_path)

documents = loader.load()

print(f"Total Documents : {len(documents)}")

print("\n========== First Document ==========\n")

print(documents[0].page_content)

print("\n========== Metadata ==========\n")

print(documents[0].metadata)