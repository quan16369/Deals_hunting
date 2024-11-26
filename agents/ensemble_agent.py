import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

from agents.agent import Agent
from agents.specialist_agent import SpecialistAgent
from agents.random_forest_agent import RandomForestAgent
from agents.lightgbm_model import LightGBMAgent
from agents.xgb_model import XGBoostAgent
from agents.cat_model import CatBoosttAgent

class EnsembleAgent(Agent):

    name = "Ensemble Agent"
    color = Agent.YELLOW
    
    def __init__(self, collection):

        self.log("Initializing Ensemble Agent")
        self.specialist = SpecialistAgent()
        self.xgb = XGBoostAgent()
      # self.cat = CatBoosttAgent()
      #  self.lgbm = LightGBMAgent()
        self.model = joblib.load('ml_model/ensemble_model.pkl')
        self.log("Ensemble Agent is ready")

    def price(self, description: str) -> float:

        self.log("Running Ensemble Agent - collaborating with specialist and XGBoost")
        specialist = self.specialist.price(description)
        #cat = self.cat.price(description)
        #lgbm = self.lgbm.price(description)
        xgb = self.xgb.price(description)
        X = pd.DataFrame({
            'Specialist': [specialist],
            #'LightGBM': [lgbm],
            #'CatBoost': [cat],
            'XGBoost': [xgb],
            'Min': [min(specialist,
                        xgb, 
                   #    lgbm, 
                   #    cat,
                        )],
            'Max': [max(specialist, 
                        xgb, 
                   #     lgbm, 
                   #     cat
                        )],
        })
        y = self.model.predict(X)[0]
        self.log(f"Ensemble Agent complete - returning ${y:.2f}")
        return y
    
    
    
