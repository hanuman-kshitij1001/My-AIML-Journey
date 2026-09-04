import os

folders = [
    "36_simple_imputer_numerical",
    "37_simple_imputer_categorical",
    "38_missing_indicator_random_sample_imputation",
    "39_knn_imputer",
    "40_iterative_imputer_mice",
    "41_what_are_outliers",
    "42_outlier_zscore",
    "43_outlier_iqr",
    "44_outlier_percentile_winsorization",
    "45_feature_construction_splitting",
    "46_curse_of_dimensionality",
    "47_pca_part1_geometric_intuition"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("All folders created successfully!")