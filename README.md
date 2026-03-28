# 🔍 Duplicate Question Pairs Detector

An end-to-end **Machine Learning** pipeline to identify whether two questions asked on a forum (like Quora) share the same intent. This project transitions from raw text processing to a high-performance classification model.

🚀 **Live Demo:** https://duplicate-question-pairs-aayu.streamlit.app/

---

## 📌 Project Overview
The goal of this project is to predict which pairs of questions have the same meaning. This is a classic **Natural Language Processing (NLP)** task that helps platforms reduce redundancy and improve user experience.

### ✨ Key Features
* **Text Preprocessing:** Automated tokenization, stopword removal, and cleaning.
* **Vectorization:** Bag of Words (`CountVectorizer`) with a optimized 3,000-word vocabulary.
* **Advanced Models:** Comparison of Gradient Boosting frameworks (XGBoost, LightGBM, CatBoost).
* **Interactive UI:** Modern Streamlit dashboard with **real-time confidence scoring**.

---

## 📊 Model Performance
After rigorous testing, **CatBoost** was selected for production due to its stability and high precision.

| Model | Accuracy | Precision (Class 1) | Recall (Class 1) |
| :--- | :--- | :--- | :--- |
| Random Forest | 79% | 0.72 | 0.68 |
| XGBoost | 80% | 0.73 | 0.73 |
| LightGBM | 80% | 0.71 | **0.75** |
| **CatBoost** | **81%** | **0.73** | **0.74** |

> **💡 Insight:** We prioritized **Precision** to minimize "False Positives," ensuring that unique questions are not incorrectly merged, which preserves the user experience.

---

## 🛠️ Tech Stack
* **Core:** Python 3.10+
* **ML Libraries:** Pandas, NumPy, Scikit-Learn, CatBoost, XGBoost, LightGBM
* **NLP:** NLTK (Natural Language Toolkit)
* **Deployment:** Streamlit Cloud
* **Version Control:** Git & GitHub

---

## 📂 Project Structure
* `app.py` - Streamlit frontend logic & custom CSS.
* `helper.py` - Feature engineering & NLTK preprocessing pipelines.
* `model.pkl` - The trained CatBoost classifier.
* `cv.pkl` - Fitted CountVectorizer vocabulary.
* `requirements.txt` - Dependency list for cloud deployment.
* `stopwords.pkl` - Stopwords from the NLTK library


---

## 🚀 Installation & Local Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aayu2417/duplicate-question-pairs.git](https://github.com/aayu2417/duplicate-question-pairs.git)
   cd duplicate-question-pairs

2. **Setup Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt

3. **Launch the app:**
   ```bash
   streamlit run app.py
