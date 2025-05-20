from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('house_price_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define the feature names in order
features = ["crim", "zn", "indus", "chas", "nox", "rm", "age", 
            "dis", "rad", "tax", "ptratio", "b", "lstat"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract input features from form and convert to float
            input_features = [float(request.form[feature]) for feature in features]

            # Scale inputs
            input_scaled = scaler.transform([input_features])

            # Predict
            prediction = model.predict(input_scaled)[0]

            return render_template('index.html', prediction=round(prediction, 2), input_data=request.form)
        except Exception as e:
            return render_template('index.html', error=str(e), input_data=request.form)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
