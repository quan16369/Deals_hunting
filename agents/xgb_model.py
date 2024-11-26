import os
import re
from typing import List
from sentence_transformers import SentenceTransformer
import joblib
from agents.agent import Agent



class XGBoostAgent(Agent):

    name = "XGBOOST Agent"
    color = Agent.MAGENTA

    def __init__(self):

        self.log("XGBOOST Agent is initializing")
        self.vectorizer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.model = joblib.load('ml_model/xgb_model.pkl')
        self.log("XGBOOST Agent is ready")

    def price(self, description: str) -> float:
      
        self.log("XGBOOST Agent is starting a prediction")
        vector = self.vectorizer.encode([description])
        result = max(0, self.model.predict(vector)[0])
        self.log(f"XGBOOST Agent completed - predicting ${result:.2f}")
        return result