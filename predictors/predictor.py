from abc import ABC, abstractmethod
import os

class Predictor(ABC):
    """
    This class is the template for requesting an inference to the model
    
    Attributes:
        model (str): model path
    """
    
    def __init__(self, model):
        """
        Create a new predictor. It assign a model

        Args:
            model (str): name model
        """
        self.model = os.path.join('..','models', model)
    
    @abstractmethod
    def predict(self, img_input, img_output) -> bool:
        """
        This method does the request to the model

        Args:
            img_input (str): input image path
            img_output (str): output image path

        Returns:
            bool: _description_
        """
        pass