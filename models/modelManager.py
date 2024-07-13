import os

class ModelManager:
    
    @staticmethod
    def get_models():
        path = os.path.join('.', 'models')
        models = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) and name != '__pycache__']
        return models

    @staticmethod
    def path_model(model):
        models = ModelManager.get_models()
        model = next((x for x in models if x == model), None)
        if model is not None:
            model = os.path.join(os.path.abspath('.'), 'models', model)
        return model
    
if __name__ == '__main__':
    print(ModelManager.path_model('XXX'))