# **************************************************
# Simple AI Agent - Without History
# It is a Perfect Text Translator
# **************************************************
# می‌خواهم به زبان انگلیسی، یک System Prompt حرفه‌ای بنویسی که آن را برای Model خودم تعریف نمایم، تا موارد ذیل را به درستی و با دقت انجام دهد:
# ۱. مدل من، یک مترجم حرفه‌ای، از زبان انگلیسی به زبان فارسی باشد.
# ۲. مدل من، باید متن را به صورت کاملا ادبی، روان، شیوا و سلیس، به زبان فارسی ترجمه کند.
# ۳. مدل من، باید صرفا متن را به فارسی ترجمه نماید و نباید از کلمات انگلیسی و یا زبان دیگری، در متن استفاده کند.
# ۴. مدل من، باید از کلماتی استفاده کند که کاملا با معنی بوده و مرتبط با متن باشد، لذا باید در انتخاب کلمات بسیار دقت کند.
# ۵. مدل من، باید در هنگام ترجمه، تمام اصول آیین نگارش را رعایت کند.
# ۶. مدل من، باید در کلماتی که به زبان فارسی می‌نویسد، نیم فاصله‌ها را به دقت رعایت نماید:
# - به عنوان مثال، به جای نوشتن کلمه 'می شود'، باید بنویسد: 'می‌شود'.
# - به عنوان مثال، به جای نوشتن کلمه 'زمینه ها'، باید بنویسد: زمینه‌ها.
# **************************************************
import os
from openai import OpenAI
from dotenv import load_dotenv

MODEL_NAME: str = "gpt-4o"
# MODEL_NAME: str = "gpt-4o-mini"
# MODEL_NAME: str = "gpt-3.5-turbo"

KEY_NAME_API_KEY: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"

SYSTEM_PROMPT: str = """
You are a professional translation model that translates text from English to Persian.

Your translations must adhere to the following guidelines:

1. Language Exclusivity: Translate the provided text exclusively into Persian. Do not include any English words or words from any other language in your output.
2. Literary Quality: Ensure that the translation is literary, fluent, eloquent, and smooth. The text should read naturally and with high-level stylistic quality.
3. Accurate Word Choice: Carefully select words that precisely capture the meaning and context of the original text. Each word must be both semantically accurate and contextually appropriate.
4. Adherence to Persian Grammar: Follow all principles of Persian grammar, punctuation, and standard orthography without exception.
5. Correct Use of Half-Spaces: Pay meticulous attention to the correct usage of half-spaces (نیم فاصله) in Persian. For example:
- Use "می‌شود" instead of "می شود".
- Use "زمینه‌ها" instead of "زمینه ها".
Your output should be a refined, accurate, and stylistically polished Persian translation of the provided English text.
"""

SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}


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


def chat_completions(
    messages: list[dict],
    temperature: float = 0.7,
    model_name: str = "gpt-3.5-turbo",
) -> str:
    """
    Chat Completions Function
    """

    api_key: str = get_api_key()

    client = OpenAI(api_key=api_key, base_url=BASE_URL)

    response = client.chat.completions.create(
        stream=False,
        model=model_name,
        messages=messages,
        temperature=temperature,
    )

    content: str | None = response.choices[0].message.content

    if not content:
        content = "No content received!"

    return content


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    source_file_path: str = "./files/sample.txt"
    target_file_path: str = "./files/sample_translated.txt"

    with open(file=source_file_path, mode="rt", encoding="utf-8") as source_file, open(
        file=target_file_path, mode="wt", encoding="utf-8"
    ) as target_file:
        paragraphs: list[str] = source_file.read().split("\n\n")

        for paragraph in paragraphs:
            messages: list[dict] = []

            messages.append(SYSTEM_MESSAGE)

            user_message: dict = {"role": "user", "content": paragraph}
            messages.append(user_message)

            assistant_answer: str = chat_completions(
                temperature=0.0,
                messages=messages,
                model_name=MODEL_NAME,
            )

            target_file.write(assistant_answer)
            target_file.write("\n\n")


if __name__ == "__main__":
    main()

    print("Finished.")
