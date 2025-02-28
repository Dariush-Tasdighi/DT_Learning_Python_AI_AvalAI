"""
Chatbot Constants
"""

# **********
BASE_URL: str = "https://api.avalai.ir/v1"
# **********

# **********
TEMPERATURE: float = 0.8
# **********

# **********
KEY_NAME_ROLE: str = "role".strip().lower()
KEY_NAME_CONTENT: str = "content".strip().lower()
KEY_NAME_API_KEY: str = "AVALAI_API_KEY".strip().upper()
# **********

# **********
ROLE_USER: str = "user".strip().lower()
ROLE_SYSTEM: str = "system".strip().lower()
ROLE_ASSISTANT: str = "assistant".strip().lower()
# **********

# **********
# MODEL_NAME: str = "gpt-4o".strip().lower()
# MODEL_NAME: str = "gpt-4o-mini".strip().lower()
MODEL_NAME: str = "gpt-3.5-turbo".strip().lower()
# MODEL_NAME: str = "gpt-3.5-turbo-instruct".strip().lower()
# **********

# **********
SYSTEM_PROMPT: str = "You are a helpful AI assistant."
SYSTEM_MESSAGE: dict = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}
# **********

if __name__ == "__main__":
    print("You must run 'chatbot.py' file!")
