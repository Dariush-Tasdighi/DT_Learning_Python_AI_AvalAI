"""
Chatbot - With History - With Database
"""

import os
import chatbot_ui as ui
import chatbot_database as database


def main() -> None:
    """
    Main Function
    """

    os.system(command="cls")

    database.initialize()

    username: str = ui.login()

    ui.chat(username=username)


if __name__ == "__main__":
    main()
