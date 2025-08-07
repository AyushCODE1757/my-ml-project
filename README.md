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
  - Fine Fuel Moisture Code
  - Duff Moisture Code
  - Initial Spread index
- Ridge Regression model for prediction of **Fire Weather Index (FWI)**
- Preprocessing includes feature engineering & one-hot encoding

---

## 🧠 Tech Stack

- Python 3.x
- Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- Ridge Regression (from `sklearn.linear_model`)

---

## 📁 Dataset Source

Algerian Forest Fire Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset+)

---

## ⚙️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
   ```
2.(Optional)Create a Virtual Environment:-
  ```bash
  python -m venv venv
  ```
  Activate it
   
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask App:  
   ```bash
   python application.py
   ```
   🛜BY default, the app runs on
   http://localhost:5000
5. Open in browser
  Visit http://127.0.0.1:5000/predictdata
---

## 📷 Sample Input & Output

**Input:**
- Temperature: 29°C
- RH: 57%
- WS: 18 km/h
- Rain: 0 mm
- Region: Sidi-Bel Abbes
- FFMC:-65.67
- DMC-3.4
- ISI-1.3
- Classes:- Fire

**Output:**
- Predicted FWI: `0.7754016798136201 (moderate fire danger)

---

## 📌 Educational Purpose

> This project was created as part of an educational tutorial led by **Krish Naik**. It closely follows the model structure and methodology taught in the original video.

---

## ⚠️ Disclaimer

> This project is created purely for **educational purposes** as part of a tutorial by **Krish Naik**.  
> The codebase and dataset usage closely follow the original video content.  
> **All credits** for the model structure and preprocessing steps go to the original author.  
> **No commercial use intended.**
