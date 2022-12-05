import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import click


@click.command("train")
@click.option("--data-dir")
@click.option("--model-save-dir")
def train(data_dir: str, model_save_dir: str):
    x = pd.read_csv(os.path.join(data_dir, "train_data.csv"))
    y = pd.read_csv(os.path.join(data_dir, "train_target.csv"))

    model = RandomForestClassifier()
    model.fit(x, y)

    os.makedirs(model_save_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_save_dir, "model.pkl"))


if __name__ == '__main__':
    train()
