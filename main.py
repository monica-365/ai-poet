#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI
#load_dotenv()

#
#llm = OpenAI()
#result = llm.predict("hi")

import streamlit as st
st.title('인공지능 시인')
title = st.text_input("시의 주제는 뭔가요?")

if st.button("시 작성 요청하기"):
    #chat_model = ChatOpenAI()
    #result = chat_model.invoke(title+"에 대한 시를 써줘")
    llm = OpenAI()
    result = llm.predict(title+"에 대한 시를 써줘")
    st.write(result.content)

