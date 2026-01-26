import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text to translate")

source_lang = st.selectbox(
    "Source Language",
    ["auto", "en", "hi", "te", "ta", "fr", "de"]
)

target_lang = st.selectbox(
    "Target Language",
    ["en", "hi", "te", "ta", "fr", "de"]
)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)
        st.success(translated)