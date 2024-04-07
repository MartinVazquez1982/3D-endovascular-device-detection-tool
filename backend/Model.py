from abc import ABCMeta, abstractmethod

class Model(metaclass=ABCMeta):
    
    @abstractmethod
    def getSegmentation(self, path: str):
        pass