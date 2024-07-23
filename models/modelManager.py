import os
import json

import pandas as pd

class ModelManager:
    """
    this class performs the administration of the models

    Attributes:
        metrics_models (pd.DataFrame | None): Pandas dataframe with the metric values if it created; else None if not
    """
    
    metrics_models = None
    
    @staticmethod
    def get_models() -> list[str]:
        """
        this method returns the model names in the mdoels directory

        Returns:
            list[str]: list of the model name
        """
        path = os.path.join('models')
        models = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) and name != '__pycache__']
        return models

    @staticmethod
    def path_model(model: str) -> str | None:
        """
        This method returns the model path if it exists; else it returns None.

        Args:
            model (str): Model name

        Returns:
            str | None: model path or None
        """
        models = ModelManager.get_models()
        model = next((x for x in models if x == model), None)
        if model is not None:
            model = os.path.join(os.path.abspath('.'), 'models', model)
        return model
    
    @staticmethod
    def getDataFrameMetrics() -> pd.DataFrame:
        """
        This method creates and returns a pandas dataframe with the metric values

        Returns:
            pd.DataFrame: Pandas dataframe with the metric values
        """
        if ModelManager.metrics_models is None:
            all_metrics = []
            pd.options.display.float_format = '{:.10f}'.format
            metric_models = [os.path.join('models', model, 'metrics.json') for model in ModelManager.get_models()]
            for metrics in metric_models:
                with open(metrics, 'r') as f:
                    data = json.load(f)
                all_metrics.append(data)
            ModelManager.metrics_models = pd.DataFrame(all_metrics)
            ModelManager.metrics_models = ModelManager.metrics_models.style.format({
                'CER': '{:.7f}',
                'DICE Coefficient': '{:.7f}',
                'Sensitivity': '{:.7f}',
                'Precision': '{:.7f}',
                'F1 Score': '{:.7f}',
                'Specificity':'{:.7f}',
                'Accuracy':'{:.7f}'
            })
        return ModelManager.metrics_models
