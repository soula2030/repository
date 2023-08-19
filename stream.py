import re
import streamlit as st
import pickle
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_data(text):
    text=text.strip()
    text=text.lower()
    cleaned_text = re.sub(r'\d+', '', text)
    text_punctuation = str.maketrans('', '', string.punctuation)
    text_without_punctuation = cleaned_text.translate(text_punctuation)
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
    preprocessed_text = preprocess_data(text)  # Preprocess the text
    Predictions= model.predict(preprocessed_text)
    return Predictions

st.title("text to market")


input_text = st.text_area("Welcome to text to market")




if st.button("Predict Sentiment"):
    loaded_model = load_model()
    vectorizer= load_preprocessor()
    dataCleaned = preprocess_data(input_text)
    dataPreprocessed = vectorizer.transform(dataCleaned)
    prediction = loaded_model.predict(dataPreprocessed)
    st.write("Predicted Sentiment:", prediction )
