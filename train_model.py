import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.pipeline.train_pipeline import train_pipeline

if __name__ == "__main__":
    try:
        print("=" * 50)
        print("Starting Training Pipeline...")
        print("=" * 50)
        
        r2_score = train_pipeline()
        
        print("=" * 50)
        print(f"✅ Training Completed Successfully!")
        print(f"📊 Model R2 Score: {r2_score:.4f}")
        print("=" * 50)
        print("\n📁 Artifacts saved in 'artifacts/' folder:")
        print("  - data.csv")
        print("  - train.csv")
        print("  - test.csv")
        print("  - model.pkl")
        print("  - preprocessor.pkl")
        print("\n🚀 You can now run: python app.py")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()