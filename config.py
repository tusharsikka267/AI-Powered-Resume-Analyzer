import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/resumematch")
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
