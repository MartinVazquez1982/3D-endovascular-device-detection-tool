from abc import ABC, abstractmethod
import os

class Predictor(ABC):
    
    def __init__(self, model):
        self.model = os.path.join('..','models', model)
    
    @abstractmethod
    def predict(self, img_input, img_output) -> bool:
        """_summary_

        Args:
            img_input (_type_): _description_
            img_output (_type_): _description_

        Returns:
            bool: _description_
        """
        pass