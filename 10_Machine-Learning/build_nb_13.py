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





import json
import os

# Yaha apni files/folders ke naam daal do (bina .ipynb extension ke)
names = [
    "",
    
]

# Minimal empty notebook structure
empty_notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

for name in names:
    # 1. folder banao (agar pehle se nahi hai)
    os.makedirs(name, exist_ok=True)

    # 2. usi naam se andar .ipynb file banao
    filepath = os.path.join(name, f"{name}.ipynb")

    if os.path.exists(filepath):
        print(f"Already exists, skipping: {filepath}")
        continue

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(empty_notebook, f, indent=1)
    print(f"Created: {filepath}")

print("\nDone! Total folders/files:", len(names))