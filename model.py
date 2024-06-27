import joblib
  
 

 

def get_prediction(data):
    model_path = r"best_model_v0.joblib"
    model = joblib.load(model_path)
    return model.predict(data)
    
    
 
    
    