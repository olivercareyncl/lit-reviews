# src/openai_client.py
import os
from openai import OpenAI

def get_client():
    # expects OPENAI_API_KEY in env (put it in .env locally / Codespaces secrets)
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# centralise model names so you can switch later
MODEL_SCREEN = "gpt-4o"         # good balance for classification
MODEL_EXTRACT = "gpt-4.1"       # strong reasoning for structured pulls
MODEL_EMBED = "text-embedding-3-large"
MODERATION = "omni-moderation-latest"
