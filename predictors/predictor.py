from abc import ABC, abstractmethod
import os

class Predictor(ABC):
    
    def __init__(self, model):
        model_path = os.path.join('..','models', model)
        self.model = model_path
    
    @abstractmethod
    def predict(self, imagen):
        pass