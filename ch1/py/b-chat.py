from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

model = ChatOpenAI(
    model="llama-4-scout-17b-16e-instruct",  # or whatever model name you loaded in LM Studio
    base_url="http://localhost:1234/v1",  # default LM Studio OpenAI-compatible endpoint
    api_key="lm-studio"  # dummy key, required by the client but not validated by LM Studio
)
prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)
