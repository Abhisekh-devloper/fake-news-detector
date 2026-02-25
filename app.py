from flask import Flask, render_template, request
import pickle
import nltk
import re
from nltk.corpus import stopwords
from news_fetcher import get_google_news

app = Flask(__name__)

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def predict_news(news):
    cleaned = clean_text(news)
    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(vector)[0]
        confidence = max(proba) * 100
    else:
        confidence = 95.0

    label = "Real News ✅" if prediction == 1 else "Fake News ❌"
    return label, round(confidence, 2)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None

    if request.method == "POST":
        news = request.form["news"]
        result, confidence = predict_news(news)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence
    )

@app.route("/search", methods=["POST"])
def search_news():
    topic = request.form["topic"]
    articles = get_google_news(topic)

    analyzed_articles = []

    for art in articles:
        label, confidence = predict_news(art["title"])
        analyzed_articles.append({
            "title": art["title"],
            "link": art["link"],
            "label": label,
            "confidence": confidence
        })

    return render_template("index.html", articles=analyzed_articles)

if __name__ == "__main__":
    app.run(debug=True)

