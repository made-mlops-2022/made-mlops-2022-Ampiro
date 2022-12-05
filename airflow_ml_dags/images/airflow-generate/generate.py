import os
import click
from sklearn.datasets import make_classification
import pandas as pd


@click.command("generate")
@click.argument("output_dir")
def generate(output_dir: str):
    x, y = make_classification(
        n_samples=100,
        n_classes=2
    )
    x_frame = pd.DataFrame(x)
    y_frame = pd.DataFrame(y)

    os.makedirs(output_dir, exist_ok=True)
    x_frame.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    y_frame.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == '__main__':
    generate()
