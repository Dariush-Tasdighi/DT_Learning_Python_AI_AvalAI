# pip install assemblyai
# python -m pip install -U assemblyai
# https://www.assemblyai.com/docs/concepts/supported-languages

import os
import assemblyai as aai

os.system(command="cls")

aai.settings.api_key = "317e8416e2d7413ab44d0761a2062bdf"

# audio_file_path: str = "https://assembly.ai/wildfires.mp3"
audio_file_path: str = "../speech_files/sample_01.mp3"

config = aai.TranscriptionConfig(
    language_code="fa",
    speech_model=aai.SpeechModel.nano,
)

transcript = aai.Transcriber(config=config).transcribe(audio_file_path)

if transcript.status == "error":
    raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)
