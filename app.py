# **************************************************
API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# **************************************************

# **************************************************
# MODEL_NAME: str = "gpt-4o"
# MODEL_NAME: str = "gpt-4o-mini"
MODEL_NAME: str = "gpt-3.5-turbo"
# MODEL_NAME: str = "gpt-3.5-turbo-instruct"
# **************************************************

# **************************************************
# Sample 0 - Very Simple Sample
# **************************************************
import os
from openai import OpenAI
from dotenv import load_dotenv

# client = OpenAI()

load_dotenv()
api_key = os.getenv(key=API_KEY_NAME)
# print(api_key)
client = OpenAI(api_key=api_key, base_url=BASE_URL)

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Why sky is blue?"}],
)

print("-" * 50)
print(response.choices[0].message.content)
print("-" * 50)
# **************************************************

# **************************************************
# Sample 1
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv(key=API_KEY_NAME)
# client = OpenAI(api_key=api_key, base_url=BASE_URL)

# response = client.chat.completions.create(
#     stream=False,
#     temperature=0.7,  # Recommanded: between 0 to 1
#     model=MODEL_NAME,
#     messages=[{"role": "user", "content": "Why sky is blue?"}],
# )

# print("-" * 50)
# print("Type of Response:", type(response))
# print("-" * 50)
# print(response)
# print("-" * 50)
# print(response.choices[0].message.content)
# print("-" * 50)
# **************************************************

# **************************************************
# ChatCompletion(
#   id='chatcmpl-AfU5Gq7i4G9pinKpxAg8Y5MjRBnhJ',
#   choices=[
#       Choice(
#           finish_reason='stop',
#           index=0,
#           logprobs=None,
#           message=ChatCompletionMessage(
#               content="Why don't scientists trust atoms? \n\nBecause they make up everything!",
#               refusal=None,
#               role='assistant',
#               audio=None,
#               function_call=None,
#               tool_calls=None
#           )
#       )
#   ],
#   created=1734450454,
#   model='gpt-3.5-turbo-0125',
#   object='chat.completion',
#   service_tier=None,
#   system_fingerprint=None,
#   usage=CompletionUsage(
#       completion_tokens=14,
#       prompt_tokens=11,
#       total_tokens=25,
#       completion_tokens_details=CompletionTokensDetails(
#           accepted_prediction_tokens=0,
#           audio_tokens=0,
#           reasoning_tokens=0,
#           rejected_prediction_tokens=0
#       ),
#       prompt_tokens_details=PromptTokensDetails(
#           audio_tokens=0,
#           cached_tokens=0
#       )
#   )
# )
# **************************************************

# **************************************************
# Sample 2 - Streaming
# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# api_key = os.getenv(key=API_KEY_NAME)
# client = OpenAI(api_key=api_key, base_url=BASE_URL)

# response_stream = client.chat.completions.create(
#     stream=True,
#     temperature=0.7,
#     model=MODEL_NAME,
#     messages=[
#         {"role": "user", "content": "Tell me a short story about science fiction."}
#     ],
# )

# print("-" * 50)

# for chunk in response_stream:
#     if chunk.choices[0].finish_reason == "stop":
#         break

#     content = chunk.choices[0].delta.content
#     if content is not None:
#         print(content, end="")

# print()
# print("-" * 50)
# **************************************************

# **************************************************
# Sample 3
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()
# api_key = os.getenv(key=API_KEY_NAME)
# client = OpenAI(api_key=api_key, base_url=BASE_URL)

# start_time: float = time.time()

# response = client.chat.completions.create(
#     stream=False,
#     temperature=0.7,
#     model=MODEL_NAME,
#     messages=[{"role": "user", "content": "Tell me a joke."}],
# )

# response_time: float = time.time() - start_time

# print("-" * 50)
# print(response.choices[0].message.content)
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("-" * 50)
# **************************************************

# **************************************************
# Sample 4
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv


# def chat_completions(messages, model_name: str, temperature: float = 0.7) -> str:
#     """
#     Chat Completions Function
#     """

#     response = client.chat.completions.create(
#         stream=False,
#         model=model_name,
#         messages=messages,
#         temperature=temperature,
#     )

#     content: str = response.choices[0].message.content

#     return content


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     load_dotenv()
#     api_key = os.getenv(key=API_KEY_NAME)

#     global client
#     client = OpenAI(api_key=api_key, base_url=BASE_URL)

#     user_prompt: str = input("User: ")

#     messages = []

#     # نکته مهم: پیغام سیستم، باید فقط
#     # یک‌بار، و حتما در ابتدا نوشته شود
#     system_prompt: str = "You are a helpful AI assistant."
#     system_message = {"role": "system", "content": system_prompt}
#     messages.append(system_message)

#     user_message = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     start_time: float = time.time()
#     assistant_answer: str = chat_completions(messages=messages, model_name=MODEL_NAME)
#     response_time: float = time.time() - start_time

#     print("-" * 50)
#     print(assistant_answer)
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("-" * 50)


# if __name__ == "__main__":
#     main()
# **************************************************

# **************************************************
# Sample 5 - Simple Chatbot - Without History
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv


# def chat_completions(messages, model_name: str, temperature: float = 0.7) -> str:
#     """
#     Chat Completions Function
#     """

#     response = client.chat.completions.create(
#         stream=False,
#         model=model_name,
#         messages=messages,
#         temperature=temperature,
#     )

#     content: str = response.choices[0].message.content

#     return content


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     load_dotenv()
#     api_key = os.getenv(key=API_KEY_NAME)

#     global client
#     client = OpenAI(api_key=api_key, base_url=BASE_URL)

#     while True:
#         user_prompt: str = input("User: ")

#         if user_prompt.lower() in ["exit", "quit", "bye"]:
#             break

#         messages = []

#         system_prompt: str = "You are a helpful AI assistant."
#         system_message = {"role": "system", "content": system_prompt}
#         messages.append(system_message)

#         user_message = {"role": "user", "content": user_prompt}
#         messages.append(user_message)

#         start_time: float = time.time()
#         assistant_answer: str = chat_completions(
#             messages=messages, model_name=MODEL_NAME
#         )
#         response_time: float = time.time() - start_time

#         print("-" * 50)
#         print(assistant_answer)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("-" * 50)
#         print()


# if __name__ == "__main__":
#     main()
# **************************************************

# **************************************************
# Sample 6 - Simple Chatbot - With History
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv


# def chat_completions(messages, model_name: str, temperature: float = 0.7) -> str:
#     """
#     Chat Completions Function
#     """

#     response = client.chat.completions.create(
#         stream=False,
#         model=model_name,
#         messages=messages,
#         temperature=temperature,
#     )

#     content: str = response.choices[0].message.content

#     return content


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     load_dotenv()
#     api_key = os.getenv(key=API_KEY_NAME)

#     global client
#     client = OpenAI(api_key=api_key, base_url=BASE_URL)

#     messages = []

#     system_prompt = "You are a helpful AI assistant."
#     system_message = {"role": "system", "content": system_prompt}
#     messages.append(system_message)

#     while True:
#         user_prompt: str = input("User: ")

#         if user_prompt.lower() in ["exit", "quit", "bye"]:
#             break

#         user_message = {"role": "user", "content": user_prompt}
#         messages.append(user_message)

#         start_time: float = time.time()
#         assistant_answer: str = chat_completions(
#             messages=messages, model_name=MODEL_NAME
#         )
#         response_time: float = time.time() - start_time

#         assistant_message = {"role": "assistant", "content": assistant_answer}
#         messages.append(assistant_message)

#         print("-" * 50)
#         print(assistant_answer)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("-" * 50)
#         print()


# if __name__ == "__main__":
#     main()
# **************************************************

# **************************************************
# Sample 7 - Simple AI Agent - Without History
# It is a Perfect Dictionary
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv


# def chat_completions(messages, model_name: str, temperature: float = 0.7) -> str:
#     """
#     Chat Completions Function
#     """

#     response = client.chat.completions.create(
#         stream=False,
#         model=model_name,
#         messages=messages,
#         temperature=temperature,
#     )

#     content: str = response.choices[0].message.content

#     return content


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     load_dotenv()
#     api_key = os.getenv(key=API_KEY_NAME)

#     global client
#     client = OpenAI(api_key=api_key, base_url=BASE_URL)

#     # system_prompt: str = "You are a helpful AI assistant."

#     system_prompt: str = """
#     You are a professional translator assistant from English language to Farsi language.

#     User must write just one word in English language.

#     If user wrote more than one word, or one word but \
#     not in English language, answer 'Error! Try Again...'.

#     Just translate English word, based on the below instructions.

#     Write the translated to Farsi language of user word in ## part.
#     Write the English Pronounce of user word in ### part.
#     Write the 5 English Synonyms in #### parts.
#     Write the 2 English Antonyms in ##### parts.
#     Write the 2 sample and simple English sentences in ###### parts.

#     Just write the below text based on above instructions and replace '#' \
#     with your answers and never write '#' in your result.

#     Translated to Farsi Language: ##
#     English Pronounce: ###

#     Synonyms:
#     1. ####
#     2. ####
#     3. ####
#     4. ####
#     5. ####

#     Antonyms:
#     1. #####
#     2. #####

#     Two Sample Sentences:
#     1. ######
#     2. ######
#     """

#     while True:
#         user_prompt: str = input("User: ")

#         if user_prompt.lower() in ["exit", "quit", "bye"]:
#             break

#         messages = []

#         system_message = {"role": "system", "content": system_prompt}
#         messages.append(system_message)

#         user_message = {"role": "user", "content": user_prompt}
#         messages.append(user_message)

#         start_time: float = time.time()
#         assistant_answer: str = chat_completions(
#             messages=messages, model_name=MODEL_NAME
#         )
#         response_time: float = time.time() - start_time

#         print("-" * 50)
#         print(assistant_answer)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("-" * 50)
#         print()


# if __name__ == "__main__":
#     main()
# **************************************************
