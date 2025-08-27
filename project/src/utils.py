# Custom indicator functions
def calculate_rsi(series, window=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calculate_macd(series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast).mean()
    ema_slow = series.ewm(span=slow).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal).mean()
    return macd_line - signal_line

def prepare_features(data):
    """Prepare features from raw market data"""
    data = data.copy()
    data['Returns'] = data['Close'].pct_change()
    data['Volume_MA'] = data['Volume'].rolling(5).mean()
    data['SMA_10'] = data['Close'].rolling(10).mean()
    data['SMA_50'] = data['Close'].rolling(50).mean()
    data['RSI'] = calculate_rsi(data['Close'])
    data['MACD'] = calculate_macd(data['Close'])
    
    clean_data = data[['Returns', 'Volume_MA', 'SMA_10', 'SMA_50', 'RSI', 'MACD', 'Close']].dropna()
    return clean_data

def calculate_metrics(y_true, y_pred):
    """Calculate regression metrics"""
    from sklearn.metrics import r2_score, mean_squared_error
    import numpy as np
    
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return {'r2_score': r2, 'rmse': rmse}