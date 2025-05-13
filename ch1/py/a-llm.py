from langchain_openai import ChatOpenAI

# Configure the local LM Studio base URL and dummy API key
model = ChatOpenAI(
    openai_api_base="http://localhost:1234/v1"  # type: ignore
)

response = model.invoke("The sky is")
print(response.content)
