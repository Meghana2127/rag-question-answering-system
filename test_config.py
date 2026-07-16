from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

print("API Key Loaded:", GOOGLE_API_KEY is not None)
print("Model:", MODEL_NAME)
print("Chunk Size:", CHUNK_SIZE)
print("Chunk Overlap:", CHUNK_OVERLAP)