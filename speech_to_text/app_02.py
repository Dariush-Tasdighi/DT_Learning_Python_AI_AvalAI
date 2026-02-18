# **************************************************
# نکته بسیار مهم:
# در زمان نصب کتابخانه
# whisper
# کتابخانه
# torch
# نیز نصب می‌شود:
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
# 1. Check your GPU
# 	- NVIDIA
# 2. Is your NVIDIA compatible with AI
# 	- 10x
# 	- 20x
# 	- ...
# 	- 50x
# 3. Update NVIDIA Driver
# 4. Download / Update CUDA Driver (2.5GB)
# 	- Check Your NVIDIA GPU with CUDA Version
# 5. Download PyTorch for GPU (3GB)
# 6. Check GPU (CUDA) with Python
# **************************************************


# **************************************************
# 1. https://vrgl.ir/T3JLR
#
# 2. FFmpeg:
# https://ffmpeg.org/download.html
#
# 3. Install Local Whisper Model:
# https://github.com/openai/whisper
# https://pypi.org/project/openai-whisper
# python -m pip install -U openai-whisper
#
# 4. For Activation GPU:
#
# 5.1. CUDA:
# https://developer.nvidia.com/cuda-toolkit
#
# 5.2. Download and Install PyTorch:
# https://pytorch.org
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 -U
# python -m pip install --trusted-host mirror-pypi.runflare.com -i https://mirror-pypi.runflare.com/simple -U
# **************************************************


# **************************************************
import os
import time
from rich import print
from typing import Final

# NEW
import torch
import whisper

# STT_MODEL_NAME: Final[str] = "tiny".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "base".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "small".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "medium".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "large".replace(" ", "").lower()
STT_MODEL_NAME: Final[str] = "turbo".replace(" ", "").lower()

STT_TEMPRETURE: Final[float] = 0.0
STT_LANGUAGE: Final[str] = "fa".replace(" ", "").lower()
STT_AUDIO_FILE_EXTENSION: Final[str] = "mp3".replace(" ", "").lower()


def main() -> None:
    """
    The main of program
    """

    os.system(command="cls" if os.name == "nt" else "clear")

    audio_file_path: str = "../speech_files/Recording.mp3"
    # audio_file_path: str = "../speech_files/Ali-Akbar-Raefipour-03.mp3"

    if not os.path.exists(path=audio_file_path):
        error_message: str = f"File not found: '{audio_file_path}'"
        raise Exception(error_message)

    if not os.path.isfile(path=audio_file_path):
        error_message: str = f"File not found: '{audio_file_path}'"
        raise Exception(error_message)

    file_extension: str = audio_file_path.split(sep=".")[-1].lower()
    if file_extension != STT_AUDIO_FILE_EXTENSION:
        error_message: str = (
            f"The '{audio_file_path}' file must have '{STT_AUDIO_FILE_EXTENSION}' extension"
        )
        raise Exception(error_message)

    # NEW
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    # print(f"Device: {device}")
    # exit()  # Test

    # **********
    # NEW
    # Warning: FP16 is not supported on CPU; using FP32 instead
    # **********
    # fp16: bool = False
    # if device == "cuda":
    #     fp16 = True
    # **********
    fp16: bool = False if device == "cuda" else True

    # NEW
    # model = whisper.load_model(
    #     device="cpu",
    #     name=STT_MODEL_NAME,
    # )

    # NEW
    # model = whisper.load_model(name=STT_MODEL_NAME).to(device="cpu")

    # NEW
    model = whisper.load_model(
        device=device,
        name=STT_MODEL_NAME,
    )

    # NEW
    # model = whisper.load_model(name=STT_MODEL_NAME).to(device=device)

    start_time: float = time.perf_counter()

    response = model.transcribe(
        fp16=fp16,
        language=STT_LANGUAGE,
        audio=audio_file_path,
        temperature=STT_TEMPRETURE,
    )

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time

    print("=" * 50)
    print(response)
    print("-" * 50)
    print(response["text"])
    print("-" * 50)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()

    except Exception as exception:
        print(f"[red][-] {exception}!")

    finally:
        print()
# **************************************************


# **************************************************
# import os
# import time
# import torch
# import whisper
# from rich import print
# from typing import Final

# STT_TEMPRETURE: Final[float] = 0.0
# STT_LANGUAGE: Final[str] = "fa".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "turbo".replace(" ", "").lower()
# STT_AUDIO_FILE_EXTENSION: Final[str] = "mp3".replace(" ", "").lower()


# def transcribe_speech_to_text_offline(
#     audio_file_path: str,
#     language: str = STT_LANGUAGE,
#     model_name: str = STT_MODEL_NAME,
#     tempreture: float = STT_TEMPRETURE,
# ) -> str:
#     """
#     Transcribe speech to text offline
#     """

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

#     device: str = "cuda" if torch.cuda.is_available() else "cpu"
#     fp16: bool = False if device == "cuda" else True

#     model = whisper.load_model(
#         device=device,
#         name=model_name,
#     )

#     response: dict = model.transcribe(
#         fp16=fp16,
#         language=language,
#         audio=audio_file_path,
#         temperature=tempreture,
#     )

#     # text: str = str(response["text"])
#     text: str = str(response.get("text", ""))
#     return text


# def main() -> None:
#     """
#     The main of program
#     """

#     os.system(command="cls" if os.name == "nt" else "clear")

#     audio_file_path: str = "../speech_files/Recording.mp3"

#     start_time: float = time.perf_counter()

#     text: str = transcribe_speech_to_text_offline(
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
