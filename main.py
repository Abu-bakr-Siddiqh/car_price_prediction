from flask import *
import pickle
import numpy as np
import pandas as pd
import sklearn
import re
import random
from random import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,6)
    loaded_model = pickle.load(open("car_price_mdl.pkl", "rb"))
    car_price = loaded_model.predict(to_predict)
    return car_price[0]


@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==6):
            car_price_pred = ValuePredictor(to_predict_list)
    car_price_pred = round(car_price_pred,3)
    return(render_template('index.html', prediction = "You can sell the car for {}".format(car_price_pred)))

if __name__ == "__main__":
    app.run(debug=True)