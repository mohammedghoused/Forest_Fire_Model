from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

#importing ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','wb'))
standard_scaler=pickle.load(open('models/scaler.pkl','wb'))


@app.route("/")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
    