from flask import Flask, render_template,request, jsonify
from flask_cors import CORS
import sklearn
from sklearn.linear_model import LogisticRegression
import pickle
from inputs import devices

app = Flask(__name__)
CORS(app)

model = pickle.load(open('Project Development Phase\Sprint 3\Phishing_model.pkl','rb'))
#dataset = [[-1,	-1,	1,	1,	1,	-1,	1,	1,	-1,	1,	1,	1,	-1,	0,	1,	1,	1,	1,	0,	1,	1,	1,	1,	1,	1,	0,	-1,	1,	1,	1,]]

@app.route('/')
def home():
    return render_template('\Sprint 4\index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #dataList = []
    url = request.form['URL']
    checkprediction = inputScript.main(url)
    print(checkprediction)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="Your are safe!!  This is a Legitimate Website."
        
    else:
        pred="You are on the wrong site. Be cautious!"
    return render_template('index.html', prediction_text='{}'.format(pred),url=url)
    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json()
    print(data)
    prediction = model.predict(data['data'])
    return jsonify({'output':str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')