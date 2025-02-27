"""
Simple Chatbot - With History
"""

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# **********
API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# **********

# **********
ROLE_KEY_NAME: str = "role".strip().lower()
CONTENT_KEY_NAME: str = "content".strip().lower()

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


def get_api_key() -> str:
    """
    Get API Key Function
    """

    load_dotenv()

    api_key: str | None = os.getenv(key=API_KEY_NAME)
    if not api_key:
        print("API Key not found!")
        exit()

    return api_key


def chat_completions(
    messages: list,
    temperature: float = 0.7,
    model_name: str = "gpt-3.5-turbo",
) -> tuple:
    """
    Chat Completions Function
    """

    api_key: str = get_api_key()

    client = OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

    response = client.chat.completions.create(
        stream=False,
        model=model_name,
        messages=messages,
        temperature=temperature,
    )

    prompt_tokens: int = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    content: str | None = response.choices[0].message.content

    if not content:
        return (None, 0, 0)

    return (content, prompt_tokens, completion_tokens)


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    SYSTEM_PROMPT: str = "You are a helpful AI assistant."
    SYSTEM_MESSAGE: dict = {
        ROLE_KEY_NAME: ROLE_SYSTEM,
        CONTENT_KEY_NAME: SYSTEM_PROMPT,
    }

    messages: list = []
    messages.append(SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input("User: ")

        if user_prompt.lower() in ["exit", "quit", "bye"]:
            break

        user_message = {
            ROLE_KEY_NAME: ROLE_USER,
            CONTENT_KEY_NAME: user_prompt,
        }

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = chat_completions(
            messages=messages,
            model_name=MODEL_NAME,
        )

        response_time: float = time.time() - start_time

        if assistant_answer:
            messages.append(user_message)

            assistant_message = {
                ROLE_KEY_NAME: ROLE_ASSISTANT,
                CONTENT_KEY_NAME: assistant_answer,
            }

            messages.append(assistant_message)

        print("-" * 50)
        print(assistant_answer)
        print("-" * 50)
        print("Prompt Tokens:", prompt_tokens)
        print("-" * 50)
        print("Completion Tokens:", completion_tokens)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)
        print()


if __name__ == "__main__":
    main()
