import streamlit as st
import pandas as pd
import numpy as np
from src import cal_height, cal_age, cal_education, cal_mbti
st.title('Count Me, Maybe?')

population = 51751065

st.session_state.sex = '<none>'
st.session_state.age = None
st.session_state.height = None
st.session_state.education = None
st.session_state.mbtis = []
template = "I am looking for a {sex}."

### 성별
st.session_state.sex = st.radio(
    "Im looking for a:",
    ["boyfriend 👨🏻", "girlfriend 👩🏻"],
)

# annotated_text(
#     "You have selected", (st.session_state.sex ,'' ,"#afa"), "."
# )

### 나이
age = st.slider("Age", 0.0, 100.0, (25.0, 75.0))
if age[0] < 20:
    st.text('whoops, you are looking for underagers..?')
st.session_state.age = age

### 키
height = st.slider("Height", 140.0, 200.0, (166.0, 188.0))
st.session_state.height = height

### 학략
st.session_state.education = st.selectbox(
    "Whats your desired level of education?",
    ("고졸 이상", "대학 이상", "인서울 4년제 이상",
     "서연고서성한중경외시", "서연고서성한", "서연고", "연대 이상"),
    placeholder="연대 이상",
)

### MBTI

st.session_state.mbtis= st.multiselect(
    "What are your preferred MBTIs?",
    ['INFP', 'ENFP', 'ESFJ', 'ISFJ', 'ISFP', 'ESFP', 'INTP', 'INFJ', 'ENFJ', 'ENTP', 'ESTJ', 'ISTJ', 'INTJ', 'ISTP', 'ESTP', 'ENTJ']
)

print(st.session_state.mbtis)
prob = cal_age(st.session_state.age[0],st.session_state.age[1])
# st.text(prob)
prob *= cal_height(st.session_state.sex,st.session_state.height[0],st.session_state.height[1])
prob *= cal_education(st.session_state.education)
prob *= cal_mbti(st.session_state.mbtis)
prob *= 0.5
st.text(f"So you are looking for {prob*100:.5f}% of the total population. \nThat will be {prob*population:.0f} people")