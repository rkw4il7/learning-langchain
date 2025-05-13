from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
model = ChatOpenAI(
    openai_api_base="http://localhost:1234/v1"  # type: ignore
)

prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)

