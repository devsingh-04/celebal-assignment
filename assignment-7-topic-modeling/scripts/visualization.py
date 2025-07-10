import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.manifold import TSNE
import seaborn as sns
import os

# ✅ Generate WordClouds for LDA topics
def create_wordclouds(topics, output_dir="../output/visualizations/wordclouds"):
    print("☁️ Creating WordClouds...")
    os.makedirs(output_dir, exist_ok=True)

    for i, topic in enumerate(topics):
        wc = WordCloud(width=800, height=400, background_color='white').generate(" ".join(topic))
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Topic {i}", fontsize=16)
        filepath = f"{output_dir}/lda_topic_{i}.png"
        plt.savefig(filepath)
        plt.close()
    print("✅ WordClouds saved.")

# ✅ t-SNE visualization for KMeans clusters
def plot_tsne_clusters(X, labels, output_path="../output/visualizations/kmeans_tsne.png"):
    print("📉 Creating t-SNE cluster plot...")
    tsne = TSNE(n_components=2, perplexity=50, random_state=42)
    X_reduced = tsne.fit_transform(X.toarray())

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=X_reduced[:, 0], y=X_reduced[:, 1], hue=labels, palette="tab10", s=60)
    plt.title("KMeans Clusters (t-SNE Projection)", fontsize=16)
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.legend(title="Cluster")
    plt.savefig(output_path)
    plt.close()
    print(f"✅ t-SNE plot saved to {output_path}")
