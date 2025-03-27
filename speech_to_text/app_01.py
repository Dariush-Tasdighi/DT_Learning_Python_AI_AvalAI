import os
import time
import whisper
from openai import OpenAI
from dotenv import load_dotenv

AUDIO_FILE_FORMAT: str = "mp3".lower()
KEY_NAME_API_KEY: str = "AVALAI_API_KEY".upper()
BASE_URL: str = "https://api.avalai.ir/v1".lower()

STT_MODELS: str = "whisper-1"

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

audio_file = open("../speech_files/sample_01.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
)
print(transcription)

# user_prompt: str = """
# سَلام داریوش جان، خُوبی؟ دِلَم خِیلی بَرات تَنگ شُده! خِیلی وَقتِه کِه نَدیدَمِت! کِی می‌تونَم دوباره تُو رو بِبینَم؟
# """
# user_prompt = user_prompt.strip()

# for voice in VOICES:
#     print("Voice:", voice)
#     for model in AUDIO_MODELS:
#         print("Model:", model)

#         response = client.audio.speech.create(
#             model=model,
#             voice=voice,
#             input=user_prompt,
#             response_format=AUDIO_FILE_FORMAT,
#         )

#         speech_file: str = f"{FILE_PREFIX}_{voice}_{model}.{AUDIO_FILE_FORMAT}"
#         speech_file_path: str = f"../speech_files/{speech_file}"
#         with open(file=speech_file_path, mode="wb") as file:
#             for chunk in response.iter_bytes():
#                 file.write(chunk)

#         print(f"\nFile: {speech_file} created.")
#         print("-" * 50)
#         print(f"Waiting {WAITING_IN_SECONDS} seconds...")
#         time.sleep(WAITING_IN_SECONDS)
#         print("-" * 50)
