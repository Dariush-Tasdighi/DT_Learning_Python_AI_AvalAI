"""
This module contains constants used in the speech-to-text application.
"""

STT_TEMPRETURE: float = 0.0
STT_LANGUAGE: str = "fa".lower()
STT_MODEL: str = "turbo".lower()

MICROPHONE_DURATION: int = 1
MICROPHONE_DEVICE_INDEX: int = 1
MICROPHONE_CHUNK_SIZE: int = 1024
MICROPHONE_FRAME_RATE: int = 48_000

TEMP_AUDIO_FILE_PATH: str = "../speech_files/LiveRecording.mp3"

if __name__ == "__main__":
    print(
        "[-] This module is not meant to be run directly. Please use the 'app.py' script instead."
    )
