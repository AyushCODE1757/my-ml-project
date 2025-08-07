# Forest Fire Danger Prediction using Ridge Regression

This project predicts the **Fire Weather Index (FWI)** using meteorological and spatial features from the **Algerian Forest Fire Dataset**. The model is trained using **Ridge Regression**, a linear regression technique with L2 regularization, to predict fire risk levels.

---

## 🔥 Project Features

- Uses **Algerian Forest Fire Dataset** (UCI Repository)
- Takes user inputs such as:
  - Temperature (°C)
  - RH (Relative Humidity)
  - WS (Wind Speed)
  - Rainfall (mm)
  - Region (Bejaia or Sidi-Bel Abbes)
  - Date (month & day)
- Ridge Regression model for prediction of **Fire Weather Index (FWI)**
- Preprocessing includes feature engineering & one-hot encoding

---

## 🧠 Tech Stack

- Python 3.x
- Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- Ridge Regression (from `sklearn.linear_model`)
- Streamlit (for user interface, if applicable)

---

## 📁 Dataset Source

Algerian Forest Fire Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset+)

---

## ⚙️ How to Run

1. Clone this repository
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application (if Streamlit used):  
   ```bash
   streamlit run app.py
   ```
4. Or, use the notebook to test locally

---

## 📷 Sample Input & Output

**Input:**
- Temperature: 30°C
- RH: 45%
- WS: 20 km/h
- Rain: 0 mm
- Region: Bejaia
- Date: June 15

**Output:**
- Predicted FWI: `18.34` (moderate fire danger)

---

## 📌 Educational Purpose

> This project was created as part of an educational tutorial led by **Krish Naik**. It closely follows the model structure and methodology taught in the original video.

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it for personal or educational use.

---

## ⚠️ Disclaimer

> This project is created purely for **educational purposes** as part of a tutorial by **Krish Naik**.  
> The codebase and dataset usage closely follow the original video content.  
> **All credits** for the model structure and preprocessing steps go to the original author.  
> **No commercial use intended.**