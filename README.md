# 🏠 House Price Prediction using Scikit-learn and Flask

This project is a machine learning web application that predicts housing prices using the [Boston Housing dataset](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv). The model is built with **scikit-learn** and served via a simple **Flask web UI**.

---

## 📊 Project Overview

- 📌 **Dataset**: Boston Housing (13 features)
- 🔍 **ML Model**: Random Forest Regressor
- 📈 **Metrics**: MAE, MSE, R² Score
- 💻 **Frontend**: HTML/CSS
- 🌐 **Backend**: Python (Flask)

---

## 🧠 Features Used

- `crim`: Per capita crime rate
- `zn`: Residential land zoned for large lots
- `indus`: Industrial land proportion
- `chas`: Proximity to Charles River (1/0)
- `nox`: Nitric oxide concentration
- `rm`: Avg. number of rooms
- `age`: Older homes percentage
- `dis`: Distance to employment centers
- `rad`: Highway access index
- `tax`: Property tax rate
- `ptratio`: Student-teacher ratio
- `b`: Demographic variable
- `lstat`: % lower status population

---


## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 🛠️ Run the App

### Step 1: Train the model
This script downloads the dataset, trains the model, and saves the model & scaler:
```bash
python train_model.py
```

### Step 2: Start the Flask server
```bash
python app.py
```

Then open your browser and go to:
👉 http://127.0.0.1:5000/

## 📂 Project Structure

```
house-price-prediction/
│
├── app.py                # Flask backend
├── model.py             # Model training script
├── house_price_model.pkl # Saved ML model
├── scaler.pkl            # Saved scaler
├── templates/
│   └── index.html        # Web UI (form)
├── static/
│   └── style.css         # CSS for styling
```

## 📷 Demo Screenshot

![Application Screenshot](path_to_your_screenshot.png)

## 🧪 Sample Input for Testing

- Crime rate: 0.1
- Avg. rooms: 6.5
- NOx concentration: 0.5
- Distance to employment: 4.0
- Pupil-teacher ratio: 18
- Lower status %: 12
- ...and other fields from the form

## 📈 Model Performance (Sample)

- MAE: 1.83
- MSE: 7.01
- R² Score: 0.91

(Scores may vary slightly on re-training)

## 🚀 Future Improvements

- Add model comparison (Linear Regression, XGBoost)
- Add plots for feature importance
- Deploy using Docker or Render
- Implement cross-validation
- Add more extensive error handling

## 🔧 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML/CSS

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
