# Predictors

The predictors are responsible for requesting an inference from the model. They facilitate the interaction between the user and the model, ensuring that data is sent for prediction and results are received efficiently.

## Create a new predictor

1. Create a New File: Create a new file to place one or more new predictors. You can have multiple predictors in a single file.

2. Define Each Predictor as a Class: Each predictor should be a class that inherits from the Predictor class and implements the predict method. The predict method should accept the path of an input image and output image as a parameter. Within the predict method, include all the logic required to request an inference from the model.