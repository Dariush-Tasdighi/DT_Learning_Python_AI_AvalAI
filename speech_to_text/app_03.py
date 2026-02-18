# **************************************************
# https://realpython.com/python-speech-recognition/
# https://dev.to/abhinowww/how-to-record-audio-in-python-automatically-detect-speech-and-silence-4951
# **************************************************


# **************************************************
import os
from rich import print
import speech_recognition

os.system(command="cls" if os.name == "nt" else "clear")

print(f"Version of 'speech_recognition' package: {speech_recognition.__version__}")
# **************************************************


# **************************************************
# import os
# from rich import print
# import speech_recognition as sr

# os.system(command="cls" if os.name == "nt" else "clear")

# print("=" * 50)

# microphone_names: list = sr.Microphone.list_microphone_names()

# for index, name in enumerate(microphone_names):
#     new_name = str(name).replace("\r", "").replace("\n", "").ljust(80, " ")
#     message = f"Name: {new_name} - Index: {index}"
#     print(message)

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# import os
# from rich import print
# import speech_recognition as sr

# MICROPHONE_DURATION: int = 1
# MICROPHONE_DEVICE_INDEX: int = 1
# MICROPHONE_CHUNK_SIZE: int = 1024
# MICROPHONE_FRAME_RATE: int = 48_000

# os.system(command="cls" if os.name == "nt" else "clear")

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
#     data = audio.get_wav_data()  # type: ignore

#     audio_file_path: str = "../speech_files/LiveRecording.mp3"
#     with open(file=audio_file_path, mode="wb") as file:
#         file.write(data)

#     print("Finished.")
#     print()
# **************************************************


# **************************************************
# import os
# from rich import print
# import speech_recognition as sr

# MICROPHONE_DURATION: int = 1
# MICROPHONE_DEVICE_INDEX: int = 1
# MICROPHONE_CHUNK_SIZE: int = 1024
# MICROPHONE_FRAME_RATE: int = 48_000


# def main() -> None:
#     """Main function."""

#     os.system(command="cls" if os.name == "nt" else "clear")

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
#         data = audio.get_wav_data()

#         audio_file_path: str = "../speech_files/LiveRecording.mp3"
#         with open(file=audio_file_path, mode="wb") as file:
#             file.write(data)

#         print("Finished.")
#         print()


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# import os
# from rich import print
# import speech_recognition as sr

# MICROPHONE_DURATION: int = 1
# MICROPHONE_DEVICE_INDEX: int = 1
# MICROPHONE_CHUNK_SIZE: int = 1024
# MICROPHONE_FRAME_RATE: int = 48_000

# TEMP_AUDIO_FILE_PATH: str = "../speech_files/LiveRecording.mp3"


# def listen(
#     audio_file_path: str,
#     notify: bool = False,
# ) -> None:
#     """Listen to microphone and save audio to file function."""

#     if notify:
#         print("Start Listening...")

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

#         audio = recognizer.listen(source=microphone)

#         if notify:
#             print("Finished Listening.")

#         data = audio.get_wav_data()

#         with open(file=audio_file_path, mode="wb") as file:
#             file.write(data)


# def main() -> None:
#     """Main function."""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     listen(
#         notify=True,
#         audio_file_path=TEMP_AUDIO_FILE_PATH,
#     )


# if __name__ == "__main__":
#     main()
# **************************************************
