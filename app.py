# **************************************************
model_name = "gpt-4o"
# model_name = "gpt-4o-mini"
# model_name = "gpt-3.5-turbo"
# model_name = "gpt-3.5-turbo-instruct"
# **************************************************

# **************************************************
# Just Check The API
# **************************************************
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

os.system(command="cls")

load_dotenv()

api_key_name = "AVALAI_API_KEY"
base_url = "https://api.avalai.ir/v1"
api_key = os.getenv(key=api_key_name)
client = OpenAI(api_key=api_key, base_url=base_url)

start_time = time.time()

chat_completion = client.chat.completions.create(
    stream=False,
    temperature=0.8,  # Recommanded: between 0 to 1
    model=model_name,
    messages=[{"role": "user", "content": "Tell me a joke."}],
)

response_time = time.time() - start_time

print("-" * 50)
print("Type of completion:", type(chat_completion))
print("-" * 50)
print(chat_completion)
print("-" * 50)
print(chat_completion.choices[0].message.content)
print("-" * 50)
print(f"Full response received {response_time:.2f} seconds after request.")
print("-" * 50)
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
# Just Check The API with Streaming
# **************************************************
# import os
# import time
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# api_key_name = "AVALAI_API_KEY"
# base_url = "https://api.avalai.ir/v1"
# api_key = os.getenv(key=api_key_name)
# client = OpenAI(api_key=api_key, base_url=base_url)

# start_time = time.time()

# chat_stream = client.chat.completions.create(
#     stream=True,
#     temperature=0.8,  # Recommanded: between 0 to 1
#     model=model_name,
#     messages=[{"role": "user", "content": "Why sky is blue?"}],
# )

# print("-" * 50)

# for chunk in chat_stream:
#     if chunk.choices[0].finish_reason == "stop":
#         break

#     content = chunk.choices[0].delta.content
#     if content is not None:
#         print(content, end="")

# response_time = time.time() - start_time

# print()
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("-" * 50)
# **************************************************
