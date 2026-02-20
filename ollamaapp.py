import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("Simple AI Chat")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{q}")
])

llm = ChatOllama(model="gemma2:2b")
chain = prompt | llm | StrOutputParser()

q = st.text_input("Ask something:")

if st.button("Send"):
    if q:
        ans = chain.invoke({"q": q})
        st.write(ans)