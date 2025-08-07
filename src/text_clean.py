import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords


top_words = set(stopwords.words('english'))

def clean_text(text):
    if pd.isna(text):
        return ""

    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # Remove mentions (@username) and hashtags (#topic)
    text = re.sub(r'@\w+|#\w+', '', text)

    # Remove punctuation
    text = re.sub(r'[^a-z\s\:\;\-\!\?\'\"]', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()


    return text




def clean_tweets(df: pd.DataFrame, text_column: str)->pd.DataFrame:

    """This function cleans the tweets data in the specified column of a DataFrame."""

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df['clean_text'] = df[f'{text_column}'].apply(clean_text)


    return df



    
