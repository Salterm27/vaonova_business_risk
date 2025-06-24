import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()
api_key = os.getenv("openai_key")

client = OpenAI(api_key=api_key)

def fetch_naics_code(business_category: str) -> str:
    prompt = (
        f"What is the most relevant 2022 NAICS code for a business in the category: '{business_category}'? "
        "Only return the 6-digit NAICS code followed by a brief description."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant knowledgeable about business classifications and NAICS codes."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response['choices'][0]['message']['content'].strip()