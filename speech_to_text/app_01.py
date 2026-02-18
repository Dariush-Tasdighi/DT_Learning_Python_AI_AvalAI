# **************************************************
# import os
# import time
# from rich import print
# from openai import OpenAI
# from dotenv import load_dotenv

# from typing import (
#     Final,
#     Optional,
# )

# STT_MODEL_NAME: Final[str] = "whisper-1".replace(" ", "").lower()
# # STT_MODEL_NAME: Final[str] = "groq.whisper-large-v3".replace(" ", "").lower()
# # STT_MODEL_NAME: Final[str] = "groq.whisper-large-v3-turbo".replace(" ", "").lower()

# STT_TEMPRETURE: Final[float] = 0.0
# STT_LANGUAGE: Final[str] = "fa".replace(" ", "").lower()
# STT_AUDIO_FILE_EXTENSION: Final[str] = "mp3".replace(" ", "").lower()

# BASE_URL: Final[str] = "https://api.avalai.ir/v1".replace(" ", "").lower()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "AVALAI_API_KEY".replace(" ", "").upper()


# def main() -> None:
#     """
#     The main of program
#     """

#     os.system(command="cls" if os.name == "nt" else "clear")

#     load_dotenv(override=True)
#     api_key: Optional[str] = os.getenv(key=KEY_NAME_OPENAI_API_KEY)
#     if not api_key:
#         error_message: str = (
#             f"The '{KEY_NAME_OPENAI_API_KEY}' key not found or is empty"
#         )
#         raise Exception(error_message)

#     # audio_file_path: str = "./alaki.mp3"
#     # audio_file_path: str = "../speech_to_text"
#     # audio_file_path: str = "../speech_to_text/app_01.py"
#     audio_file_path: str = "../speech_files/Recording.mp3"

#     if not os.path.exists(path=audio_file_path):
#         error_message: str = f"File not found: '{audio_file_path}'"
#         raise Exception(error_message)

#     if not os.path.isfile(path=audio_file_path):
#         error_message: str = f"File not found: '{audio_file_path}'"
#         raise Exception(error_message)

#     file_extension: str = audio_file_path.split(sep=".")[-1].lower()
#     if file_extension != STT_AUDIO_FILE_EXTENSION:
#         error_message: str = (
#             f"The '{audio_file_path}' file must have '{STT_AUDIO_FILE_EXTENSION}' extension"
#         )
#         raise Exception(error_message)

#     with open(file=audio_file_path, mode="rb") as file:
#         start_time: float = time.perf_counter()

#         client = OpenAI(
#             api_key=api_key,
#             base_url=BASE_URL,
#         )

#         response = client.audio.transcriptions.create(
#             file=file,
#             model=STT_MODEL_NAME,
#             language=STT_LANGUAGE,
#             temperature=STT_TEMPRETURE,
#         )

#         end_time: float = time.perf_counter()
#         elapsed_time: float = end_time - start_time

#         print("=" * 50)
#         print(response.text)
#         print("-" * 50)
#         print(f"Elapsed time: {elapsed_time:.2f} seconds")
#         print("=" * 50)


# if __name__ == "__main__":
#     try:
#         main()

#     except Exception as exception:
#         print(f"[red][-] {exception}!")

#     finally:
#         print()
# **************************************************


# **************************************************
# import os
# import time
# from rich import print
# from typing import Final
# from openai import OpenAI
# from dotenv import load_dotenv

# from typing import (
#     Final,
#     Optional,
# )

# BASE_URL: Final[str] = "https://api.avalai.ir/v1".replace(" ", "").lower()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "AVALAI_API_KEY".replace(" ", "").upper()

# STT_TEMPRETURE: Final[float] = 0.0
# STT_LANGUAGE: Final[str] = "fa".replace(" ", "").lower()
# STT_AUDIO_FILE_EXTENSION: Final[str] = "mp3".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "groq.whisper-large-v3-turbo".replace(" ", "").lower()


# def transcribe_speech_to_text_online(
#     audio_file_path: str,
#     base_url: str = BASE_URL,
#     language: str = STT_LANGUAGE,
#     model_name: str = STT_MODEL_NAME,
#     api_key: Optional[str] = None,
#     tempreture: float = STT_TEMPRETURE,
# ) -> str:
#     """
#     Transcribe speech to text online
#     """

#     if not api_key:
#         load_dotenv(override=True)
#         api_key = os.getenv(key=KEY_NAME_OPENAI_API_KEY)
#         if not api_key:
#             error_message: str = (
#                 f"The '{KEY_NAME_OPENAI_API_KEY}' key not found or is empty"
#             )
#             raise Exception(error_message)

#     if not os.path.exists(path=audio_file_path):
#         error_message: str = f"File not found: '{audio_file_path}'"
#         raise Exception(error_message)

#     if not os.path.isfile(path=audio_file_path):
#         error_message: str = f"File not found: '{audio_file_path}'"
#         raise Exception(error_message)

#     file_extension: str = audio_file_path.split(sep=".")[-1].lower()
#     if file_extension != STT_AUDIO_FILE_EXTENSION:
#         error_message: str = (
#             f"The '{audio_file_path}' file must have '{STT_AUDIO_FILE_EXTENSION}' extension"
#         )
#         raise Exception(error_message)

#     with open(file=audio_file_path, mode="rb") as file:
#         start_time: float = time.perf_counter()

#         client = OpenAI(
#             api_key=api_key,
#             base_url=base_url,
#         )

#         response = client.audio.transcriptions.create(
#             file=file,
#             model=model_name,
#             language=language,
#             temperature=tempreture,
#         )

#         result: str = response.text
#         return result


# def main() -> None:
#     """
#     The main of program
#     """

#     os.system(command="cls" if os.name == "nt" else "clear")

#     audio_file_path: str = "../speech_files/Recording.mp3"

#     start_time: float = time.perf_counter()

#     text: str = transcribe_speech_to_text_online(
#         audio_file_path=audio_file_path,
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time

#     print("=" * 50)
#     print(text)
#     print("-" * 50)
#     print(f"Elapsed time: {elapsed_time:.2f} seconds")
#     print("=" * 50)


# if __name__ == "__main__":
#     try:
#         main()

#     except Exception as exception:
#         print(f"[red][-] {exception}!")

#     finally:
#         print()
# **************************************************
