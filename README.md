# Weather_Forecast_App
# Weather Forecasting Web Application

## Overview
This project is a Flask-based web application that predicts whether it will rain based on user-input weather parameters. It leverages machine learning models trained on historical weather data to provide accurate predictions. The application features a user-friendly web interface where users can enter weather parameters, and the model processes this data to generate predictions.

## Project Structure
- **application.py**: The main Flask application responsible for handling user requests and model inference.
- **model_2.pkl**: A trained machine learning model used for weather prediction.
- **model_svc.pkl**: A Support Vector Classifier (SVC) model for classification.
- **scaler2.pkl**: A standard scaler used for preprocessing input data.
- **Weather_forecast.ipynb**: Jupyter notebook containing data preprocessing, model training, and evaluation.
- **Weather_forecast_RandomSearchCV.ipynb**: Notebook demonstrating hyperparameter tuning using RandomSearchCV.
- **weather_forecast_data.csv**: Dataset used for training and testing the model.

## Machine Learning Models Used
### **1. Support Vector Classifier (SVC)**
Support Vector Machines (SVM) are supervised learning models used for classification tasks. The `model_svc.pkl` file contains a trained SVC model that classifies input weather parameters into two categories: "Rain" or "No Rain." SVM is known for its ability to handle high-dimensional data effectively.

### **2. Alternative Model (model_2.pkl)**
Another machine learning model (`model_2.pkl`) has been used for classification, though the specific algorithm used is not mentioned. This model was trained on weather features including temperature, humidity, wind speed, cloud cover, and pressure. It was evaluated based on accuracy, precision, and recall.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/weather-forecasting.git
   cd weather-forecasting
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   *(Ensure Flask, NumPy, Scikit-learn, and Joblib are installed.)*

## Usage
1. Run the Flask application:
   ```sh
   python application.py
   ```
2. Open a browser and visit:
   ```
   http://127.0.0.1:5000/
   ```
3. Enter weather parameters (temperature, humidity, wind speed, cloud cover, and pressure) in the form.
4. The application will preprocess the input using `scaler2.pkl` and pass it to the trained model.
5. The model predicts and displays whether it will rain or not.

## Future Enhancements
- Improve model accuracy by training on a larger dataset.
- Experiment with deep learning techniques for better predictions.
- Implement a REST API for external integration.
- Deploy the application on a cloud platform for accessibility.

## License
This project is licensed under the MIT License.

