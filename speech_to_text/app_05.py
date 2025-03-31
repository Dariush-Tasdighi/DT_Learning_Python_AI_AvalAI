import os
import torch
import whisper
import speech_recognition as sr

DURATION: float = 2
LANGUAGE: str = "fa".lower()
STT_MODEL: str = "turbo".lower()
TEMP_AUDIO_FILE: str = "../speech_files/temp.wav"


def listen(audio_file: str) -> str:
    """
    Listen Function
    """

    print("Listening...")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(
            source=source,
            duration=DURATION,
        )

        audio = recognizer.listen(source=source)

        with open(file=audio_file, mode="wb") as file:
            data = audio.get_wav_data()
            file.write(data)


def convert_speech_to_text(audio_file: str) -> str:
    """
    Convert Speech to Text Function
    """

    print("Converting Speech to Text...")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    # print("Device:", device)

    model = whisper.load_model(
        device=device,
        name=STT_MODEL,
    )

    result = model.transcribe(
        temperature=0.0,
        audio=audio_file,
        language=LANGUAGE,
    )

    return result["text"]


def main() -> None:
    os.system(command="cls")

    while True:
        try:
            listen(audio_file=TEMP_AUDIO_FILE)
            text: str = convert_speech_to_text(audio_file=TEMP_AUDIO_FILE)

            if text.strip().lower() in ["خدا نگهدار"]:
                break

            print("=" * 50)
            print(text)
            print("=" * 50)

        except Exception as ex:
            print(f"#ERR: {ex}")


if __name__ == "__main__":
    main()
