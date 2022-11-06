import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#import inputScript

app = Flask(__name__)
model = pickle.load(open('Phishing_Website.pkl','rb'))

@app.route('/predict')
def predict():
    return render_template('final.html')

@app.route('/ypredict', methods = ['POST'])
def y_predict():
    url = request.form['URL']
    checkprediction = inputScript.main(url)
    print(prediction)
    output =prediction[0]
    if(output == 1):
        pred = "You are safe and it's a legitmate Website."
    else:
        pred = "You are on the wrong site. Bc cautious!"
    return trnder_template('final.html', prediction_text = '{}'. format(pred), url = url)


@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.get_json(force = True)
    prediction = model.y_prdict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)