"""
Chatbot
"""

import os
from pprint import pprint
import chatbot_database as database

# **********
ROLE_KEY_NAME: str = "role".strip().lower()
CONTENT_KEY_NAME: str = "content".strip().lower()

ROLE_USER: str = "user".strip().lower()
ROLE_SYSTEM: str = "system".strip().lower()
ROLE_ASSISTANT: str = "assistant".strip().lower()
# **********

# **********
# MODEL_NAME: str = "gpt-4o".strip().lower()
# MODEL_NAME: str = "gpt-4o-mini".strip().lower()
MODEL_NAME: str = "gpt-3.5-turbo".strip().lower()
# MODEL_NAME: str = "gpt-3.5-turbo-instruct".strip().lower()
# **********

os.system(command="cls")

print("-" * 50)

database.initialize_database()

print("-" * 50)

print(database.login(username="alireza", password="12345"))
print(database.login(username="dariush", password="12345"))
print(database.login(username="DARIUSH", password="1234512345"))
print(database.login(username="dariush", password="1234512345"))

print("-" * 50)

print(database.get_user_credit(username="alireza"))
print(database.get_user_credit(username="DARIUSH"))
print(database.get_user_credit(username="dariush"))

print("-" * 50)

print(database.get_model_prices(model_name="Googooli"))
print(database.get_model_prices(model_name="GPT-4O"))
print(database.get_model_prices(model_name="gpt-4o"))
print(database.get_model_prices(model_name="gpt-4o-mini"))
print(database.get_model_prices(model_name="gpt-3.5-turbo"))
print(database.get_model_prices(model_name=MODEL_NAME))

print("-" * 50)

print(database.get_user_credit(username="DARIUSH"))

total_price = database.get_total_price(
    prompt_tokens=10,
    prompt_token_price=2,
    completion_tokens=20,
    completion_token_price=3,
)
print("Total Price:", total_price)

database.reduce_user_credit(
    username="Dariush",
    amount=total_price,
)

print(database.get_user_credit(username="DARIUSH"))

print("-" * 50)

pprint(database.get_user_messages(username="Ali"))
pprint(database.get_user_messages(username="Dariush"))

print("-" * 50)

database.add_user_message(
    username="Dariush",
    model_name=MODEL_NAME,
    role=ROLE_SYSTEM,
    content="System Content 1",
)

database.add_user_message(
    username="Dariush",
    model_name=MODEL_NAME,
    role=ROLE_USER,
    content="User Content 1",
)

database.add_user_message(
    username="Dariush",
    model_name=MODEL_NAME,
    role=ROLE_ASSISTANT,
    content="Assistant Content 1",
    prompt_tokens=10,
    prompt_token_price=2,
    completion_tokens=20,
    completion_token_price=3,
    total_price=total_price,
)

pprint(database.get_user_messages(username="Dariush"))

print("-" * 50)

print("End")
