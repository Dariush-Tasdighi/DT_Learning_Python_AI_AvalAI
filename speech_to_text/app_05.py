import os
import torch
import whisper
from rich import print
import speech_recognition as sr

TEMPRETURE: float = 0.0
LANGUAGE: str = "fa".strip().lower()
MODEL: str = "turbo".strip().lower()

MICROPHONE_DURATION: int = 1
MICROPHONE_DEVICE_INDEX: int = 1
MICROPHONE_CHUNK_SIZE: int = 1024
MICROPHONE_FRAME_RATE: int = 48_000

TEMP_AUDIO_FILE_PATH: str = "../speech_files/LiveRecording.mp3"


def listen(
    audio_file_path: str,
    notify: bool = False,
) -> None:
    """Listen to microphone and save audio to file function."""

    if notify:
        print("Start Listening...")

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

        if notify:
            print("Finished Listening.")

        data = audio.get_wav_data()  # type: ignore

        with open(file=audio_file_path, mode="wb") as file:
            file.write(data)


def transcribe_speech_to_text_offline(
    audio_file_path: str,
    notify: bool = False,
) -> str:
    """Trasncribe speech to text using local / offline LLM model."""

    if not os.path.exists(path=audio_file_path):
        print(f"[-] Audio file not found: {audio_file_path}")
        exit()

    if not os.path.isfile(path=audio_file_path):
        print(f"[-] Audio file not found: {audio_file_path}")
        exit()

    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    if notify:
        print("Trasncribing speech to text Starting...")

    model = whisper.load_model(
        name=MODEL,
        device=device,
    )

    result = model.transcribe(
        language=LANGUAGE,
        audio=audio_file_path,
        temperature=TEMPRETURE,
    )

    if notify:
        print("Trasncribing speech to text Finished.")

    return str(result["text"])


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    while True:
        try:
            listen(
                notify=True,
                audio_file_path=TEMP_AUDIO_FILE_PATH,
            )

            text: str = transcribe_speech_to_text_offline(
                notify=True,
                audio_file_path=TEMP_AUDIO_FILE_PATH,
            )

            if text.strip().lower() in ["خدا نگهدار", "خداحافظ", "خدا حافظ"]:
                break

            print("=" * 50)
            print(text)
            print("=" * 50)

        except KeyboardInterrupt:
            break

        except Exception as error:
            print(f"[-] {error}")


if __name__ == "__main__":
    main()
