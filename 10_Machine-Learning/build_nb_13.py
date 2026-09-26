# import os

# folders = [
#     "36_simple_imputer_numerical",
#     "37_simple_imputer_categorical",
#     "38_missing_indicator_random_sample_imputation",
#     "39_knn_imputer",
#     "40_iterative_imputer_mice",
#     "41_what_are_outliers",
#     "42_outlier_zscore",
#     "43_outlier_iqr",
#     "44_outlier_percentile_winsorization",
#     "45_feature_construction_splitting",
#     "46_curse_of_dimensionality",
#     "47_pca_part1_geometric_intuition"
# ]

# for folder in folders:
#     os.makedirs(folder, exist_ok=True)

# print("All folders created successfully!")





# import json
# import os

# # Yaha apni files/folders ke naam daal do (bina .ipynb extension ke)
# names = [
#     "58_Batch_Gradient_Descent_with_Code_Demo",
#     "59_Stochastic_Gradient_Descent",
#     "60_Mini_Batch_Gradient_Descent",
# ]
# # Minimal empty notebook structure
# empty_notebook = {
#     "cells": [],
#     "metadata": {
#         "kernelspec": {
#             "display_name": "Python 3",
#             "language": "python",
#             "name": "python3"
#         },
#         "language_info": {
#             "name": "python",
#             "version": "3.x"
#         }
#     },
#     "nbformat": 4,
#     "nbformat_minor": 5
# }

# for name in names:
#     # 1. folder banao (agar pehle se nahi hai)
#     os.makedirs(name, exist_ok=True)

#     # 2. usi naam se andar .ipynb file banao
#     filepath = os.path.join(name, f"{name}.ipynb")

#     if os.path.exists(filepath):
#         print(f"Already exists, skipping: {filepath}")
#         continue

#     with open(filepath, "w", encoding="utf-8") as f:
#         json.dump(empty_notebook, f, indent=1)
#     print(f"Created: {filepath}")

# print("\nDone! Total folders/files:", len(names))

from pathlib import Path
import json
import re

# Jahan ye Python code run hoga, wahi folders banenge
BASE_DIR = Path.cwd()

videos = [
    "Polynomial Regression | Machine Learning",

    "Bias Variance Trade-off | Overfitting and Underfitting in Machine Learning",

    "Ridge Regression Part 1 | Geometric Intuition and Code | Regularized Linear Models",

    "Ridge Regression Part 2 | Mathematical Formulation & Code from scratch | Regularized Linear Models",

    "Ridge Regression Part 3 | Gradient Descent | Regularized Linear Models",

    "5 Key Points - Ridge Regression | Part 4 | Regularized Linear Models",

    "Lasso Regression | Intuition and Code Sample | Regularized Linear Models",

    "Why Lasso Regression creates sparsity?",

    "ElasticNet Regression | Intuition and Code Example | Regularized Linear Models",

    "Logistic Regression Part 1 | Perceptron Trick",

    "Logistic Regression Part 2 | Perceptron Trick Code",

    "Logistic Regression Part 3 | Sigmoid Function | 100 Days of ML"
]


def clean_name(name):
    """
    Windows-invalid characters ko replace/remove karta hai.
    """
    name = name.replace("|", "-")
    name = name.replace("?", "")
    name = name.replace(":", "-")
    name = name.replace("*", "")
    name = name.replace('"', "'")
    name = name.replace("<", "(")
    name = name.replace(">", ")")
    name = name.replace("/", "-")
    name = name.replace("\\", "-")

    return name.strip()


for number, title in enumerate(videos, start=61):

    # Clean title for Windows
    clean_title = clean_name(title)

    # Final folder name
    folder_name = f"{number}_{clean_title}"

    # Create folder
    folder_path = BASE_DIR / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    # Same name ka notebook
    notebook_name = f"{folder_name}.ipynb"
    notebook_path = folder_path / notebook_name

    # Basic Jupyter Notebook
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {folder_name}\n",
                    "\n",
                    "## Theory Notes\n",
                    "\n",
                    f"**Topic:** {title}\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    # Create .ipynb
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=4, ensure_ascii=False)

    print(f"✅ Created: {folder_name}")


print("\n🎉 ALL FOLDERS + NOTEBOOKS CREATED SUCCESSFULLY!")
print(f"📂 Location: {BASE_DIR}")