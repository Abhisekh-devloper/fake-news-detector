# 🧠 AI Fake News Detection System

An intelligent web application that detects whether a news article is **Real** or **Fake** using Machine Learning and Natural Language Processing (NLP). The system can also fetch **live news from Google News** and automatically analyze it.

---

## 🚀 Features

✅ Detect fake vs real news from user input
✅ Confidence score with progress bar
✅ Live Google News search and analysis
✅ Dark mode UI
✅ Professional responsive interface
✅ TF-IDF + Passive Aggressive Classifier
✅ Flask web application
✅ Modular project structure

---

## 🧠 Tech Stack

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Flask

**Machine Learning**

* Scikit-learn
* TF-IDF Vectorizer
* Passive Aggressive Classifier
* NLTK

**Data Source**

* Kaggle Fake & True News Dataset
* Google News RSS Feed

---

## 📁 Project Structure

```
fake-news-detector/
│
├── dataset/
├── model/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── news_fetcher.py
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/Abhisekh-developer/fake-news-detector.git
cd fake-news-detector
```

---

### 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 3: Train Model (first time only)

```bash
python train_model.py
```

This will create:

* model/model.pkl
* model/vectorizer.pkl

---

### 🔹 Step 4: Run Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔍 How It Works

1. User enters news text
2. Text preprocessing (NLP cleaning)
3. TF-IDF converts text to vectors
4. ML model predicts Fake or Real
5. Confidence score displayed
6. Optional: Fetch live news from Google RSS

---

## 📊 Model Details

* Algorithm: Passive Aggressive Classifier
* Feature Extraction: TF-IDF
* Text Processing: NLTK
* Accuracy: ~90%+ (depends on dataset)

---

## 🌙 UI Highlights

* Modern gradient design
* Dark mode toggle
* Confidence progress bar
* Live news cards
* Mobile responsive

---

## 🚧 Future Improvements

* BERT based detection
* Full article scraping
* News source credibility scoring
* Multi-language support
* Cloud deployment

---

## 👨‍💻 Author

**Abhisekh Mohanty**
GitHub: https://github.com/Abhisekh-developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
