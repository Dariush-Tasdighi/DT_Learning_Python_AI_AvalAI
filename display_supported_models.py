# **************************************************
import os
from rich import print
from dotenv import load_dotenv

# from typing import Final
# from typing import Optional

from typing import (
    Final,
    Optional,
)

from openai import OpenAI
from openai.types import Model

BASE_URL: Final[str] = "https://api.avalai.ir/v1".replace(" ", "").lower()
KEY_NAME_OPENAI_API_KEY: Final[str] = "AVALAI_API_KEY".replace(" ", "").upper()


def sort_function(model):
    """
    Sort items by 'id'
    """

    return model["id"]


def main() -> None:
    """
    The main of program
    """

    os.system(command="cls" if os.name == "nt" else "clear")

    load_dotenv(override=True)
    api_key: Optional[str] = os.getenv(key=KEY_NAME_OPENAI_API_KEY)
    if not api_key:
        error_message: str = (
            f"The '{KEY_NAME_OPENAI_API_KEY}' key not found or is empty"
        )
        raise Exception(error_message)

    client = OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

    data: list[Model] = client.models.list().data

    suported_models: list[dict] = []
    for model in data:
        suported_model: dict = {"id": model.id, "owned_by": model.owned_by}
        suported_models.append(suported_model)

    suported_models.sort(key=sort_function)

    for index, model in enumerate(suported_models, start=1):
        # id: str = model["id"]
        # owned_by: str = model["owned_by"]

        id: str = model.get("id", "NO 'id'")
        owned_by: str = model.get("owned_by", "NO 'owned_by'")

        if "openai" in owned_by.lower():
            owned_by = f"[red]{owned_by}[/red]"

        message: str = f"{index:>3} - {id:<55} - {owned_by}"
        print(message)


if __name__ == "__main__":
    try:
        main()

    except Exception as exception:
        print(f"[red][-] {exception}!")

    finally:
        print()
# **************************************************


# **************************************************
# import os
# from rich import print
# from dotenv import load_dotenv

# from typing import (
#     Final,
#     Optional,
# )

# from openai import OpenAI
# from openai.types import Model

# BASE_URL: Final[str] = "https://api.avalai.ir/v1".replace(" ", "").lower()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "AVALAI_API_KEY".replace(" ", "").upper()


# def sort_function(model):
#     """
#     Sort items by 'id'
#     """

#     return model["id"]


# def main() -> None:
#     """
#     The main of program
#     """

#     os.system(command="cls" if os.name == "nt" else "clear")

#     load_dotenv(override=True)
#     api_key: Optional[str] = os.getenv(key=KEY_NAME_OPENAI_API_KEY)
#     if not api_key:
#         error_message: str = (
#             f"The '{KEY_NAME_OPENAI_API_KEY}' key not found or is empty"
#         )
#         raise Exception(error_message)

#     client = OpenAI(
#         api_key=api_key,
#         base_url=BASE_URL,
#     )

#     data: list[Model] = client.models.list().data

#     suported_models: list[dict] = []
#     for model in data:
#         suported_model: dict = {"id": model.id, "owned_by": model.owned_by}
#         suported_models.append(suported_model)

#     suported_models.sort(key=sort_function)

#     for index, model in enumerate(suported_models, start=1):
#         id: str = model.get("id", "NO 'id'")
#         owned_by: str = model.get("owned_by", "NO 'owned_by'")

#         if "openai" in owned_by.lower():
#             owned_by = f"[red]{owned_by}[/red]"

#         message: str = f"{index:>3} - {id:<55} - {owned_by}"
#         print(message)


# if __name__ == "__main__":
#     try:
#         main()

#     except Exception as exception:
#         print(f"[red][-] {exception}!")

#     finally:
#         print()
# **************************************************
