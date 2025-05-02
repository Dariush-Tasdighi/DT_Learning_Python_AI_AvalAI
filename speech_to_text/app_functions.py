"""
Speech to Text Application Functions.
"""

import os
import torch
import whisper
import speech_recognition as sr
import app_constants as constants


def listen(audio_file_path: str) -> None:
    """
    Listen to Microphone and Save Audio to File.
    """

    print("Listening...")

    with sr.Microphone(
        chunk_size=constants.MICROPHONE_CHUNK_SIZE,
        sample_rate=constants.MICROPHONE_FRAME_RATE,
        device_index=constants.MICROPHONE_DEVICE_INDEX,
    ) as microphone:
        recognizer = sr.Recognizer()

        recognizer.adjust_for_ambient_noise(
            source=microphone,
            duration=constants.MICROPHONE_DURATION,
        )

        audio = recognizer.listen(source=microphone)

        with open(file=audio_file_path, mode="wb") as file:
            data = audio.get_wav_data()
            file.write(data)


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
        name=constants.STT_MODEL,
    )

    result = model.transcribe(
        audio=audio_file_path,
        language=constants.STT_LANGUAGE,
        temperature=constants.STT_TEMPRETURE,
    )

    return result["text"]


if __name__ == "__main__":
    print(
        "[-] This module is not meant to be run directly. Please use the 'app.py' script instead."
    )
