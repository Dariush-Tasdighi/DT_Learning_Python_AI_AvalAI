import os
import requests
from dotenv import load_dotenv

os.system(command="cls")

load_dotenv()

api_key_name = "AVALAI_API_KEY"
api_key = os.getenv(key=api_key_name)
authorization = f"Bearer {api_key}"

api_url = "https://api.avalai.ir/user/credit"

headers = {
    "Content-Type": "application/json",
    "Authorization": authorization,
}

response = requests.get(url=api_url, headers=headers)

print(response.json())
print()