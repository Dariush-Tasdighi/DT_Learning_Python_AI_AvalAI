import os
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

TEMP_AUDIO_FILE_PATH: str = "../speech_files/LiveRecording.mp3"


def listen(audio_file_path: str) -> None:
    """
    Listen to Microphone and Save Audio to File.
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

    while True:
        try:
            listen(audio_file_path=TEMP_AUDIO_FILE_PATH)
            text: str = transcribe_speech_to_text_offline(
                audio_file_path=TEMP_AUDIO_FILE_PATH
            )

            if text.strip().lower() in ["خدا نگهدار"]:
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
