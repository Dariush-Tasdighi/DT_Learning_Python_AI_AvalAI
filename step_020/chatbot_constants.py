"""
Chatbot Constants
"""

# **********
API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# **********

# **********
# MODEL_NAME: str = "gpt-4o"
# MODEL_NAME: str = "gpt-4o-mini"
MODEL_NAME: str = "gpt-3.5-turbo"
# MODEL_NAME: str = "gpt-3.5-turbo-instruct"
# **********

# **********
SYSTEM_PROMPT: str = "You are a helpful AI assistant."
SYSTEM_MESSAGE = {"role": "system", "content": SYSTEM_PROMPT}
# **********

if __name__ == "__main__":
    print("You must run 'chatbot.py' file!")
