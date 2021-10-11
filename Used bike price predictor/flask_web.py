from flask import Flask, render_template, request, flash, redirect
import os
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
bikes = pd.read_csv('Cleaned_data.csv')

app.secret_key = os.urandom(24)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))


@app.route('/')
def home():
    brand = sorted(bikes['brand'].unique())
    bikename = sorted(bikes['bike_name'].unique())
    owner = sorted(bikes['owner'].unique())
    age = sorted(bikes['age'].unique())
    power = sorted(bikes['power'].unique())
    return render_template('home.html', brand=brand, bikename=bikename,
                           owner=owner, age=age, power=power)


@app.route('/predict', methods=['POST'])
def predict():
    bikename = request.form.get('bikename')
    brand = request.form.get('brand')
    kms_driven = float(request.form.get('kms_driven'))
    age = float(request.form.get('age'))
    power = float(request.form.get('power'))
    owner = request.form.get('owner')
    print(kms_driven)
    prediction = model.predict(pd.DataFrame([[bikename, kms_driven, owner, age, power, brand]], columns=[
                               'bike_name', 'kms_driven', 'owner', 'age', 'power', 'brand']))
    print(prediction)
    prediction = str(np.round(prediction[0], 2))
    return prediction


if __name__ == "__main__":
    app.run(debug=True)
