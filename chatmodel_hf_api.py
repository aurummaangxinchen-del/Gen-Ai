
from dotenv import load_dotenv,find_dotenv
from langchain_core.messages import AIMessage, HumanMessage,SystemMessage
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from langchain.chat_models import init_chat_model

load_dotenv()

mood = input("Select the mood :")

message=[
    SystemMessage(content=mood)
]


model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.8)

print("Welcome type 0 to exit the application")

while True:

    
    prompt = input("YOU :  ")
    message.append(HumanMessage(content=prompt))
    if(prompt =="0"):
        break

    message.append(prompt)
    response = model.invoke(message)

    message.append(AIMessage(content= response.content))

    print("Bot : ",response.content)
