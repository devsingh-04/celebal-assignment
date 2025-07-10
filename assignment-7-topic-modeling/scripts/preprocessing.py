import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Download NLTK resources (only once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# 🧹 Clean and lemmatize one text sample
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# 🧼 Preprocess the whole DataFrame
def preprocess_dataframe(df, text_column='text'):
    print("🔧 Preprocessing text data...")
    df['clean_text'] = df[text_column].apply(clean_text)
    return df

# 🔠 TF-IDF for KMeans
def get_tfidf_matrix(texts, max_features=1000):
    print("📊 Creating TF-IDF matrix...")
    tfidf = TfidfVectorizer(max_features=max_features)
    X = tfidf.fit_transform(texts)
    return X, tfidf

# 📚 CountVectorizer for LDA
def get_count_matrix(texts, max_features=1000):
    print("📚 Creating CountVectorizer matrix...")
    count_vec = CountVectorizer(max_features=max_features)
    X = count_vec.fit_transform(texts)
    return X, count_vec
