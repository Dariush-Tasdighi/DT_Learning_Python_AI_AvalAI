import os
import time
from openai import OpenAI
from dotenv import load_dotenv

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".lower()
STT_MODEL: str = "whisper-1".lower()
AUDIO_FILE_FORMAT: str = "mp3".lower()
KEY_NAME_API_KEY: str = "AVALAI_API_KEY".upper()
BASE_URL: str = "https://api.avalai.ir/v1".lower()


def main() -> None:
    """
    Main Function
    """

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

    audio_path_file: str = "../speech_files/sample_01.mp3"

    with open(file=audio_path_file, mode="rb") as file:
        start_time: float = time.time()

        transcription = client.audio.transcriptions.create(
            file=file,
            model=STT_MODEL,
            language=STT_LANGUAGE,
            temperature=STT_TEMPRETURE,
        )

        response_time: float = time.time() - start_time

        print("=" * 50)
        print(transcription.text)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)


if __name__ == "__main__":
    main()
