# import joblib
  
 

 

# def get_prediction(data):
#     model_path = r"F:\Guided Project\Git upload\New folder\Wild-Blueberry-Yield-Prediction\best_model_v0.joblib"
#     model = joblib.load(model_path)
#     return model.predict(data)
    
    
import joblib
import os

def get_prediction(data):
    model_path = os.path.join(os.path.dirname(__file__), 'best_model_v0.joblib')
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    try:
        model = joblib.load(model_path)
    except Exception as e:
        raise IOError(f"Error loading the model: {e}")
    
    try:
        predictions = model.predict(data)
    except Exception as e:
        raise ValueError(f"Error making predictions: {e}")

    return predictions
    
    