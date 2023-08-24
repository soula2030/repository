import re
import streamlit as st
import pickle
import string
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from PIL import Image
import nltk
nltk.download('punkt')
nltk.download('wordnet')



def preprocess_data(text):
    text=text.strip()
    text=text.lower()
    cleaned_text = re.sub(r'\d+', '', text)
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = cleaned_text.translate(translator)
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text_without_punctuation)
    verb_lemmatized = [
             WordNetLemmatizer().lemmatize(word, pos="v")
             for word in tokens
         ]
    noun_lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos="n")
            for word in verb_lemmatized
         ]
    text_clean = [' '.join(noun_lemmatized)]
    return  text_clean

def load_preprocessor():
    with open("vectorizer.pkl", "rb") as model_file:
        vectorizer= pickle.load(model_file)
    return vectorizer

def load_model():
    with open("basicmodel.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    return model

def predict(model, text):
    preprocessed_text = preprocess_data(text)
    Predictions= model.predict(preprocessed_text)
    return Predictions

st.write("<h1>👋 I'm the Text to Market wizard 🧙‍♂️.</h1>", unsafe_allow_html=True)
with st.form("input_form"):
    st.write("<h3>Enter your news and wait for the magic ✨</h3>", unsafe_allow_html=True)
    input_text = st.text_area("", height=150)
    if st.form_submit_button("Predict"):
        if input_text:
            loaded_model = load_model()
            vectorizer = load_preprocessor()
            dataCleaned = preprocess_data(input_text)
            dataPreprocessed = vectorizer.transform(dataCleaned)
            prediction = loaded_model.predict(dataPreprocessed)
            if prediction == 0:
                image_array = np.random.randint(0, 5, (5, 5, 3), dtype=np.uint8)
                image = Image.fromarray(image_array)
                st.image("images/image (2).png", width=150)
                st.write("<h3>The stock market is skydiving without a parachute 🪂</h3>", unsafe_allow_html=True)
            else:
                st.balloons()
                image_array = np.random.randint(0, 5, (5, 5, 3), dtype=np.uint8)
                image = Image.fromarray(image_array)
                st.image("images/image (3).png", width=150)
                st.write("<h3>The stock market's prediction is shooting for the stars 🚀</h3>", unsafe_allow_html=True)

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
