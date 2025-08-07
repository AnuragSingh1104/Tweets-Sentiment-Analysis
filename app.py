import streamlit as st
import pandas as pd
import os
from src.text_clean import clean_tweets, clean_text
from src.prediction_visualization import prediction, plot_bar_pie, plot_wordclouds, plot_top_words
from src.prediction_visualization import vader_predict_label

# ---- Page Setup ---- #
st.set_page_config(
    page_title="Twitter Sentiment Analyzer",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- Custom Styles ---- #
st.markdown("""
    <style>
        h1, h4, p {
            font-family: 'Segoe UI', sans-serif;
        }
        .centered {
            text-align: center;
        }
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        .stDownloadButton>button {
            background-color: #2d7d9a;
            color: white;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Header ---- #
st.markdown("""
<h1 style='color:#4B8BBE; font-weight:700;' class='centered'>📊 Twitter Sentiment Analyzer</h1>
<p style='font-size:17px;'>Choose between analyzing a single tweet or uploading a dataset.</p>
<hr>
""", unsafe_allow_html=True)

# ---- Mode Selection ---- #
mode = st.sidebar.radio("Choose analysis mode:", ("📁 Upload CSV File", "📝 Enter Single Tweet"))

# ============================ #
#     MODE 1: CSV UPLOAD       #
# ============================ #
if mode == "📁 Upload CSV File":

    save_folder = r"C:\Users\Anurag\Desktop\Twitter Sentiment analysis Ananlysis\data"
    os.makedirs(save_folder, exist_ok=True)

    uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

    if uploaded_file:
        try:
            save_path = os.path.join(save_folder, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            try:
                df = pd.read_csv(save_path, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(save_path, encoding="latin1")

            text_cols = [col for col in df.columns if df[col].dtype == object]
            if not text_cols:
                st.error("⚠️ No text columns detected in the uploaded file.")
            else:
                default_cols = [
                    col for col in text_cols
                    if any(keyword in col.lower() for keyword in ['tweet', 'text', 'content', 'message', 'status'])
                ]
                default_col = default_cols[0] if default_cols else text_cols[0]

                with st.sidebar:
                    st.header("✏️ Text Column Selection")
                    tweet_col = st.selectbox(
                        "Select the tweet column:",
                        options=text_cols,
                        index=text_cols.index(default_col)
                    )
                    st.caption("Selected column will be used for analysis.")

                st.markdown(f"<h4 style='color:#4B8BBE;'>🔍 Preview: <code>{tweet_col}</code></h4>", unsafe_allow_html=True)
                st.dataframe(df[tweet_col].head(10), use_container_width=True)

                st.info("✅ Column selected! Now you can clean and analyze sentiment.")

                cleaned_df = clean_tweets(df, tweet_col)
                df['clean_text'] = cleaned_df['clean_text']

                if "predicted_df" not in st.session_state:
                    st.session_state['predicted_df'] = None

                if st.button("📈 Predict Sentiment"):
                    with st.spinner("Analyzing sentiment..."):
                        st.session_state['predicted_df'] = prediction(df)
                    st.success("✅ Sentiment prediction completed!")

                if st.session_state['predicted_df'] is not None:
                    predicted_df = st.session_state['predicted_df']

                    st.markdown("### 🧾 Sentiment Prediction Table")
                    st.dataframe(predicted_df[['clean_text', 'predicted_sentiment']].head(10), use_container_width=True)

                    st.download_button(
                        label="📥 Download CSV Results",
                        data=predicted_df.to_csv(index=False),
                        file_name="predicted_sentiments.csv",
                        mime="text/csv"
                    )

                    st.markdown("---")
                    st.header("📊 Sentiment Visualizations")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("#### 📋 Sentiment Count & Proportion")
                        fig_bar_pie = plot_bar_pie(predicted_df)
                        st.pyplot(fig_bar_pie)

                    with col2:
                        st.markdown("#### ☁️ Word Clouds by Sentiment")
                        fig_wordclouds = plot_wordclouds(predicted_df)
                        st.pyplot(fig_wordclouds)

                    st.markdown("#### 🔠 Top Words in Each Sentiment")
                    fig_top_words = plot_top_words(predicted_df, n=10)
                    st.pyplot(fig_top_words)

        except Exception as e:
            st.error(f"❌ Failed to process the file: {e}")
    else:
        st.info("📌 Upload a CSV file to get started.")


# MODE 2: SINGLE TWEET      

elif mode == "📝 Enter Single Tweet":
    st.subheader("🔍 Analyze a Single Tweet")
    user_tweet = st.text_area("Enter a tweet to analyze sentiment:")

    if st.button("📈 Predict Sentiment"):
        if user_tweet.strip() == "":
            st.warning("⚠️ Please enter a tweet before analyzing.")
        else:
            cleaned = clean_text(user_tweet)
            sentiment = vader_predict_label(cleaned)
            st.success(f"✅ **Predicted Sentiment:** `{sentiment}`")
