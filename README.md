# 🎬 IMDB Sentiment Analysis App

This project is a **Machine Learning web application** built with **Streamlit** that predicts the **sentiment (Positive / Negative)** of movie reviews. The model is trained on the **IMDB Movie Reviews dataset** using **Logistic Regression**. This app uses **Natural Language Processing (NLP)** techniques to process text reviews. It is trained with **Logistic Regression** for classification and provides a **simple, interactive UI** built with Streamlit. It can be deployed as a **web application** for easy use.

## 🛠️ Tech Stack
- Python 🐍
- Scikit-learn 🤖
- Streamlit 🎨
- Joblib (Model Serialization)

## Project Structure
├── app.py                    - Streamlit app code  
├── model.pkl                 - Trained Logistic Regression model  
├── vectorizer.pkl            - TF-IDF Vectorizer for text preprocessing  
├── requirements.txt          - Project dependencies  
├── README.md                 - Project documentation  

## How to Run the App
1. Clone the repository: `git clone https://github.com/sonalshinde24/sentiment-analysis-reviews.git` and `cd sentiment-analysis-reviews`  
2. Create a virtual environment (optional but recommended): `python -m venv venv` then `source venv/bin/activate` on Linux/Mac or `venv\Scripts\activate` on Windows  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run the app: `streamlit run app.py`  

## Usage
Enter a movie review in the input box. The model will analyze the text and classify it as **Positive 😀** or **Negative 😞**. Simple, fast, and interactive!  

## Example Predictions
| Review | Prediction |
|--------|------------|
| "The movie was fantastic and full of suspense!" | Positive 😀 |
| "Worst movie ever. Waste of time." | Negative 😞 |

## Developer
**Sonal Shinde**  
[LinkedIn](https://www.linkedin.com/in/sonal-shinde-7aa40b250)  
[GitHub](https://github.com/sonalshinde24)  

## Future Enhancements
Add more ML/DL models (Naive Bayes, LSTMs, Transformers), support multi-language reviews, deploy on **Streamlit Cloud / Heroku / AWS**.  

## Requirements
streamlit, scikit-learn, pandas, numpy, joblib
