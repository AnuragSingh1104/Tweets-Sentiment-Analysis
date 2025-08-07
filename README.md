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



*(You can add screenshots or GIFs here)*


1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/AnuragSingh1104/Tweets-Sentiment-Analysis.git
cd Tweets-Sentiment-Analysis
2. Create and Activate Virtual Environment (Optional but Recommended)
bash
Copy
Edit
# Using venv
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
# Or if not in the requirements.txt already
pip install streamlit
▶️ How to Use
🚀 Run the App
bash
Copy
Edit
streamlit run app.py
This command will start a local Streamlit server and open the app in your default browser.

🧪 Interact with the App
Single Tweet Mode:
Paste or type a tweet in the text box to analyze its sentiment.

Batch Mode (CSV Upload):
Upload a .csv file containing tweets in one column. The app will process all tweets and display results, including:

Sentiment table

Bar and pie chart distribution

Word clouds per sentiment

Top keywords per category

🧰 Technologies Used
Python 3 – Core programming language

Streamlit – Interactive web application framework

NLTK VADER – Lexicon-based sentiment analysis engine

Pandas – Data manipulation and CSV handling

Matplotlib / Seaborn – Data visualization

NumPy – Numerical operations

re – Regular expressions for text cleaning

📁 Project Structure
graphql
Copy
Edit
/ (root)
├── app.py                  # Main Streamlit app script
├── main.py                 # Model prediction and orchestration
├── src/
│   ├── text_clean.py       # Preprocessing and cleaning functions
│   └── prediction_visualization.py  # Sentiment scoring & plotting
├── notebook/
│   └── sentiment analysis.ipynb     # Data exploration & experiments
├── twitter_validation.csv  # Sample CSV for testing
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Optional: UV/Poetry support
└── README.md               # This documentation
📈 Future Enhancements
Integrate live tweet scraping from Twitter API

Improve model with transformer-based sentiment models (e.g., BERT)

Deploy on Streamlit Cloud or Hugging Face Spaces

🤝 Contributing
Contributions are welcome!
If you find bugs or want to suggest features, feel free to open an issue or submit a pull request.

