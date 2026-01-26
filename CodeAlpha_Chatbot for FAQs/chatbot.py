import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 FAQ Chatbot")

faqs = {
    "What is AI?": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that learns from data.",
    "What is Deep Learning?": "Deep Learning uses neural networks with multiple layers.",
    "What is Python?": "Python is a popular programming language used in AI and ML.",
    "What is Streamlit?": "Streamlit is a Python framework for building web applications easily."
}

questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

user_question = st.text_input("Ask your question:")

if user_question:
    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, question_vectors)
    index = similarity.argmax()

    if similarity[0][index] > 0.3:
        st.success(answers[index])
    else:
        st.warning("Sorry, I don't understand your question.")
