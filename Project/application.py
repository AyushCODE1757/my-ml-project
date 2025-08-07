from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from statsmodels.api import OLS
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import pickle
application=Flask(__name__)
app=application
ridge_model=pickle.load(open("models/ridge.pkl","rb"))
stand_scaler=pickle.load(open("models/scaler.pkl","rb"))
@app.route("/")

def index():
    return render_template("index.html")

@app.route('/predictdata',methods=['GET','POST'])

def predict_data():
    if request.method=='POST':
        tempt = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes_str = request.form.get("Classes")
        Region_str = request.form.get("Region")
        Classes = 1.0 if Classes_str.lower() == 'fire' else 0
        Region = 0 if Region_str.lower() == 'bejaia' else 1.0
        new_scaled_data = stand_scaler.transform([[tempt, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_scaled_data)
        return render_template("home.html",results=result[0])
    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)