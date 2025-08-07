# 🐦 Tweets Sentiment Analysis

This project analyzes the sentiment of tweets by classifying each tweet as **positive**, **negative**, or **neutral**. It leverages **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, a rule-based model specifically designed for analyzing sentiments in social media texts.

The core is a **web app built with Streamlit**, allowing users to input a single tweet or upload a CSV of tweets for batch analysis. The app visualizes sentiment scores through insightful charts and word clouds.

---

## 🔑 Key Features

- ✅ **Single & Batch Analysis**  
  Analyze one tweet instantly or upload a CSV file for bulk sentiment analysis.

- 🔍 **VADER Sentiment Scoring**  
  Uses NLTK’s VADER lexicon to calculate sentiment polarity (positive/negative/neutral).

- 📊 **Interactive Visualizations**  
  Displays sentiment distribution using bar plots, pie charts, word clouds, and top words.

- 🖥️ **Streamlit Web App**  
  No web development skills needed — just run the Python script to launch the app.

---



# Create environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

# Or install individually
pip install streamlit pandas numpy matplotlib seaborn nltk
pip install -r requirements.txt

# Or install individually
pip install streamlit pandas numpy matplotlib seaborn nltk


🤝 Contributing
Contributions are welcome!
If you find bugs or want to suggest features, feel free to open an issue or submit a pull request.


