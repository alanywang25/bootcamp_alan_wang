from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import matplotlib
# Use non-interactive backend to avoid threading issues
matplotlib.use('Agg')  # Must be set before importing pyplot
import matplotlib.pyplot as plt
import io
import base64
from src.utils import prepare_features

app = Flask(__name__)

# Load model and scaler
try:
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    print("Model and scaler loaded successfully!")
except FileNotFoundError:
    print("Model files not found. Please train the model first.")
    model = None
    scaler = None

@app.route('/predict', methods=['POST'])
def predict():
    """Predict returns from JSON features"""
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
            
        features = data['features']
        if len(features) != 5:
            return jsonify({'error': 'Expected 5 features: [Volume_MA, SMA_10, SMA_50, RSI, MACD]'}), 400
            
        # Scale features and predict
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'features': features,
            'message': 'SPY returns prediction'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict/<float:input1>', methods=['GET'])
def predict_one(input1):
    """Predict returns using only Volume_MA (single feature)"""
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Use default values for other features
        default_features = [300.0, 290.0, 50.0, 0.0]  # SMA_10, SMA_50, RSI, MACD
        
        features = [input1] + default_features
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'input_used': {'Volume_MA': input1},
            'default_features_used': {
                'SMA_10': default_features[0],
                'SMA_50': default_features[1],
                'RSI': default_features[2],
                'MACD': default_features[3]
            },
            'message': 'Prediction using Volume_MA with default values for other features'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/predict/<float:input1>/<float:input2>', methods=['GET'])
def predict_two(input1, input2):
    """Predict returns using Volume_MA and RSI (two features)"""
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Use default values for remaining features
        default_features = [300.0, 290.0, 0.0]  # SMA_10, SMA_50, MACD
        
        features = [input1, default_features[0], default_features[1], input2, default_features[2]]
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]
        
        return jsonify({
            'prediction': float(prediction),
            'inputs_used': {'Volume_MA': input1, 'RSI': input2},
            'default_features_used': {
                'SMA_10': default_features[0],
                'SMA_50': default_features[1],
                'MACD': default_features[2]
            },
            'message': 'Prediction using Volume_MA and RSI with default values for other features'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/plot')
def plot():
    """Generate sample plot of model coefficients"""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Create bar plot of coefficients
        feature_names = ['Volume_MA', 'SMA_10', 'SMA_50', 'RSI', 'MACD']
        coefficients = model.coef_
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(feature_names, coefficients)
        ax.set_title('Linear Regression Coefficients')
        ax.set_ylabel('Coefficient Value')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        
        # Convert to base64
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_bytes = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        
        return f'<img src="data:image/png;base64,{img_bytes}" alt="Model Coefficients"/>'
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)