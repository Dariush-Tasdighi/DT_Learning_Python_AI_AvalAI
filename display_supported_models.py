# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# api_key_name = "AVALAI_API_KEY"
# base_url = "https://api.avalai.ir/v1"
# api_key = os.getenv(key=api_key_name)

# client = OpenAI(api_key=api_key, base_url=base_url)

# models = client.models.list().data

# for model in models:
#     print(model)
# **************************************************

# **************************************************
# import os
# from openai import OpenAI
# from dotenv import load_dotenv


# def sort_function(model):
#     return model["id"]


# os.system(command="cls")

# load_dotenv()

# api_key_name = "AVALAI_API_KEY"
# base_url = "https://api.avalai.ir/v1"
# api_key = os.getenv(key=api_key_name)

# client = OpenAI(api_key=api_key, base_url=base_url)

# data = client.models.list().data

# suported_models = []
# for model in data:
#     suported_models.append({"id": model.id, "owned_by": model.owned_by})

# # print(type(suported_models))  # <class 'list'>
# suported_models.sort(key=sort_function)

# for model in suported_models:
#     # print("Id:", model["id"], "Owned By:", model["owned_by"])
#     print(
#         "Id:",
#         model["id"],
#         " " * (50 - len(model["id"])),
#         "Owned By:",
#         model["owned_by"],
#     )
# **************************************************

# **************************************************
import os
from openai import OpenAI
from colorama import Fore
from dotenv import load_dotenv


def sort_function(model):
    return model["id"]


os.system(command="cls")

load_dotenv()

api_key_name = "AVALAI_API_KEY"
base_url = "https://api.avalai.ir/v1"
api_key = os.getenv(key=api_key_name)

client = OpenAI(api_key=api_key, base_url=base_url)

data = client.models.list().data

suported_models = []
for model in data:
    suported_models.append({"id": model.id, "owned_by": model.owned_by})

suported_models.sort(key=sort_function)

for index, model in enumerate(suported_models):
    id: str = model["id"]
    owned_by: str = model["owned_by"]

    if "openai" in owned_by:
        owned_by = f"{Fore.RED}{owned_by}{Fore.RESET}"

    message = f"Id: {id.ljust(50, " ")} Owned By: {owned_by}"

    if index % 2 == 0:
        print(f"{Fore.WHITE}{message}{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}{message}{Fore.RESET}")

print()
# **************************************************
