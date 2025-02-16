# Purpose
- Test functionality of **MLflow** and **DagsHub**.
    - How to register your experiments
    - How to share the experiments among different envs
    - How to load model from the different env from dev env
    - How to trace the model in / out

# Prerequisite
- Models are developed in **Google Colab**.
- Models are deployed and called in **your local env**.
- The repo uses uv to manage the python packages necessary for this test. After installing uv in your local env, run the following script to set up the python env.

```bash
uv sync
```

Main dependencies:
- mlflow
- dagshub

# How to register your experiments
- You can use your local env and DagsHub to register your experiments. In order to share your experiments, using DagsHub is convenient. Although it has subscription plan, free plan works enough for personal development.

## Local
- Use MLflow.
- Check out [tracking.py](tracking.py) as an example script.
> ### What is MLflow?
> MLflow is a solution to many of these issues in this dynamic landscape, offering tools and simplifying processes to streamline the ML lifecycle and foster collaboration among ML practitioners. Throughout the lifecycle of a particular project, there are components within MLflow that are designed to cater to different needs.

![image](https://mlflow.org/docs/latest/_images/mlflow-overview.png)

Before run the code, you need to run the server.

```bash
uv run mlflow server --host 127.0.0.1 --port 8080
```

> [!WARNING]
> This option does not work when you run your code in Google Colab, so you need to go with the remote option as described in the next section.

## Remote (DagsHub)
- MLflow can be integrated with the major cloud services such as AWS [ref](https://mlflow.org/docs/latest/introduction/index.html). To minimize the running cost, [DagsHub](https://dagshub.com/docs/index.html) is tested in this repo.

> ### What is DagsHub?
> DagsHub is an AI platform that helps developers and teams manage the entire lifecycle from data collection, through dataset curation and annotation, tracking experimentation (both model training and prompt engineering), to model management. DagsHub is based on open source tools and formats (such as Git, DVC, MLflow, Label Studio, and others) so it should quickly feel familiar.

![image](https://dagshub.com/docs/assets/index/dagshub-flow.png)

> [!IMPORTANT]
> In order to run your code to train your model in Cloab env, you need to launch your notebook from GUI. To check out the details, refer this [link](https://dagshub.com/docs/integration_guide/google_colab/).

# How to load model from the different env from dev env
## Local
- When the registory is located in the same env with your production env, check out [load_model.py](load_model.py).
- Also see the [offical doc](https://mlflow.org/docs/latest/getting-started/registering-first-model/step3-load-model.html).

## Remote (DagsHub)
- Check out [load_model_dagshub.py](load_model_dagshub.py).
> [!NOTE]
> The usage is almost the same as Local. Before loading, you need to complete authetification. Check out the [official doc] (https://dagshub.com/docs/client/reference/auth.html).

# How to trace the model in / out
- Check out [logging_prediction_history.py](logging_prediction_history.py).
- Also see the [official doc](https://mlflow.org/docs/latest/llms/tracing/index.html).

![image](https://mlflow.org/docs/latest/_images/tracing-top.gif)