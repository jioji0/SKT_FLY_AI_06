import streamlit as st

st.header("GPT Demo")

st.write("당신이 좋아하는 동물은은?")
name = st.text_input("동물의 이름","강아지")

if(name):
    st.write("유모차만 타고, 성질 더러운 말티즈 vs 산책 5시간 해줘야하는 보더콜리")
    wife = st.text_input("선택한 강아지의 종","말티즈")

    button_click= st.button("결과보기")
    if button_click:
        if(wife == "말티즈"):
            st.write("정신적으로 힘들어도 몸이 편한 길을 선택하셨네요")
        else:
            st.write("몸은 힘들어도 행복한 길을 선택하셨네요")
        

data = [10, 20, 30]

st.write("Bar Chart")
st.bar_chart(data)
