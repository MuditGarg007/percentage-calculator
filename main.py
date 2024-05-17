import streamlit as st
from PIL import Image

st.set_page_config(page_title="Percentage Calculator", page_icon= "📈")

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.header("PERCENTAGE CALCULATOR")
st.subheader("Calculate you percentage")

def calcPercent(L, max_marks):
    percentage = (sum(L)/(len(L) * max_marks))*100
    return percentage

def input_marks(subjects):
    subjects_marks = []
    for i in range(subjects):
        marks = st.number_input("Marks for Subject " + str(i+1), 0)
        subjects_marks.append(marks)
    return subjects_marks

with st.container():
    subjects= st.number_input("Number of subjects: ", 0)
    subjects = int(subjects)
    max_marks = st.number_input("Maximum marks in each subject: ", 0)
    all_marks = input_marks(subjects)
    

with st.container():
    if st.button("Calculate🎉"):
            percentage = calcPercent(all_marks, max_marks)
            st.subheader("Congrats! Your total percentage is: " + str(percentage) + "%")

