import os
import pandas as pd
import joblib
import click


@click.command("predict")
@click.option("--data-dir")
@click.option("--model-dir")
@click.option("--output-dir")
def predict(data_dir: str, model_dir: str,  output_dir: str):
    data = pd.read_csv(os.path.join(data_dir, "train_data.csv"))
    model = joblib.load(os.path.join(model_dir, "model.pkl"))
    predictions = pd.DataFrame(model.predict(data))

    os.makedirs(output_dir, exist_ok=True)
    predictions.to_csv(os.path.join(output_dir, "prediction.csv"), index=False)


if __name__ == '__main__':
    predict()
