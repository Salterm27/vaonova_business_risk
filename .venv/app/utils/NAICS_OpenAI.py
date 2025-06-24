import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()
api_key = os.getenv("openai_key")

client = OpenAI(api_key=api_key)
def fetch_naics_code(business_category: str) -> dict:
    prompt = (
        f"Give the most relevant 2022 NAICS code for the business category '{business_category}'. "
        "Respond with a compact, single-line JSON object like: {\"code\": \"xxxxx\", \"description\": \"...\"}. "
        "Do not include any extra text, line breaks, or formatting. Only return the JSON."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You always return clean, compact, one-line JSON responses only."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Could not parse response as JSON: {content}")