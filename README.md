# 3D Endovascular Device Detection Tool

This web page was made like end part final project of the system engineering degree course. Its functionality is to request an inference from a trained model during the final project.

## Table of Contents

1. [Install Dependencies](#install-dependencies)
2. [Run the Application](#run-the-application)
3. [Use](#use)
    - [Predictor](#predictor)
    - [Add a Model](#add-a-model)
4. [Project Structure](#project-structure)
5. [Creators & Directors](#creators--directors)

## Install dependencies

For install the dependecies for Anaconda must execute the following command:

```bash
conda env create -f environment.yml
```

Otherwise, install Streamlit:

```bash
pip install streamlit
```

## Run the application

For run the web page execute the following command:

```bash
streamlit run app.py
```

## Use

To request an inference you must create a predictor and load one or more models.

### Predictor

A predictor does the request of the inference to the model.Instructions for creating a predictors are in the `predictors/README.md` file.

### Add a model

A model is the one that does the inference. Instructions for adding  models can be found in the `models/README.md` file.

## Project structure

The project structure is as follows:

```
3D-endovascular-device-detection-tool
|-- .streamlit
    |-- config.toml
|-- images
|-- models
    |-- modelManager.py
    |-- README.md
|-- pages
    |-- about.py
    |-- home.py
    |-- models.py
|-- predictors
    |-- predictor.py
    |-- README.md
.gitignore
app.py
environment.yml
README.md
```

## Creators & Directors

| Role        | Name           | Contact                     |
|-------------|----------------|-----------------------------|
| Creator     | David Burckhardt   | [burck432@gmail.com](mailto:burck432@gmail.com)   |
| Creator     | Martin Vazquez Arispe    | [martin.vazquez.arispe@gmail.com](mailto:martin.vazquez.arispe@gmail.com)     |
| Director    | Dr. Ignacio Larrabide  | [ilarrabide@pladema.exa.unicen.edu.ar](mailto:ilarrabide@pladema.exa.unicen.edu.ar)    |
| Co-Director    | Dra. Romina Luciana Muñoz   | [romi.l.m9@gmail.com](mailto:romi.l.m9@gmail.com)     |