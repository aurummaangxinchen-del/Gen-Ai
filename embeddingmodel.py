from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv,find_dotenv

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from langchain.chat_models import init_chat_model

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text = ['Hello my name is aurum ',"How was attack on titan"]

vector = embeddings.embed_documents(text)

print(vector)