"""
Chatbot UI
"""

import time
from pprint import pprint
import chatbot_database as database
import chatbot_constants as constants
import chatbot_functions as functions


def login() -> tuple:
    """
    Login Function
    """

    username: str = input("Username: ")
    password: str = input("Password:")

    # Username is not case sensitive!
    username = username.strip().lower()

    found_user: None | tuple = database.login(username=username, password=password)

    if not found_user:
        print("Username and / or password is not correct!")
        exit()

    return username


def chat(username: str) -> None:
    """
    Chat Function
    """

    prompt_token_price, completion_token_price = database.get_model_prices(
        model_name=constants.MODEL_NAME
    )

    # print("." * 50)  # TODO
    # print("prompt_token_price:", prompt_token_price)  # TODO
    # print("completion_token_price:", completion_token_price)  # TODO
    # print("." * 50)  # TODO

    while True:
        credit: float = database.get_user_credit(username=username)

        if credit <= 0:
            print("You do not have any credit!")
            exit()

        messages: list = database.get_user_messages_for_ai(username=username)

        # print("." * 50)  # TODO
        # pprint(messages)  # TODO
        # print("." * 50)  # TODO

        if len(messages) == 0:
            messages.append(constants.SYSTEM_MESSAGE)

            database.add_message(
                username=username,
                model_name=constants.MODEL_NAME,
                role=constants.ROLE_SYSTEM,
                content=constants.SYSTEM_PROMPT,
            )

        print("=" * 50)
        user_prompt: str = input(f"User ({credit}): ")

        if user_prompt.lower() in ["exit", "quit", "bye"]:
            exit()

        user_message = {
            constants.KEY_NAME_ROLE: constants.ROLE_USER,
            constants.KEY_NAME_CONTENT: user_prompt,
        }

        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = functions.chat_completions(
            messages=messages,
            model_name=constants.MODEL_NAME,
            temperature=constants.TEMPERATURE,
        )

        response_time: float = time.time() - start_time

        total_price: float = database.get_total_price(
            prompt_tokens=prompt_tokens,
            prompt_token_price=prompt_token_price,
            completion_tokens=completion_tokens,
            completion_token_price=completion_token_price,
        )

        # print("." * 50)  # TODO
        # print("Total Price:", total_price)  # TODO
        # print("." * 50)  # TODO

        if assistant_answer:
            database.reduce_user_credit(
                username=username,
                amount=total_price,
            )

            database.add_message(
                username=username,
                model_name=constants.MODEL_NAME,
                role=constants.ROLE_USER,
                content=user_prompt,
            )

            database.add_message(
                username=username,
                model_name=constants.MODEL_NAME,
                role=constants.ROLE_ASSISTANT,
                content=assistant_answer,
                prompt_tokens=prompt_tokens,
                prompt_token_price=prompt_token_price,
                completion_tokens=completion_tokens,
                completion_token_price=completion_token_price,
                total_price=total_price,
            )

        print("-" * 50)
        print(assistant_answer)
        print("-" * 50)
        print("Total Price:", total_price)
        print("-" * 50)
        print("Prompt Tokens:", prompt_tokens)
        print("-" * 50)
        print("Completion Tokens:", completion_tokens)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)
        print()


if __name__ == "__main__":
    print("You must run 'chatbot.py' file!")
