import os
import asyncio

from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

KEY_NAME_API_KEY: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# TTS_MODEL_NAME: str = "gpt-4o-mini-tts"
# TTS_MODEL_NAME: str = "gpt-4o-mini-audio-preview"
# TTS_MODEL_NAME: str = "gpt-4o-audio-preview"
TTS_MODEL_NAME: str = "gpt-4o-mini-transcribe"


def get_api_key() -> str:
    """
    Get API Key Function
    """

    load_dotenv()

    api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
    if not api_key:
        print("API Key not found!")
        exit()

    return api_key


api_key: str = get_api_key()
openai = AsyncOpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)

input = """Thank you for contacting us. I completely understand your frustration with the canceled flight, and I'm here to help you get rebooked quickly.\n\nI just need a few details from your original reservation, like your booking confirmation number or passenger info. Once I have those, I'll find the next available flight and make sure you reach your destination smoothly."""

instructions = """Voice Affect: Calm, composed, and reassuring; project quiet authority and confidence.\n\nTone: Sincere, empathetic, and gently authoritative—express genuine apology while conveying competence.\n\nPacing: Steady and moderate; unhurried enough to communicate care, yet efficient enough to demonstrate professionalism.\n\nEmotion: Genuine empathy and understanding; speak with warmth, especially during apologies (\"I'm very sorry for any disruption...\").\n\nPronunciation: Clear and precise, emphasizing key reassurances (\"smoothly,\" \"quickly,\" \"promptly\") to reinforce confidence.\n\nPauses: Brief pauses after offering assistance or requesting details, highlighting willingness to listen and support."""


async def main() -> None:
    """
    Main Function
    """

    async with openai.audio.speech.with_streaming_response.create(
        input=input,
        voice="coral",
        model=TTS_MODEL_NAME,
        response_format="pcm",
        instructions=instructions,
    ) as response:
        await LocalAudioPlayer().play(response)


if __name__ == "__main__":
    asyncio.run(main())
