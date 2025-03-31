import os
import time
import pygame
from openai import OpenAI
from dotenv import load_dotenv

VOICE: str = "onyx"
MODEL_NAME: str = "gpt-4o"
AUDIO_MODEL_NAME: str = "tts-1-hd"
AUDIO_FILE_FORMAT: str = "mp3".lower()

KEY_NAME_ROLE: str = "role".lower()
KEY_NAME_USER: str = "user".lower()
KEY_NAME_SYSTEM: str = "system".lower()
KEY_NAME_CONTENT: str = "content".lower()
KEY_NAME_ASSISTANT: str = "assistant".lower()

KEY_NAME_API_KEY: str = "AVALAI_API_KEY".upper()
BASE_URL: str = "https://api.avalai.ir/v1".lower()

SYSTEM_PROMPT: str = """
تو یک روانشناس حرفه‌ای به نام علی هستی.
تو باید کاملا به زبان فارسی به مراجعه‌کننده پاسخ دهی.
تو باید کاملا دوستانه و با لحنی ملایم سعی کنی که مراجعه‌کننده را آرام کنی.
در ابتدای گفتگو، نام مراجعه‌کننده را سوال کن.
در بعضی از پاسخ‌های خودت هم، برای ایجاد یک رابطه دوستانه و صمیمی، سعی کن که نام مراجعه‌کننده را بیان کنی
"""
SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    KEY_NAME_ROLE: KEY_NAME_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def get_api_key() -> str:
    """
    Get API Key Function
    """

    load_dotenv()

    api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
    if not api_key:
        print("API Key not found!")
        exit()

    return api_key


def chat_completions(
    messages: list[dict],
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
    completion_tokens: int = response.usage.completion_tokens
    content: str | None = response.choices[0].message.content

    if not content:
        return None, 0, 0

    return content, prompt_tokens, completion_tokens


def play_audio_file(audio_file_path: str) -> None:
    """
    Play Audio File Function
    """

    pygame.mixer.init()
    pygame.mixer.music.load(filename=audio_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.unload()

    os.remove(path=audio_file_path)


def convert_text_to_speech(
    text: str,
    voice: str = "onyx",
    audio_model_name: str = "tts-1",
) -> tuple:
    """
    Convert Text to Speech Function
    """

    api_key: str = get_api_key()

    client = OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

    response = client.audio.speech.create(
        input=text,
        voice=voice,
        model=audio_model_name,
        response_format=AUDIO_FILE_FORMAT,
    )

    speech_file: str = f"temp.{AUDIO_FILE_FORMAT}"
    speech_file_path: str = f"../speech_files/{speech_file}"
    with open(file=speech_file_path, mode="wb") as file:
        for chunk in response.iter_bytes():
            file.write(chunk)

    play_audio_file(audio_file_path=speech_file_path)


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    messages: list[dict] = []
    messages.append(SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input("User: ").strip()

        if user_prompt.lower() in ["bye", "exit", "quit"]:
            break

        user_message: dict = {
            KEY_NAME_ROLE: KEY_NAME_USER,
            KEY_NAME_CONTENT: user_prompt,
        }
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = chat_completions(
            messages=messages,
            model_name=MODEL_NAME,
        )

        response_time: float = time.time() - start_time

        if not assistant_answer:
            messages.pop()
            assistant_answer = "No content received!"
        else:
            assistant_message = {
                KEY_NAME_ROLE: KEY_NAME_ASSISTANT,
                KEY_NAME_CONTENT: assistant_answer,
            }
            messages.append(assistant_message)

            convert_text_to_speech(
                text=assistant_answer,
                voice=VOICE,
                audio_model_name=AUDIO_MODEL_NAME,
            )

        print("=" * 50)
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
