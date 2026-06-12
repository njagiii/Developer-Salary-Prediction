'''
Simple Flask app for developer salary prdiction model

Run:
    python flask_app.py

then open in browser
    http://127.0.0.1:5000
'''

import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, render_template_string, jsonify

# App Setup

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__),'models','salary_pipeline.pkl')

# Picking the model
pipeline = joblib.load(MODEL_PATH)

print(f'Model loaded from {MODEL_PATH}')

# HTML form 
HTML = '''
<html>
    <head><title>Salary Predictor</title></head>
    <body>
        <h1>Developer Salary Predictor</h1>
        <form method="POST" action"/predict"></form>

        <button type="submit">Predict</>
    </body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route("/predict",methods=["POST"])
def predict():
    pass


if __name__ == '__main__':
    app.run(debug=True)
