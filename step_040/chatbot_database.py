"""
Chatbot Database
"""

import sqlite3 as sqlite
import chatbot_constants as constants


def create_database() -> None:
    """
    Create Database Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
    except Exception as ex:
        print(f"#ERROR: Function: {create_database.__name__} - {ex}")
        exit()
    finally:
        if connection:
            connection.close()


def create_models_table() -> None:
    """
    Create Models Table Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = """
        CREATE TABLE IF NOT EXISTS Models (
            Name                 TEXT NOT NULL,
            PromptTokenPrice     REAL NOT NULL,
            CompletionTokenPrice REAL NOT NULL);
        """
        cursor.execute(query)
        connection.commit()
    except Exception as ex:
        print(f"#ERROR: Function: {create_models_table.__name__} - {ex}")
        exit()
    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def create_users_table() -> None:
    """
    Create Users Table Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = """
        CREATE TABLE IF NOT EXISTS Users (
            Username TEXT NOT NULL,
            Password TEXT NOT NULL,
            Credit   REAL NOT NULL);
        """
        cursor.execute(query)
        connection.commit()

    except Exception as ex:
        print(f"#ERROR: Function: {create_users_table.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def create_user_messages_table() -> None:
    """
    Create User Messages Table Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = """
        CREATE TABLE IF NOT EXISTS UserMessages (
            Username             TEXT NOT NULL,
            Model                TEXT NOT NULL,
            Role                 TEXT NOT NULL,
            Content              TEXT NOT NULL,
            PromptTokens         INT  NOT NULL,
            PromptTokenPrice     REAL NOT NULL,
            CompletionTokens     INT  NOT NULL,
            CompletionTokenPrice REAL NOT NULL,
            TotalPrice           REAL NOT NULL);
        """

        cursor.execute(query)
        connection.commit()
    except Exception as ex:
        print(f"#ERROR: Function: {create_user_messages_table.__name__} - {ex}")
        exit()
    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def seed_models_table() -> None:
    """
    Seed Models Table Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        # ********************
        model_name: str = "gpt-4o".strip().lower()

        query: str = "SELECT * FROM Models WHERE Name=?"
        values: tuple = (model_name,)
        cursor.execute(query, values)
        found_model = cursor.fetchone()

        if not found_model:
            query = "INSERT INTO Models VALUES (:Name, :PromptTokenPrice, :CompletionTokenPrice)"
            values: dict = {
                "Name": model_name,
                "PromptTokenPrice": 3.0,
                "CompletionTokenPrice": 4.0,
            }
            cursor.execute(query, values)
            connection.commit()
        # ********************

        # ********************
        model_name: str = "gpt-4o-mini".strip().lower()

        query: str = "SELECT * FROM Models WHERE Name=?"
        values: tuple = (model_name,)
        cursor.execute(query, values)
        found_model = cursor.fetchone()

        if not found_model:
            query = "INSERT INTO Models VALUES (:Name, :PromptTokenPrice, :CompletionTokenPrice)"
            values: dict = {
                "Name": model_name,
                "PromptTokenPrice": 2.0,
                "CompletionTokenPrice": 3.0,
            }
            cursor.execute(query, values)
            connection.commit()
        # ********************

        # ********************
        model_name: str = "gpt-3.5-turbo".strip().lower()

        query: str = "SELECT * FROM Models WHERE Name=?"
        values: tuple = (model_name,)
        cursor.execute(query, values)
        found_model = cursor.fetchone()

        if not found_model:
            query = "INSERT INTO Models VALUES (:Name, :PromptTokenPrice, :CompletionTokenPrice)"
            values: dict = {
                "Name": model_name,
                "PromptTokenPrice": 1.0,
                "CompletionTokenPrice": 2.0,
            }
            cursor.execute(query, values)
            connection.commit()
        # ********************
    except Exception as ex:
        print(f"#ERROR: Function: {seed_models_table.__name__} - {ex}")
        exit()
    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def seed_users_table() -> None:
    """
    Seed Users Table Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        # ********************
        username: str = "dariush".strip().lower()

        query: str = "SELECT * FROM Users WHERE Username=?"
        values: tuple = (username,)
        cursor.execute(query, values)
        found_user = cursor.fetchone()

        if not found_user:
            query = "INSERT INTO Users VALUES (:Username, :Password, :Credit)"
            values: dict = {
                "Credit": 200.0,
                "Username": username,
                "Password": "1234512345",
            }
            cursor.execute(query, values)
            connection.commit()
        # ********************
    except Exception as ex:
        print(f"#ERROR: Function: {seed_users_table.__name__} - {ex}")
        exit()
    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def initialize() -> None:
    """
    InitializeFunction
    """

    create_database()

    create_users_table()
    create_models_table()
    create_user_messages_table()

    seed_users_table()
    seed_models_table()


def login(username: str, password: str) -> tuple | None:
    """
    Login Function
    """

    try:
        # Username is not Case Sensitive!
        username = username.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = "SELECT * FROM Users WHERE username=? AND password=?"
        values: tuple = (username, password)
        cursor.execute(query, values)
        found_user = cursor.fetchone()

        return found_user

    except Exception as ex:
        print(f"#ERROR: Function: {login.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_user_credit(username: str) -> float:
    """
    Get User Credit Function
    """

    try:
        # Username is not Case Sensitive!
        username = username.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = "SELECT Credit FROM Users WHERE username=?"
        values: tuple = (username,)

        cursor.execute(query, values)
        credit = cursor.fetchone()

        if not credit:
            return 0

        return credit[0]

    except Exception as ex:
        print(f"#ERROR: Function: {get_user_credit.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_model_prices(model_name: str) -> tuple:
    """
    Get Model Prices Function
    """

    try:
        # Model name is not Case Sensitive!
        model_name = model_name.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = (
            "SELECT PromptTokenPrice, CompletionTokenPrice FROM Models WHERE Name=?"
        )
        values: tuple = (model_name,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if not result:
            return 0, 0

        return result

    except Exception as ex:
        print(f"#ERROR: Function: {get_model_prices.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_total_price(
    prompt_tokens: int,
    prompt_token_price: float,
    completion_tokens: int,
    completion_token_price: float,
):
    """
    Get Total Price Function
    """

    total_prompt_token_price = prompt_tokens * prompt_token_price
    total_completion_token_price = completion_tokens * completion_token_price

    total_price: float = total_prompt_token_price + total_completion_token_price

    return total_price


def update_user_credit(username: str, credit: float) -> None:
    """
    Update User Credit Function
    """

    try:
        # Username is not case sensitive!
        username = username.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query = "UPDATE Users SET Credit = :Credit WHERE Username = :Username"
        values: dict = {
            "Credit": credit,
            "Username": username,
        }

        cursor.execute(query, values)
        connection.commit()

    except Exception as ex:
        print(f"#ERROR: Function: {update_user_credit.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def reduce_user_credit(
    username: str,
    amount: float,
) -> None:
    """
    Reduce User Credit Function
    """

    # Username is not case sensitive!
    username = username.strip().lower()

    credit: float = get_user_credit(username=username)
    credit -= amount

    if credit < 0:
        credit = 0.0

    update_user_credit(username=username, credit=credit)


def get_user_messages(username: str) -> list:
    """
    Get User Messages Function
    """

    try:
        # Username is not Case Sensitive!
        username = username.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = "SELECT * FROM UserMessages WHERE Username = ?"
        values: tuple = (username,)
        cursor.execute(query, values)
        result = cursor.fetchall()

        return result

    except Exception as ex:
        print(f"#ERROR: Function: {get_user_messages.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_user_messages_for_ai(username: str) -> list:
    """
    Get User Messages for AI Function
    """

    try:
        # Username is not Case Sensitive!
        username = username.strip().lower()

        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        query: str = "SELECT * FROM UserMessages WHERE Username = ?"
        values: tuple = (username,)
        cursor.execute(query, values)
        result = cursor.fetchall()

        messages: list = []

        if result:
            for item in result:
                message: dict = {
                    constants.KEY_NAME_ROLE: item[2],
                    constants.KEY_NAME_CONTENT: item[3],
                }

                messages.append(message)

        return messages

    except Exception as ex:
        print(f"#ERROR: Function: {get_user_messages_for_ai.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def add_message(
    username: str,
    model_name: str,
    role: str,
    content: str,
    prompt_tokens: int = 0,
    prompt_token_price: float = 0.0,
    completion_tokens: int = 0,
    completion_token_price: float = 0.0,
    total_price: float = 0.0,
) -> None:
    """
    Add Message Function
    """

    try:
        connection = sqlite.connect(database=constants.DATABASE)
        cursor = connection.cursor()

        role = role.strip().lower()
        username = username.strip().lower()
        model_name = model_name.strip().lower()

        query = """INSERT INTO UserMessages VALUES(
                    :Username,
                    :Model,
                    :Role,
                    :Content,
                    :PromptTokens,
                    :PromptTokenPrice,
                    :CompletionTokens,
                    :CompletionTokenPrice,
                    :TotalPrice
                    )"""

        values: dict = {
            "Username": username,
            "Model": model_name,
            "Role": role,
            "Content": content,
            "PromptTokens": prompt_tokens,
            "PromptTokenPrice": prompt_token_price,
            "CompletionTokens": completion_tokens,
            "CompletionTokenPrice": completion_token_price,
            "TotalPrice": total_price,
        }

        cursor.execute(query, values)
        connection.commit()

    except Exception as ex:
        print(f"#ERROR: Function: {add_message.__name__} - {ex}")
        exit()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    print("You must run 'chatbot.py' file!")
