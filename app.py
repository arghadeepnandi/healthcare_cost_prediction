from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import sys
import os
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            # Get form data
            age = int(request.form.get('age'))
            sex = request.form.get('sex')
            bmi = float(request.form.get('bmi'))
            children = int(request.form.get('children'))
            smoker = request.form.get('smoker')
            region = request.form.get('region')
            
            data = CustomData(
                age=age,
                sex=sex,
                bmi=bmi,
                children=children,
                smoker=smoker,
                region=region
            )
            
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")
            
            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")
            
            # Return template with results AND original form data
            return render_template('index.html', 
                                   results=results[0],
                                   age=age,
                                   sex=sex,
                                   bmi=bmi,
                                   children=children,
                                   smoker=smoker,
                                   region=region)
        
        except Exception as e:
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            return render_template('index.html', error=str(e))

if __name__ == "__main__":
    print("=" * 80)
    print("💊 Healthcare Cost Predictor - Starting Flask Server")
    print("=" * 80)
    print(f"📁 Working Directory: {os.getcwd()}")
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    
    # Check if model exists
    model_path = os.path.join("artifacts", "model.pkl")
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
    
    if os.path.exists(model_path) and os.path.exists(preprocessor_path):
        print("✅ Model and preprocessor found")
    else:
        print("⚠️  WARNING: Model not found! Please run training pipeline first:")
        print("   python train_model.py")
    
    print("\n🌐 Server will start at: http://localhost:5001")
    print("   Press CTRL+C to stop the server")
    print("=" * 80)
    print()
    
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False)