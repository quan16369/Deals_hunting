import os
import re
from typing import List
from sentence_transformers import SentenceTransformer
import joblib
from agents.agent import Agent



class CatBoosttAgent(Agent):

    name = "CATBOOST Agent"
    color = Agent.CYAN

    def __init__(self):

        self.log("CATBOOST Agent is initializing")
        self.vectorizer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.model = joblib.load('ml_model/cat_model.pkl')
        self.log("CATBOOST Agent is ready")

    def price(self, description: str) -> float:
      
        self.log("CATBOOST Agent is starting a prediction")
        vector = self.vectorizer.encode([description])
        result = max(0, self.model.predict(vector)[0])
        self.log(f"CATBOOST Agent completed - predicting ${result:.2f}")
        return result