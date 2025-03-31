# **************************************************
# # https://github.com/openai/whisper
# #
# # For Activation GPU:
# # pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# import os
# import time
# import torch
# import whisper

# STT_TEMPRETURE: float = 0.0
# STT_LANGUAGE: str = "fa".lower()

# # STT_MODEL: str = "tiny".lower()
# # STT_MODEL: str = "base".lower()
# # STT_MODEL: str = "small".lower()
# # STT_MODEL: str = "medium".lower()
# # STT_MODEL: str = "large".lower()
# STT_MODEL: str = "turbo".lower()

# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     device = "cuda" if torch.cuda.is_available() else "cpu"
#     print("Device:", device)
#     # exit()

#     audio_path_file: str = "../speech_files/sample_01.mp3"
#     # audio_path_file: str = "../speech_files/Ali-Akbar-Raefipour-03.mp3"

#     # Solution (1) - with 'turbo' model - mp3 is 51 seconds: 31.72 seconds
#     # model = whisper.load_model(name=STT_MODEL, device="cpu")

#     # Solution (2) - with 'turbo' model - mp3 is 51 seconds: 47.70 seconds
#     model = whisper.load_model(name=STT_MODEL, device=device)

#     # Solution (3) - with 'turbo' model - mp3 is 51 seconds: 40.23 seconds
#     # model = whisper.load_model(name=STT_MODEL).to(device=device)

#     if not os.path.exists(path=audio_path_file):
#         print("#ERR: Audio file does not exist!")
#         exit()

#     start_time: float = time.time()

#     result = model.transcribe(
#         language=STT_LANGUAGE,
#         audio=audio_path_file,
#         temperature=STT_TEMPRETURE,
#     )

#     response_time: float = time.time() - start_time

#     print("=" * 50)
#     print(result)
#     print("-" * 50)
#     print(result["text"])
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("=" * 50)
#     print()


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
import os
import time
import torch
import whisper

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".lower()
STT_MODEL: str = "turbo".lower()

TEMP_AUDIO_FILE_PATH: str = "../speech_files/temp.wav"


def convert_speech_to_text(audio_file_path: str) -> str:
    """
    Convert Speech to Text
    """

    print("Converting Speech to Text...")

    if not os.path.exists(path=audio_file_path):
        print("[-] Audio file does not exist!")
        exit()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = whisper.load_model(
        device=device,
        name=STT_MODEL,
    )

    result = model.transcribe(
        temperature=0.0,
        language=STT_LANGUAGE,
        audio=audio_file_path,
    )

    return result["text"]


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    start_time: float = time.time()
    text: str = convert_speech_to_text(audio_file_path=TEMP_AUDIO_FILE_PATH)
    response_time: float = time.time() - start_time

    print("=" * 50)
    print(text)
    print("-" * 50)
    print(f"Full response received {response_time:.2f} seconds after request.")
    print("=" * 50)
    print()


if __name__ == "__main__":
    main()
# **************************************************
