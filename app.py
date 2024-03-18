from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    engine_size = float(request.form['Size'])

    # Make prediction
    prediction = model.predict([[engine_size]])
    output = np.round(prediction[0], 2)

    return render_template('index.html', prediction_text="Fuel Consumption: {} mpg".format(output[0]))


@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])

    output=prediction[0]
    return jsonify(output)
if __name__=="__main__":
    app.run(debug=True)
    