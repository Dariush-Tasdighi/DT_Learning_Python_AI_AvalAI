# **************************************************
# نکته بسیار مهم:
# برای استفاده از کتابخانه
# whisper
# باید کتابخانه
# torch
# را نصب کنید:
#
# علاوه بر این، و در عین ناباوری، باید حتما برنامه
# ffmpeg
# نیز بر روی سیستم نصب شده باشد و مسیر
# Path
# نیز در
# System Environment Variables
# اضافه شده باشد.
# **************************************************


# **************************************************
# 1. https://vrgl.ir/T3JLR
#
# 2. FFmpeg:
# https://ffmpeg.org/download.html
#
# 3. Install Local Whisper Model:
# https://github.com/openai/whisper
# https://pypi.org/project/whisper
# python -m pip install -U openai-whisper
#
# 4. For Activation GPU:
#
# 5.1. CUDA:
# https://developer.nvidia.com/cuda-toolkit
#
# 5.2. Download and Install PyTorch:
# https://pytorch.org
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
# **************************************************
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


# os.system(command="cls")

# device = "cuda" if torch.cuda.is_available() else "cpu"
# print("Device:", device)
# # exit()

# audio_file_path: str = "../speech_files/sample_01.mp3"
# # audio_file_path: str = "../speech_files/Ali-Akbar-Raefipour-03.mp3"

# # Solution (1) - with 'turbo' model - mp3 is 51 seconds: 31.72 seconds
# # model = whisper.load_model(name=STT_MODEL, device="cpu")

# # Solution (2) - with 'turbo' model - mp3 is 51 seconds: 47.70 seconds
# model = whisper.load_model(name=STT_MODEL, device=device)

# # Solution (3) - with 'turbo' model - mp3 is 51 seconds: 40.23 seconds
# # model = whisper.load_model(name=STT_MODEL).to(device=device)

# if not os.path.exists(path=audio_file_path):
#     print(f"[-] Audio file not found: {audio_file_path}")
#     exit()

# start_time: float = time.time()
# result = model.transcribe(
#     language=STT_LANGUAGE,
#     audio=audio_file_path,
#     temperature=STT_TEMPRETURE,
# )
# response_time: float = time.time() - start_time

# print("=" * 50)
# print(result)
# print("-" * 50)
# print(result["text"])
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
import os
import time
import torch
import whisper

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".lower()
STT_MODEL: str = "turbo".lower()

TEMP_AUDIO_FILE_PATH: str = "../speech_files/Recording.mp3"


def transcribe_speech_to_text_offline(audio_file_path: str) -> str:
    """
    Trasncribe Speech to Text using Local / Offline LLM Model.
    """

    print("Trasncribing Speech to Text using Local / Offline LLM Model...")

    if not os.path.exists(path=audio_file_path):
        print(f"[-] Audio file not found: {audio_file_path}")
        exit()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = whisper.load_model(
        device=device,
        name=STT_MODEL,
    )

    result = model.transcribe(
        language=STT_LANGUAGE,
        audio=audio_file_path,
        temperature=STT_TEMPRETURE,
    )

    return result["text"]


def main() -> None:
    """
    Main Function.
    """

    os.system(command="cls")

    start_time: float = time.time()
    text: str = transcribe_speech_to_text_offline(audio_file_path=TEMP_AUDIO_FILE_PATH)
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
