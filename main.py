from pydantic import BaseModel
from ollama import chat

class Country(BaseModel):
    name: str
    capital:str
    population: int
    languages: list[str]

response = chat(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Tell me about Sweden",
        }
    ],
    model="qwen2.5:3b",
    format=Country.model_json_schema(),
) 
country = Country.model_validate_json(response.message.content)   
print(country)

