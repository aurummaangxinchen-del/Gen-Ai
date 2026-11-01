import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
 
load_dotenv()
 
st.set_page_config(page_title="AI Chatbot", page_icon="💬")
 
 
@st.cache_resource
def get_model():
    return init_chat_model("groq:openai/gpt-oss-120b", temperature=0.8)
 
 
model = get_model()
 
st.title("AI Chatbot")
 
# Step 1: pick the mood (becomes the system message)
if "messages" not in st.session_state:
    mood = st.text_input("Select the mood", placeholder="e.g. a friendly pirate")
    if st.button("Start chat") and mood.strip():
        st.session_state.messages = [SystemMessage(content=mood.strip())]
        st.rerun()
    st.stop()
 
# Step 2: chat
for m in st.session_state.messages:
    if isinstance(m, HumanMessage):
        role = "user"
    elif isinstance(m, AIMessage):
        role = "assistant"
    else:
        continue
    with st.chat_message(role):
        st.markdown(m.content)
 
if prompt := st.chat_input("Type your message"):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
 
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
        st.markdown(response.content)
 
    st.session_state.messages.append(AIMessage(content=response.content))