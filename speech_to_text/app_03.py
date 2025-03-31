# **************************************************
# https://realpython.com/python-speech-recognition/
# https://dev.to/abhinowww/how-to-record-audio-in-python-automatically-detect-speech-and-silence-4951
# **************************************************


# **************************************************
# import os
# import speech_recognition

# os.system(command="cls")

# print("Version of 'speech_recognition' package:", speech_recognition.__version__)
# **************************************************


# **************************************************
# import os
# import speech_recognition as sr

# os.system(command="cls")

# print("=" * 50)

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     new_name = str(name).replace("\r", "").replace("\n", "").ljust(80, " ")
#     message = f"Name: {new_name} - Index: {index}"
#     print(message)

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# import os
# import speech_recognition as sr

# MICROPHONE_DURATION: int = 1
# MICROPHONE_DEVICE_INDEX: int = 1
# MICROPHONE_CHUNK_SIZE: int = 1024
# MICROPHONE_FRAME_RATE: int = 48_000

# os.system(command="cls")

# with sr.Microphone(
#     chunk_size=MICROPHONE_CHUNK_SIZE,
#     sample_rate=MICROPHONE_FRAME_RATE,
#     device_index=MICROPHONE_DEVICE_INDEX,
# ) as microphone:
#     recognizer = sr.Recognizer()

#     recognizer.adjust_for_ambient_noise(
#         source=microphone,
#         duration=MICROPHONE_DURATION,
#     )

#     print("Listening...")

#     audio = recognizer.listen(source=microphone)

#     audio_path_file: str = "../speech_files/temp.wav"

#     with open(file=audio_path_file, mode="wb") as file:
#         data = audio.get_wav_data()
#         file.write(data)

#     print("Finished")
# **************************************************


# **************************************************
# import os
# import speech_recognition as sr

# MICROPHONE_DURATION: int = 1
# MICROPHONE_DEVICE_INDEX: int = 1
# MICROPHONE_CHUNK_SIZE: int = 1024
# MICROPHONE_FRAME_RATE: int = 48_000


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     with sr.Microphone(
#         chunk_size=MICROPHONE_CHUNK_SIZE,
#         sample_rate=MICROPHONE_FRAME_RATE,
#         device_index=MICROPHONE_DEVICE_INDEX,
#     ) as microphone:
#         recognizer = sr.Recognizer()

#         recognizer.adjust_for_ambient_noise(
#             source=microphone,
#             duration=MICROPHONE_DURATION,
#         )

#         print("Listening...")

#         audio = recognizer.listen(source=microphone)

#         audio_path_file: str = "../speech_files/temp.wav"

#         with open(file=audio_path_file, mode="wb") as file:
#             data = audio.get_wav_data()
#             file.write(data)

#         print("Finished")


# if __name__ == "__main__":
#     main()
# **************************************************

# **************************************************
import os
import speech_recognition as sr

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


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    listen(audio_file_path=TEMP_AUDIO_FILE_PATH)

    print("Finished")


if __name__ == "__main__":
    main()
# **************************************************
