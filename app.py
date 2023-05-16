import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a_n=a*r^{n-1}+a*r^{n-2}+a*r^{n-3}+\dots+a*r^0''')

st.subheader("Image :")
st.image("kid.jpg")
st.subheader("Audio :")
st.audio("Audio.mp3")
st.subheader("Video :")
st.video("video.mp4")

st.number_input('Pick a number', 0, 10)
st.text_input('Email adress')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favourite color')
