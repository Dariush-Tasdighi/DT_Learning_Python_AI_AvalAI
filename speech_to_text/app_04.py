import os
import time
import torch
import whisper
import speech_recognition as sr

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".lower()
STT_MODEL: str = "turbo".lower()

MICROPHONE_DURATION: int = 1
MICROPHONE_DEVICE_INDEX: int = 1
MICROPHONE_CHUNK_SIZE: int = 1024
MICROPHONE_FRAME_RATE: int = 48_000

TEMP_AUDIO_FILE_PATH: str = "../speech_files/temp.wav"


def listen(audio_file_path: str) -> None:
    """
    Listen Function
    """

    print("Listening...")

    with sr.Microphone(
        chunk_size=MICROPHONE_CHUNK_SIZE,
        sample_rate=MICROPHONE_FRAME_RATE,
        device_index=MICROPHONE_DEVICE_INDEX,
    ) as microphone:
        recognizer = sr.Recognizer()

        recognizer.adjust_for_ambient_noise(
            source=microphone,
            duration=MICROPHONE_DURATION,
        )

        audio = recognizer.listen(source=microphone)

        with open(file=audio_file_path, mode="wb") as file:
            data = audio.get_wav_data()
            file.write(data)


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

    listen(audio_file_path=TEMP_AUDIO_FILE_PATH)

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
