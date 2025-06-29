from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_confusion_matrix(y_true, y_pred, model_name, output_path="../output/confusion_matrices"):
    """
    Save a confusion matrix heatmap to the output/confusion_matrices/ directory.
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f'Confusion Matrix - {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

    # Ensure output path exists
    os.makedirs(output_path, exist_ok=True)

    # Save the figure
    file_path = os.path.join(output_path, f"{model_name}_confusion_matrix.png")
    plt.savefig(file_path)
    plt.close()

def generate_classification_report(y_true, y_pred):
    """
    Return classification report as a dictionary.
    """
    return classification_report(y_true, y_pred, output_dict=True)
