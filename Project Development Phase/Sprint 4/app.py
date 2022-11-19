from flask import Flask, render_template,request, jsonify
from flask_cors import CORS
import sklearn
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import phishLogic

app = Flask(__name__)
CORS(app)

model = pickle.load(open("C:/Users/exson/Projects/IBM-Project-43716-1660718978/Project Development Phase/Sprint 3/Phishing_model.pkl","rb"))

@app.route('/')
def predict():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
   
    url = request.form['url']
    checkprediction = phishLogic.main(url)
    print(checkprediction)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="Your are safe!!  This is a Legitimate Website."
        
    else:
        pred="You are on the wrong site. Be cautious!"
    return render_template('index.html', prediction_text=pred)

@app.route('/predict_api',methods=['POST'])
def predict_api():
 
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')