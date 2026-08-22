import json

cells = []

def md(text):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": text.splitlines(keepends=True)
    })

def code():
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": []
    })

md("""# Day 13 | End to End Toy Project
Is notebook me hum ek chhota sa Machine Learning project end-to-end banayenge — 
Student ki **IQ aur CGPA** ke aadhar par uska **Placement** predict karna.

**Pipeline Overview:**
1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Selection & Splitting
4. Feature Scaling
5. Model Training & Evaluation
6. Model Deployment
""")

md("""## 1. Data Preprocessing
- Sabse pehle dataset ko import karte hain.
- Jo columns model ke liye zaroori nahi hote (jaise `Unnamed: 0` ya ID columns), unhe drop kar dete hain.
- Model ko feed karne se pehle data ko **clean** karna zaroori hota hai — missing values, unnecessary columns, wrong datatypes sab check kiye jaate hain.
""")
code()

md("""## 2. Exploratory Data Analysis (EDA)
- Matplotlib ka use karke data ko visualize karte hain.
- Ek **scatterplot** banate hain jisme x-axis pe CGPA aur y-axis pe IQ hota hai, color se placement (0/1) dikhaya jata hai.
- Isse pata chalta hai ki dono features (IQ, CGPA) placement ke saath kaisa pattern dikhate hain — kya linearly separable hai ya nahi.
""")
code()

md("""## 3. Feature Selection & Splitting
- Dataset ko do parts me divide karte hain:
  - **Input features (X):** IQ, CGPA
  - **Target variable (y):** Placement
- Fir `train_test_split` ka use karke data ko **training set** aur **testing set** me split karte hain.
- Isse hum model ko train karne ke baad, unseen data pe fairly evaluate kar paate hain.
""")
code()

md("""## 4. Feature Scaling
- IQ aur CGPA alag-alag range me hote hain (jaise IQ 80-140 aur CGPA 0-10).
- Isliye dono features ko ek standard range me laate hain (Standardization/Normalization).
- Isse Logistic Regression jaise algorithms better aur fast converge karte hain.
""")
code()

md("""## 5. Model Training & Evaluation
- **Logistic Regression** model ko training data pe train karte hain.
- Model ki performance ko **accuracy score** se measure karte hain.
- Fir **decision boundary** plot karke visually dekhte hain ki model ne data ko kaise classify kiya hai.
""")
code()

md("""## 6. Model Deployment
- Trained model ko **Pickle** library ke through ek file (`.pkl`) me save/export karte hain.
- Is saved model ko ek **web application** me integrate kiya ja sakta hai.
- Deployment ke liye common platforms: **Heroku, AWS, Google Cloud** discuss kiye gaye hain.
""")
code()

notebook = {
    "cells": cells,
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

with open("13_End_to_End_Toy_Project.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully: 13_End_to_End_Toy_Project.ipynb")