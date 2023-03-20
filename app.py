import pickle
import flask
from flask import Flask, request, app, jsonify, render_template
from flask import Response
from flask_cors import CORS
import numpy as np

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict/postman", methods=['POST'])
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
        

@app.route("/", methods=['POST'])
def predictForm():
    if(request.method=='POST'):
        f1 = int(request.form['Frequency'])
        f2 = float(request.form['Angle_of_attack'])
        f3 = float(request.form['Chord_length'])
        f4 = float(request.form['F-S_velocity'])
        f5 = float(request.form['Suction_side'])

        result = 0
        testing_set = np.array([f1,f2,f3,f4,f5])
        pickled_model = pickle.load(open('model.pkl','rb'))
        result = pickled_model.predict(testing_set.reshape(1,-1))
        return_string = f"Airfoil pressure level is {result} in decibels"

        return render_template("index.html", result = return_string)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)


























