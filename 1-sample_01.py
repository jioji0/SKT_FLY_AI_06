import openai

#edit with your infomation
OPENAI_API_KEY = "add your key"
OPENAI_API_VERSION = "2023-05-15"
OPENAI_API_TYPE = "azure"
OPENAI_ENDPOINT = "add your endpoint"

MODEL_NAME = "dev-gpt-4o-mini"

openai.api_key = OPENAI_API_KEY
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION
openai.azure_endpoint = OPENAI_ENDPOINT

query = input("궁굼한걸 물어보세요! :")

response = openai.chat.completions.create(
                model = MODEL_NAME,
                messages = [
                    {"role":"system","content":"Your are a helpful assiatant."},
                    {"role":"user","content":query}
                ]
            )

print(response.choices[0].message.content)
