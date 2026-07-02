import pickle
import warnings
from pathlib import Path

from flask import Flask, request, jsonify, render_template
import numpy as np

try:
    from sklearn.exceptions import InconsistentVersionWarning
    warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
except Exception:
    pass

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

# Load the model from the module directory so deployment does not depend on cwd.
with open(BASE_DIR / "regmodel.pkl", "rb") as regmodel_file:
    regmodel = pickle.load(regmodel_file)

with open(BASE_DIR / "scaler.pkl", "rb") as scaler_file:
    scalar = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text="Predicted House Price is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)
