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
    background-image: url(https://img.freepik.com/free-vector/white-background-with-hexagonal-line-pattern-design_1017-28442.jpg?w=2000&t=st=1692905849~exp=1692906449~hmac=64d1cb5d47b5d4eced08bc18a009895d3971376aca7440d5baf93dd4a7ae410b);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
