import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

folders = {
    25: "Feature_Scaling_Normalization",
    26: "Encoding_Categorical_Data",
    27: "One_Hot_Encoding",
    28: "Column_Transformer",
    29: "Machine_Learning_Pipelines",
    30: "Function_Transformer",
    31: "Power_Transformer",
    32: "Binning_and_Binarization",
    33: "Handling_Mixed_Variables",
    34: "Handling_Date_and_Time_Variables",
    35: "Handling_Missing_Data_Part1",
}

for num, topic in folders.items():
    folder_name = f"{num}_{topic}"
    folder_path = os.path.join(BASE_DIR, folder_name)

    os.makedirs(folder_path, exist_ok=True)
    print(f"✅ Folder bana: {folder_name}")

print("\n🎉 Sab folders ban gaye!")