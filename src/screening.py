import json
from openai import OpenAI
from .schemas import screening_schema

MODEL = "gpt-4o"

def screen_text(text: str) -> dict:
    client = OpenAI()
    prompt = open("config/prompts/screening.md", encoding="utf-8").read() + "\n\n" + text
    resp = client.responses.create(
        model=MODEL,
        input=[{"role": "user", "content": prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "Screen", "schema": screening_schema, "strict": True}},
    )
    content = resp.output[0].content[0].text
    return json.loads(content) if isinstance(content, str) else content
