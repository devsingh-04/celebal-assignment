from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# 🧾 Create Document-Term Matrix for LDA
def get_lda_count_matrix(texts, max_features=1000):
    print("📚 Creating CountVectorizer matrix for LDA...")
    vectorizer = CountVectorizer(max_features=max_features, stop_words='english')
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

# 🧠 Run LDA
def run_lda(X, n_topics=10):
    print(f"🧠 Running LDA with {n_topics} topics...")
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)
    return lda

# 📝 Extract Top Words for Each Topic
def get_lda_topics(lda_model, vectorizer, n_top_words=10):
    print("📝 Extracting top words for each topic...")
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        top_features = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        topics.append(top_features)

    return topics
