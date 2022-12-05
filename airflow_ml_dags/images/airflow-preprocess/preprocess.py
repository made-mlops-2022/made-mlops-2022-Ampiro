import os
import pandas as pd
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))

    mean = data.mean()
    std = data.std()
    data = (data - mean) / std

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "data.csv"), index=False)


if __name__ == '__main__':
    preprocess()
