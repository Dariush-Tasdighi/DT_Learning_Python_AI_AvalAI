"""
Chatbot Functions
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import chatbot_constants as constants


def get_api_key() -> str:
    """
    Get API Key Function
    """

    load_dotenv()

    api_key: str | None = os.getenv(key=constants.API_KEY_NAME)
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
        base_url=constants.BASE_URL,
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
        return ("No content received!", 0, 0)

    return (content, prompt_tokens, completion_tokens)


if __name__ == "__main__":
    print("You must run 'chatbot.py' file!")
