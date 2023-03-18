import pickle
import flask
from flask import Flask, request, app, jsonify
from flask import Response
from flask_cors import CORS
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if(request.method=='POST'):
        f1 = int(request.json['Frequency'])
        f2 = float(request.json['Angle_of_attack'])
        f3 = float(request.json['Chord_length'])
        f4 = float(request.json['F-S_velocity'])
        f5 = float(request.json['Suction_side'])

        result = 0
        testing_set = np.array([f1,f2,f3,f4,f5])
        pickled_model = pickle.load(open('model.pkl','rb'))
        result = pickled_model.predict(testing_set.reshape(1,-1))

        return jsonify(f"The pressure level is {result} decibels.")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)


























