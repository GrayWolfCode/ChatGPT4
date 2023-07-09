import openai
from dotenv import load_dotenv
import os 

load_dotenv()

api_key_openai=os.environ.get("API_KEY")
openai.api_key=api_key_openai

def get_response(prompt, model="text-curie-002", max_tokens=150):
    response = openai.Completion.create(
        engine=model, #or "your_chosen_engine",
        prompt=prompt,
        max_tokens=max_tokens,
        n=5,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()

t=get_response("What is your name?")
print(t)