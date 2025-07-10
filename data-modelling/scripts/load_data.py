import pandas as pd
from sklearn.datasets import fetch_20newsgroups

def load_and_save_dataset(filepath="data/raw/20_newsgroups.csv"):
    print("🔄 Fetching 20 Newsgroups dataset...")
    newsgroups_data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

    df = pd.DataFrame({
        'text': newsgroups_data.data,
        'target': newsgroups_data.target,
        'target_name': [newsgroups_data.target_names[i] for i in newsgroups_data.target]
    })

    print(f"💾 Saving dataset to: {filepath}")
    df.to_csv(filepath, index=False)
    print("✅ Dataset saved successfully.")
    return df

if __name__ == "__main__":
    load_and_save_dataset()
