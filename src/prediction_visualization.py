import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

import nltk
from nltk.corpus import stopwords

from src.text_clean import clean_tweets




analyzer = SentimentIntensityAnalyzer()

def vader_predict_label(text: str,) -> str:
    """
    Return VADER sentiment label for given text.
    """

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
    

def prediction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply VADER sentiment analysis on the DataFrame.
    """
    if 'clean_text' not in df.columns:
        raise ValueError("DataFrame must have a 'clean_text' column. Run clean_tweets() first.")
        
    df['predicted_sentiment'] = df['clean_text'].apply(vader_predict_label)

    return df



stop_words = set(stopwords.words('english'))



sns.set_style("whitegrid")


def plot_bar_pie(df):
    counts = df['predicted_sentiment'].value_counts().reindex(['Positive','Neutral','Negative'], fill_value=0)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Bar plot
    sns.barplot(x=counts.index, y=counts.values, palette=['#2ca02c','#7f7f7f','#d62728'], ax=axes[0])
    axes[0].set_title("Sentiment Counts")
    axes[0].set_xlabel("Sentiment")
    axes[0].set_ylabel("Number of Tweets")

    # Pie chart
    axes[1].pie(counts.values, labels=counts.index, autopct='%1.1f%%', colors=['#2ca02c','#7f7f7f','#d62728'])
    axes[1].set_title("Sentiment Proportions")

    plt.tight_layout()

    return fig

def plot_wordclouds(df):
    sentiments = ['Positive','Neutral','Negative']
    fig, axes = plt.subplots(1, 3, figsize=(18,6))
    for ax, sentiment in zip(axes, sentiments):
        text = " ".join(df[df['predicted_sentiment'] == sentiment]['clean_text'])
        if text.strip():
            wc = WordCloud(width=400, height=400, background_color='white').generate(text)
            ax.imshow(wc, interpolation='bilinear')
            ax.axis('off')
            ax.set_title(f"{sentiment} Word Cloud")
        else:
            ax.set_title(f"No {sentiment} tweets to display word cloud")
            ax.axis('off')
    plt.tight_layout()

    return fig

def plot_top_words(df, n=10):
    sentiments = ['Positive', 'Neutral', 'Negative']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for ax, sentiment in zip(axes, sentiments):
        words = " ".join(df[df['predicted_sentiment'] == sentiment]['clean_text']).split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        common = Counter(filtered_words).most_common(n)

        if common:
            top_words, counts = zip(*common)
            sns.barplot(x=list(counts), y=list(top_words), palette='viridis', ax=ax)
            ax.set_title(f"Top {n} Words in {sentiment} Tweets")
            ax.set_xlabel("Count")
        else:
            ax.set_title(f"No words in {sentiment} Tweets after removing stopwords")
            ax.axis('off')

    plt.tight_layout()

    return fig


