import streamlit as st
st.write("<h1>Presentation of the Team </h1>", unsafe_allow_html=True)
st.write("<h2>1173 DataScience Batch - Casablanca</h2>", unsafe_allow_html=True)


col1,col2,col3=st.columns(3)
with col1:
    st.image("images/souad.jpg",width=200)
    st.write("SOUAD the Techwoman \U0001F44B ")
    st.image("images/Rania.jpg",width=200)
    st.write("RANIA The future engineer \U0001F44B")
with col2:
    st.image("images/ahmed.jpg",width=200)
    st.write("AHMAD the Sous-Chef \U0001F44B")
    st.image("images/salma.jpg",width=200)
    st.write("SALMA The IT project Manager \U0001F44B")
with col3:
    st.image("images/yassir.jpg",width=200)
    st.write("YASSIR The entrepreneur \U0001F44B")
    st.image("images/adnane.jpg",width=200)
    st.write("ADNANE The geek \U0001F44B")

CSS = """
h1 {
    color: grey;
}
.stApp {
    background-image: url(https://img.freepik.com/vecteurs-libre/fond-minimal-geometrique-bleu_53876-99573.jpg?w=1800&t=st=1692908352~exp=1692908952~hmac=ff6ee87e06e2b22f236d8a073571eb0cf84914e31af49b704d3bf54c3b43c8e0);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
