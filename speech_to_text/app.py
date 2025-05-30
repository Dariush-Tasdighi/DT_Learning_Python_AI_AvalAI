import os
import app_constants as constants
import app_functions as functions


def main() -> None:
    """
    Main function.
    """

    os.system(command="cls")

    while True:
        try:
            functions.listen(
                audio_file_path=constants.TEMP_AUDIO_FILE_PATH,
            )

            text: str = functions.transcribe_speech_to_text_offline(
                audio_file_path=constants.TEMP_AUDIO_FILE_PATH,
            )

            if text.strip().lower() in ["خدا نگهدار", "خداحافظ"]:
                break

            # متن را به یک مدل دیگری می‌دهیم تا جواب ما را بدهد

            # متن پاسخ هوش مصنوعی را به مدل دیگری می‌دهیم تا آن‌را تبدیل به صدا کند

            # فایل صدا را پخش می‌کنیم

            print("=" * 50)
            print(text)
            print("=" * 50)

        except KeyboardInterrupt:
            break

        except Exception as error:
            print(f"[-] {error}")


if __name__ == "__main__":
    main()
