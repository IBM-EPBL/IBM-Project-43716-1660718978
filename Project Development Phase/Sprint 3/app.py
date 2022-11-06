from flask import Flask, render_template,request, jsonify
from flask_cors import CORS
import sklearn
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open('Project Development Phase\Sprint 3\Phishing_model.pkl','rb'))
dataset = [[-1,	-1,	1,	1,	1,	-1,	1,	1,	-1,	1,	1,	1,	-1,	0,	1,	1,	1,	1,	0,	1,	1,	1,	1,	1,	1,	0,	-1,	1,	1,	1,]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    dataList = []
    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json()
    print(data)
    prediction = model.predict(data['data'])
    return jsonify({'output':str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')