import streamlit as st
import joblib
import numpy as np
from PIL import Image

# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="🎬 IMDB Sentiment Analysis",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- LOAD MODEL -----------------
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ----------------- CUSTOM CSS -----------------
st.markdown("""
    <style>
        /* Main background */
        .main {
            background-color: #1e2a38;
            color: #f5f5f5;
        }
        /* Title and subtitle */
        .main-title {
            font-size: 36px;
            color: #FFD700;
            font-weight: bold;
            text-align: center;
        }
        .sub-title {
            font-size: 18px;
            color: #f0f0f0;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Text area */
        textarea {
            background-color: #2c3e50;
            color: #ecf0f1;
            font-size: 16px;
            border-radius: 8px;
        }
        /* Button */
        .stButton>button {
            background-color: #1ABC9C;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #16A085;
        }
        /* Positive/Negative result */
        .positive {
            background-color: #2ECC71;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
        }
        .negative {
            background-color: #E74C3C;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
        }
        /* Sidebar */
        .css-1d391kg {  /* Streamlit sidebar container class */
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        .sidebar .sidebar-content {
            color: #f5f5f5;
        }
        .sidebar .sidebar-content a {
            color: #1ABC9C;
        }
    </style>
""", unsafe_allow_html=True)

# logo = Image.open("happy_sad.png")  # Replace with your file path

# # Display the logo in the sidebar
# st.sidebar.image(logo, width=200)  # Adjust width as needed



# ----------------- SIDEBAR -----------------
st.sidebar.markdown("""
<div style="background-color:#0E1117;padding:20px;border-radius:10px;">
    <h2 style="color:#FFD700;text-align:center;">🎬 Movie Sentiment Analyzer</h2>
    <p style="color:#FFFFFF;text-align:center;font-size:14px;">
    Predict the sentiment of IMDB movie reviews using Machine Learning!
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# About App Card
st.sidebar.markdown("""
<div style="background-color:#1F2937;padding:15px;margin-bottom:10px;border-radius:10px;">
    <h4 style="color:#00FFFF;">📖 About this App</h4>
    <p style="color:#D1D5DB;font-size:14px;">
    This app uses <b>Machine Learning (Logistic Regression)</b> trained on <b>IMDB reviews</b> 
    to predict the <b>sentiment</b> of a movie review.
    </p>
</div>
""", unsafe_allow_html=True)

# Built With Card
st.sidebar.markdown("""
<div style="background-color:#1F2937;padding:15px;margin-bottom:10px;border-radius:10px;">
    <h4 style="color:#00FFFF;">🛠 Built With</h4>
    <ul style="color:#D1D5DB;font-size:14px;">
        <li>Python 🐍</li>
        <li>Scikit-learn 🤖</li>
        <li>Streamlit 🎨</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Developer Card
st.sidebar.markdown("""
<div style="background-color:#1F2937;padding:15px;margin-bottom:10px;border-radius:10px;">
    <h4 style="color:#00FFFF;">👨‍💻 Developer</h4>
    <p style="color:#D1D5DB;font-size:14px;">
        Sonal Shinde<br>
        <a href="https://www.linkedin.com/in/sonal-shinde-7aa40b250" target="_blank" style="color:#FFD700;">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Source Code Card
st.sidebar.markdown("""
<div style="background-color:#1F2937;padding:15px;margin-bottom:10px;border-radius:10px;">
    <h4 style="color:#00FFFF;">📂 Source Code</h4>
    <p style="color:#D1D5DB;font-size:14px;">
        <a href="https://github.com/sonalshinde24/sentiment-analysis-reviews" target="_blank" style="color:#FFD700;">GitHub Repository</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Optional: Add a small IMDB logo at the bottom
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg", use_column_width=True)



# # ----------------- SIDEBAR -----------------
# st.sidebar.markdown("<h2 style='text-align:center;'>🎬 Movie Sentiment Analyzer</h2>", unsafe_allow_html=True)

# st.sidebar.markdown("---")

# # About App
# st.sidebar.markdown("## 📖 About this App")
# st.sidebar.info(
#     """
# This app uses **Machine Learning (Logistic Regression)**  
# trained on **IMDB movie reviews** to predict the **sentiment** of a review.
# """
# )

# # Built With
# st.sidebar.markdown("## 🛠 Built With")
# st.sidebar.markdown(
#     """
# - **Python 🐍**
# - **Scikit-learn 🤖**
# - **Streamlit 🎨**
# """
# )
# st.sidebar.markdown("---")

# # Developer
# st.sidebar.markdown("## 👨‍💻 Developer")
# st.sidebar.markdown(
#     """
# **Sonal Shinde**  
# [LinkedIn](https://www.linkedin.com/in/sonal-shinde-7aa40b250)  
# """
# )
# st.sidebar.markdown("---")

# # Source Code
# st.sidebar.markdown("## 📂 Source Code")
# st.sidebar.markdown("[GitHub Repository](https://github.com/sonalshinde24/sentiment-analysis-reviews)")
# st.sidebar.markdown("---")


# ----------------- HEADER -----------------
st.markdown("<div class='main-title'>🎬 IMDB Movie Review Sentiment Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Enter a movie review below and let AI tell you the sentiment 🚀</div>", unsafe_allow_html=True)

# ----------------- MAIN CONTENT -----------------
review = st.text_area("✍️ Write your movie review here...", height=150)

if st.button("🔍 Analyze Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review first.")
    else:
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)[0]
        probability = np.max(model.predict_proba(review_vector))

        if prediction == 1:
            st.markdown(f"<div class='positive'>✅ Positive Review <br> Confidence: {probability:.2%}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='negative'>❌ Negative Review <br> Confidence: {probability:.2%}</div>", unsafe_allow_html=True)

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit | © 2025</p>", unsafe_allow_html=True)
