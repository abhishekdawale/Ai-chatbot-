import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("🦉 Almost Everything")
input_text = st.text_input("Ask anything ...")

prompt = ChatPromptTemplate.from_messages(
    [("system","You are helpful AI assistasnt.Please respond to the question asked."),
       ("user", "Question:{question}")])
       
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
        response = chain.invoke({"question": input_text})
        st.write("🦉Answer:", response)
        #streamlit run chatbot.py