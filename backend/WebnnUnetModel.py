from Model import Model

class WebnnUnetModel(Model):
    
    def getSegmentation(self, path: str):
        print('Hola')
        
if __name__ == "__main__":
    
    obj = WebnnUnetModel()
    
    obj.getSegmentation(path = "2")
    