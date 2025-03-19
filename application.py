from flask import Flask,render_template,request
import pickle
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
application =Flask(__name__)
try:
    with open("model_svc.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler2.pkl", "rb") as f:
        scaler = pickle.load(f)
    print("Both model and scaler loaded successfully!")
except Exception as e:
    print("Error loading files:", e)
app = application
scaler1 = joblib.load("scaler2.pkl")
model = pickle.load(open("model_2.pkl","rb"))

@app.route("/")
def welcome():
    return render_template('index.html')
@app.route("/Classification",methods=['GET','POST'])
def classification():
    if(request.method=='POST'):
        temperature = float(request.form.get('temperature'))
        humidity = float(request.form.get('humidity'))
        wind_speed = float(request.form.get('wind_speed'))
        cloud_cover = float(request.form.get('cloud_cover'))
        pressure = float(request.form.get('pressure'))
        new_data = [[temperature,humidity,wind_speed,cloud_cover,pressure]]
        new_scaled = scaler.transform(new_data).astype(np.float64)
        result = model.predict(new_scaled)
        temp = result[0]
        if(temp==1):
            result1="Rain"
        else:
            result1="No Rain"    
        return render_template('result.html',prediction=result1) 
    else:
        return render_template('form.html') 
if(__name__=='__main__'):
    application.run()
