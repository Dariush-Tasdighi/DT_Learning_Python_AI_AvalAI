# **************************************************
embedding_model_name = "text-embedding-ada-002"
# embedding_model_name = "text-embedding-3-small"
# embedding_model_name = "text-embedding-3-large"
# **************************************************

# **************************************************
# Step (1)
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
# print(api_key)

# client = OpenAI(api_key=api_key, base_url=base_url)

# start_time = time.time()

# input = "Hello, World!"

# response = client.embeddings.create(
#     input=input,
#     model=embedding_model_name,
# )

# response_time = time.time() - start_time

# print("-" * 50)
# print("Type of completion:", type(response))
# print("-" * 50)
# print(response)
# print("-" * 50)
# print(response.data[0].embedding)
# print("-" * 50)
# print("Length of the embedding:", len(response.data[0].embedding))
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("-" * 50)
# **************************************************

# **************************************************
# {
#   "object": "list",
#   "data": [
#     {
#       "object": "embedding",
#       "index": 0,
#       "embedding": [
#         -0.006929283495992422,
#         -0.005336422007530928,
#         -4.547132266452536e-05,
#         -0.024047505110502243
#       ],
#     }
#   ],
#   "model": "text-embedding-3-small",
#   "usage": {
#     "prompt_tokens": 5,
#     "total_tokens": 5
#   }
# }
# **************************************************

# **************************************************
# Step (2)
# **************************************************
# import os
# import json  # New
# import time
# import numpy as np  # New
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# api_key_name = "AVALAI_API_KEY"
# base_url = "https://api.avalai.ir/v1"
# api_key = os.getenv(key=api_key_name)
# print(api_key)

# client = OpenAI(api_key=api_key, base_url=base_url)

# start_time = time.time()

# input = "Hello, World!"

# response = client.embeddings.create(
#     input=input,
#     model=embedding_model_name,
# )

# response_time = time.time() - start_time

# print("-" * 50)

# print("Type of completion:", type(response))
# print("-" * 50)

# print("response:\n")
# print(response)
# print("-" * 50)

# print("response.data[0].embedding:\n")
# print(response.data[0].embedding)
# print("-" * 50)

# response_json = response.model_dump_json()
# print("response_json:\n")
# print(response_json)
# print("-" * 50)

# result = json.loads(response_json)
# print("result:\n")
# print(result)
# print("-" * 50)

# embeddings = result["data"][0]["embedding"]
# print("embeddings:\n")
# print(embeddings)
# print("-" * 50)

# embeddings_array = np.array(embeddings)
# print("Length of the embeddings_array:", len(embeddings_array))
# print("-" * 50)

# print(f"Full response received {response_time:.2f} seconds after request.")
# print("-" * 50)
# **************************************************

# **************************************************
# Step (3)
# **************************************************
import os
import json
import numpy as np
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv


def generate_embeddings(input: str) -> np.ndarray:
    response = client.embeddings.create(
        input=input,
        model=embedding_model_name,
    )

    response_json = response.model_dump_json()
    result = json.loads(response_json)
    embeddings = result["data"][0]["embedding"]
    embeddings_array = np.array(embeddings)
    return embeddings_array


def cosine_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    similarity = dot_product / (norm1 * norm2)
    return similarity


os.system(command="cls")

load_dotenv()

api_key_name = "AVALAI_API_KEY"
base_url = "https://api.avalai.ir/v1"
api_key = os.getenv(key=api_key_name)
# print(api_key)

client = OpenAI(api_key=api_key, base_url=base_url)

data = [
    "Hello, World!",
    "Hello universe!",
    "What's up? How have you been doing?",
    "He just said Hello and he was gone.",
    "Emily said hello.",
]

query = "Hello"

cosine_similarity_list = []
query_embedding = generate_embeddings(input=query)

for item in data:
    item_embedding = generate_embeddings(input=item)
    cosine_similarity_value = cosine_similarity(
        embedding1=query_embedding, embedding2=item_embedding
    )
    cosine_similarity_list.append(cosine_similarity_value)

df = pd.DataFrame({"Text": data, "Cosine Similarity": cosine_similarity_list})

print("-" * 50)
print("Data Similarity Result:\n")
print(df)

print("-" * 50)
print("Top 2 Similar Indexes:\n")
top_2_similar_indexes = df["Cosine Similarity"].nlargest(n=2).index
print(top_2_similar_indexes)

print("-" * 50)
print("Top 2 Similar Texts:\n")
top_2_similar_texts = df.loc[top_2_similar_indexes.tolist(), "Text"]
print(top_2_similar_texts)

print("-" * 50)
# **************************************************
