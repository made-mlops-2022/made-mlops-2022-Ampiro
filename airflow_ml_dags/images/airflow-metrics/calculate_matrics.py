import os
import pandas as pd
from sklearn.metrics import accuracy_score
import click
import json


@click.command("calculate_metrix")
@click.option("--data-dir")
@click.option("--data-type")
@click.option("--predict-dir")
@click.option("--output-dir")
def calculate_metrix(
    data_dir: str,
    data_type: str,
    predict_dir: str,
    output_dir: str
):
    y_true = pd.read_csv(os.path.join(data_dir, data_type + "_target.csv"))
    y_pred = pd.read_csv(os.path.join(predict_dir, "prediction.csv"))

    acc = accuracy_score(y_true, y_pred)
    metrics = {
        "accuracy": acc
    }

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "metrics.json")
    with open(path, 'w') as f:
        json.dump(metrics, f)


if __name__ == '__main__':
    calculate_metrix()
