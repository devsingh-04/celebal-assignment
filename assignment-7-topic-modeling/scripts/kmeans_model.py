from sklearn.cluster import KMeans
import numpy as np

# 🔢 Apply KMeans and return cluster labels
def run_kmeans(X, n_clusters=10):
    print(f"🚀 Running KMeans with {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    kmeans.fit(X)
    return kmeans.labels_, kmeans

# 🧠 Extract top keywords for each cluster
def get_top_keywords_per_cluster(tfidf_model, kmeans_model, n_terms=10):
    print("📝 Extracting top keywords per cluster...")
    order_centroids = kmeans_model.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf_model.get_feature_names_out()
    keywords = []

    for i in range(kmeans_model.n_clusters):
        cluster_terms = [terms[ind] for ind in order_centroids[i, :n_terms]]
        keywords.append(cluster_terms)

    return keywords
