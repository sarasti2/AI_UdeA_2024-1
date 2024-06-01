from flask import Flask, jsonify, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    return jsonify({"Hello": "World"})


@app.route("/predict", methods=['POST'])
def predict():
     json_ = request.json
     df = pd.DataFrame(json_)
     prediction = xgb.predict(df)
     return jsonify({'prediction': list(prediction)})


if __name__ == "__main__":
    with open('fase-3/modelo/model.pkl', 'rb') as f:
        xgb = pickle.load(f)
    app.run(debug=True)