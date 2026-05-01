import os
from dotenv import load_dotenv, find_dotenv

# This will find the .env file automatically in your project
load_dotenv(find_dotenv())

print("API Key:", os.getenv("MY_API_KEY"))

