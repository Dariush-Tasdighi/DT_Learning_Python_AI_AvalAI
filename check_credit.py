# **************************************************
API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# **************************************************

# **************************************************
import os
import requests
from dotenv import load_dotenv

os.system(command="cls")

load_dotenv()

api_key: str | None = os.getenv(key=API_KEY_NAME)
if not api_key:
    print("API Key not found!")
    exit()

authorization = f"Bearer {api_key}"

api_url = "https://api.avalai.ir/user/credit"

headers = {
    "Content-Type": "application/json",
    "Authorization": authorization,
}

response = requests.get(url=api_url, headers=headers)

print(response.json())
print()
# **************************************************
