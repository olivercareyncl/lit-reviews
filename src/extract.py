import json
from openai import OpenAI
from .schemas import extraction_schema

MODEL = "gpt-4.1"

def extract_metadata(text: str) -> dict:
    client = OpenAI()
    prompt = open("config/prompts/extract.md", encoding="utf-8").read() + "\n\n" + text
    resp = client.responses.create(
        model=MODEL,
        input=[{"role": "user", "content": prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "Extract", "schema": extraction_schema, "strict": True}},
    )
    content = resp.output[0].content[0].text
    return json.loads(content) if isinstance(content, str) else content
