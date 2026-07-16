"""
Application Configuration
-------------------------

This module centralizes all configurable settings for the project.

Any module needing configuration should import values from here
instead of hardcoding them.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===============================
# API Configuration
# ===============================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ===============================
# LLM Configuration
# ===============================

MODEL_NAME = "gemini-2.5-flash"

TEMPERATURE = 0.3

# ===============================
# Text Splitting
# ===============================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ===============================
# Retriever
# ===============================

TOP_K = 4

# ===============================
# File Paths
# ===============================

VECTOR_DB_PATH = "vector_store"

LOG_PATH = "logs"

CACHE_PATH = "cache"

DATA_PATH = "data"

# ===============================
# Supported Files
# ===============================

SUPPORTED_FILES = [".pdf"]