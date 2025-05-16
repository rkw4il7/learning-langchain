from langchain_openai.chat_models import ChatOpenAI

# Set up your local LM Studio server details
model = ChatOpenAI(
    model="llama-4-scout-17b-16e-instruct",  # or whatever model name you loaded in LM Studio
    base_url="http://localhost:1234/v1",  # default LM Studio OpenAI-compatible endpoint
    api_key="lm-studio"  # dummy key, required by the client but not validated by LM Studio
)

response = model.invoke("Name all of the LLMs and their providers.")
print(response.content)
