import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request


model = pickle.load(open('winemodel.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():

    inputValue = []
    for i in request.form.values():
        inputValue.append(i)

    feature = []

    for j in request.form.keys():
        feature.append(j)

    inputValue = [np.array(inputValue)]


    data = pd.DataFrame(inputValue, columns=feature)

    x = model.predict(data)
    if x[0] == 0:
        result = "Bad quality wine"
    else:
        result = "Good quality wine"
    return render_template("result.html", result = result)


@app.route('/send', methods=['POST', 'GET'])
def send():
    return render_template('index.html')
    
if __name__ == '__main__':

    app.run(debug=True)


