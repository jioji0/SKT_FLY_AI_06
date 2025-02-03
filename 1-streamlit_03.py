import openai
import streamlit as st
from dotenv import load_dotenv
import os 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.azure_endpoint = os.getenv("OPENAI_ENDPOINT")

MODEL_NAME = os.getenv("MODEL_NAME")

subject = st.text_input("프로젝트의 주제를 입력하세요 :")
content = st.text_area("프로젝트의 내용을 입력하세요 :")


button_click = st.button("작문")

if(button_click):
    with st.spinner('Wait for it....'):
        response = openai.chat.completions.create(
                        model = MODEL_NAME,
                        temperature = 0.7,
                        messages = [
                            {"role":"system","content":"너는 이제부터 대학교 교수님이야."},
                            {"role":"user","content":"프로젝트트 제목은"+subject},
                            {"role":"user","content":"프로젝트트 내용은"+content},
                            {"role":"user","content":"상상력을 발휘해줘"}
                        ]
                    )


        st.write(response.choices[0].message.content)

        st.success("Done!")