import streamlit as st

def main():
    st.title('식용버섯일까 독버섯일까?')
    st.info('버섯 사진을 업로드하면, 식용버섯인지 독버섯인지 알려드립나다.')
    image = st.file_uploader('이미지 파일을 업로드하세요.', type=['jpg','png','jpeg']) 

