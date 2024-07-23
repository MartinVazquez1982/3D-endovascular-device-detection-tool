# Models

The models are responsible for performing the inferences. They process the input data and provide predictions based on their training.

## Upload a new model

1. **Create a Directory for the Model**: Create a new directory within the `model/` directory. The directory name should be descriptive of the model.

2. **Save Model Files**: Place all necessary files for the model in this new directory. This typically includes the trained model file (e.g., `model.pkl`), configuration files, and any other relevant scripts.

3. **Create the metrics.json file**: This file is to store the different metrics and view it on the models page.

Structure of the `metrics.json` file:

```json
{
    "Model": "Model name",
    "Classification Error": 0.0,
    "DICE": 0.0,
    "Sensitivity": 0.0,
    "Precision": 0.0,
    "F1 Score": 0.0,
    "Specificity": 0.0,
    "Accuracy": 0.0
}
```

Basic structure of a model directory:

```
models
|-- ModelName
    |-- metrics.json
    |-- Others files & directories
```