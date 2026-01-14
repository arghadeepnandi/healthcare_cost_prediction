import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        """
        Train multiple models and select the best one
        """
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "XGBRegressor": XGBRegressor(),
                "AdaBoost": AdaBoostRegressor(),
            }
            
            params = {
                "Decision Tree": {
                    'max_depth': [5, 10, 15, 20],
                    'min_samples_split': [2, 5, 10],
                },
                "Random Forest": {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [10, 20, 30],
                    'min_samples_split': [2, 5],
                },
                "Gradient Boosting": {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'max_depth': [3, 5, 7],
                },
                "Linear Regression": {},
                "Ridge": {
                    'alpha': [0.1, 1.0, 10.0],
                },
                "Lasso": {
                    'alpha': [0.1, 1.0, 10.0],
                },
                "XGBRegressor": {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'max_depth': [3, 5, 7],
                },
                "AdaBoost": {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.05, 0.1],
                }
            }
            
            model_report: dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params
            )
            
            # Get best model based on test R2 score
            best_model_name = max(model_report, key=lambda x: model_report[x]['test_r2'])
            best_model_score = model_report[best_model_name]['test_r2']
            best_model = models[best_model_name]
            
            # Retrain best model with best parameters
            best_params = params[best_model_name]
            if best_params:
                from sklearn.model_selection import GridSearchCV
                gs = GridSearchCV(best_model, best_params, cv=3, n_jobs=-1)
                gs.fit(X_train, y_train)
                best_model.set_params(**gs.best_params_)
            
            best_model.fit(X_train, y_train)
            
            if best_model_score < 0.6:
                raise CustomException("No best model found with R2 score > 0.6", sys)
            
            logging.info(f"Best model found: {best_model_name} with R2 score: {best_model_score:.4f}")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            
            return r2_square
        
        except Exception as e:
            raise CustomException(e, sys)