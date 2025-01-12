![avalai.ir](avalai.png)

# Learning TikToken

## References

- https://pypi.org/project/tiktoken
- https://github.com/openai/tiktoken
- https://platform.openai.com/tokenizer
- https://en.wikipedia.org/wiki/Byte_pair_encoding
- https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

## Setup

- python -m venv .venv

- .\\.venv\Scripts\activate

- python -m pip list

- python -m pip install -U openai
- python -m pip install -U tiktoken
- python -m pip install -U python-dotenv

- python -m pip list

Write / Modify / Run Source Codes(s)!

- deactivate

## Create .env File (For Saving Passwords / API Keys / Access Tokens / ...)

- In the root of project, create a file, with the name of '.env', and write key name(s) and value:
    - AVALAI_API_KEY="..."

## Run

- python .\app.py
