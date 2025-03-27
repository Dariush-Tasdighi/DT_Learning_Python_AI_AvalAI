# https://www.openai.fm/

import os
import time
import base64
from openai import OpenAI
from dotenv import load_dotenv

KEY_NAME_ROLE: str = "role".lower()
KEY_NAME_USER: str = "user".lower()
KEY_NAME_SYSTEM: str = "system".lower()
KEY_NAME_CONTENT: str = "content".lower()
KEY_NAME_API_KEY: str = "AVALAI_API_KEY".upper()

FILE_PREFIX: str = "08"
TEMPERATURE: float = 0.0
WAITING_IN_SECONDS: float = 60
AUDIO_FILE_FORMAT: str = "wav".lower()
BASE_URL: str = "https://api.avalai.ir/v1".lower()

VOICES: list[str] = [
    # "ash",  # OK - Male
    # "echo",  # OK - Male
    # "onyx",  # OK - Male
    # "ballad",  # OK - Male
    # "verse",  # OK - Male
    "sage",  # OK - Female
    # "nova",  # OK - Female - OK
    # "fable",  # OK Female
    # "alloy",  # OK - Female
    # "coral",  # OK - Female - OK
    # "shimmer",  # OK - Female
]

AUDIO_MODELS: list[str] = [
    # "gpt-4o-audio-preview",
    # "gpt-4o-audio-preview-2024-10-01",
    "gpt-4o-audio-preview-2024-12-17",
    # "gpt-4o-mini-audio-preview",
    # "gpt-4o-mini-audio-preview-2024-12-17",
]

os.system(command="cls")

load_dotenv()

api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
if not api_key:
    print("API Key not found!")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

SYSTEM_PROMPT: str = """
تو صرفا یک گوینده متن هستی و فقط باید متنی که کاربر بهت می‌دهد را به زبان فارسی و با لهجه کشور ایران بخوانی.

باید متن را به طور کامل بخوانی.

اصلا نباید کلمه اضافه‌تری جز متن کاربر بگویی.

Voice Affect: Low, hushed, and suspenseful; convey tension and intrigue.

Tone: Deeply serious and mysterious, maintaining an undercurrent of unease throughout.

Pacing: Slow, deliberate, pausing slightly after suspenseful moments to heighten drama.

Emotion: Restrained yet intense—voice should subtly tremble or tighten at key suspenseful points.

Emphasis: Highlight sensory descriptions ("footsteps echoed," "heart hammering," "shadows melting into darkness") to amplify atmosphere.

Pronunciation: Slightly elongated vowels and softened consonants for an eerie, haunting effect.

Pauses: Insert meaningful pauses after phrases like "only shadows melting into darkness," and especially before the final line, to enhance suspense dramatically.
"""
SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    KEY_NAME_ROLE: KEY_NAME_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

user_prompt: str = """
سلام داریوش جان، خوبی؟ دلم خیلی براتْ تنگ شده! خیلی وقته که ندیدمت! کِی می‌تونم دوباره تو رو ببینم؟
"""
user_prompt = user_prompt.strip()
user_message = {
    KEY_NAME_ROLE: KEY_NAME_USER,
    KEY_NAME_CONTENT: user_prompt,
}

messages: list[dict] = []
messages.append(SYSTEM_MESSAGE)
messages.append(user_message)

for voice in VOICES:
    print("Voice:", voice)
    for model in AUDIO_MODELS:
        print("Model:", model)
        chat_completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=TEMPERATURE,
            modalities=["text", "audio"],
            audio={"voice": voice, "format": AUDIO_FILE_FORMAT},
        )

        speech_file: str = (
            f"{FILE_PREFIX}_{str(TEMPERATURE)}_{voice}_{model}.{AUDIO_FILE_FORMAT}"
        )
        speech_file_path: str = f"../speech_files/{speech_file}"
        with open(file=speech_file_path, mode="wb") as file:
            data: str = chat_completion.choices[0].message.audio.data
            audio: bytes = base64.b64decode(s=data)
            file.write(audio)

        print(f"\nFile: {speech_file} created.")
        print("-" * 50)
        print(f"Waiting {WAITING_IN_SECONDS} seconds...")
        time.sleep(WAITING_IN_SECONDS)
        print("-" * 50)
