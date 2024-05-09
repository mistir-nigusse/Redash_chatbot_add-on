import os
from dotenv import load_dotenv

# Load the .env file
x = load_dotenv(".env")


class Config:
    RANDOM_SEED: int = int(os.getenv("RANDOM_SEED", default="1729"))
    OPENAI_API_KEY: str = os.getenv("sk-proj-TxjgIUKpU0twgu9OvnIbT3BlbkFJ4RJ1lt3hCT5ZB9Mv7vYH")

    if OPENAI_API_KEY is None:
        raise EnvironmentError("Environment variables not found. Check your .env file or environment.")