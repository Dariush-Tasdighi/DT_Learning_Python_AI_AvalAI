# **************************************************
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".strip().lower()
STT_MODEL: str = "whisper-1".strip().lower()
AUDIO_FILE_FORMAT: str = "mp3".strip().lower()
BASE_URL: str = "https://api.avalai.ir/v1".strip().lower()
KEY_NAME_AVALAI_API_KEY: str = "AVALAI_API_KEY".strip().upper()

os.system(command="cls")

load_dotenv(override=True)

api_key: str | None = os.getenv(
    key=KEY_NAME_AVALAI_API_KEY,
)

if not api_key:
    print("[-] API Key not found!")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

audio_file_path: str = "../speech_files/Recording.mp3"
# audio_path_file: str = "../speech_files/Recording.mp3"  # Bad Practice Naming

if not os.path.exists(path=audio_file_path):
    print(f"[-] Audio file not found: {audio_file_path}")
    exit()

with open(file=audio_file_path, mode="rb") as file:
    start_time: float = time.time()

    result = client.audio.transcriptions.create(
        file=file,
        model=STT_MODEL,
        language=STT_LANGUAGE,
        temperature=STT_TEMPRETURE,
    )

    response_time: float = time.time() - start_time

    print("=" * 50)
    print(result.text)
    print("-" * 50)
    print(f"Full response received {response_time:.2f} seconds after request.")
    print("=" * 50)
# **************************************************


# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv

# STT_TEMPRETURE: float = 0.0
# STT_LANGUAGE: str = "fa".strip().lower()
# STT_MODEL: str = "whisper-1".strip().lower()
# AUDIO_FILE_FORMAT: str = "mp3".strip().lower()
# BASE_URL: str = "https://api.avalai.ir/v1".strip().lower()
# KEY_NAME_AVALAI_API_KEY: str = "AVALAI_API_KEY".strip().upper()


# def get_api_key(key_name: str) -> str:
#     """
#     Get API key from environment variables.
#     """

#     load_dotenv(override=True)

#     api_key: str | None = os.getenv(key=key_name)

#     if not api_key:
#         print("[-] API Key not found!")
#         exit()

#     return api_key


# def transcribe_speech_to_text_online(
#     key_name: str,
#     audio_file_path: str,
# ) -> str:
#     """
#     Trasncribe speech to text using OpenAI API.
#     """

#     print("Trasncribing speech to text using OpenAI API...")

#     if not os.path.exists(path=audio_file_path):
#         print(f"[-] Audio file not found: {audio_file_path}")
#         exit()

#     api_key: str = get_api_key(
#         key_name=key_name,
#     )

#     client = OpenAI(
#         api_key=api_key,
#         base_url=BASE_URL,
#     )

#     with open(file=audio_file_path, mode="rb") as file:
#         transcription = client.audio.transcriptions.create(
#             file=file,
#             model=STT_MODEL,
#             language=STT_LANGUAGE,
#             temperature=STT_TEMPRETURE,
#         )

#     return transcription.text


# def main() -> None:
#     """
#     Main function.
#     """

#     os.system(command="cls")

#     audio_file_path: str = "../speech_files/Recording.mp3"

#     start_time: float = time.time()

#     text: str = transcribe_speech_to_text_online(
#         audio_file_path=audio_file_path,
#         key_name=KEY_NAME_AVALAI_API_KEY,
#     )

#     response_time: float = time.time() - start_time

#     print("=" * 50)
#     print(text)
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("=" * 50)


# if __name__ == "__main__":
#     main()
# **************************************************
