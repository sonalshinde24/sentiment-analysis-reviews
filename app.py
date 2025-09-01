import streamlit as st
import joblib
import re

# ✅ Page config (must be the first Streamlit command)
st.set_page_config(page_title="IMDB Sentiment Analysis", page_icon="🎬", layout="centered")

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", " ", text)  # remove HTML tags
    text = re.sub(r"[^a-zA-Z]", " ", text)  # keep only letters
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text

# App UI
st.title("🎬 IMDB Movie Review Sentiment Analysis")
st.write("This app predicts whether a movie review is **Positive** or **Negative**.")

# Text input
review = st.text_area("Enter your movie review here:")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review before analyzing.")
    else:
        # Preprocess
        clean_review = preprocess_text(review)
        vectorized_review = vectorizer.transform([clean_review])

        # Predict
        prediction = model.predict(vectorized_review)[0]
        probability = model.predict_proba(vectorized_review).max()

        # Display result
        if prediction == 1:
            st.success(f"✅ Positive Review (Confidence: {probability:.2f})")
        else:
            st.error(f"❌ Negative Review (Confidence: {probability:.2f})")
