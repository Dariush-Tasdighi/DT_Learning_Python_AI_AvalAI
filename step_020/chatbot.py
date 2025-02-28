"""
Simple Chatbot - With History
"""

import os
import time
import chatbot_constants as constants
import chatbot_functions as functions


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    messages: list = []
    messages.append(constants.SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input("User: ")

        if user_prompt.lower() in ["exit", "quit", "bye"]:
            break

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

        if not assistant_answer:
            # Remove Last Messages!
            messages.pop()
        else:
            assistant_message = {
                constants.KEY_NAME_ROLE: constants.ROLE_ASSISTANT,
                constants.KEY_NAME_CONTENT: assistant_answer,
            }

            messages.append(assistant_message)

        print("-" * 50)
        print(assistant_answer)
        print("-" * 50)
        print("Prompt Tokens:", prompt_tokens)
        print("-" * 50)
        print("Completion Tokens:", completion_tokens)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)
        print()


if __name__ == "__main__":
    main()
