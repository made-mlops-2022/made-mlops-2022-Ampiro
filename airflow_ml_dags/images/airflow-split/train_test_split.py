import os
import pandas as pd
from sklearn.model_selection import train_test_split
import click


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split(input_dir: str, output_dir: str):
    x = pd.read_csv(os.path.join(input_dir, "data.csv"))
    y = pd.read_csv(os.path.join(input_dir, "target.csv"))

    x_train, x_test, y_train, y_test = train_test_split(
        x, y,
        test_size=0.2,
        random_state=42
    )

    x_train = pd.DataFrame(x_train)
    y_train = pd.DataFrame(y_train)
    x_test = pd.DataFrame(x_test)
    y_test = pd.DataFrame(y_test)

    os.makedirs(output_dir, exist_ok=True)
    x_train.to_csv(os.path.join(output_dir, "train_data.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "train_target.csv"), index=False)

    x_test.to_csv(os.path.join(output_dir, "test_data.csv"), index=False)
    y_test.to_csv(os.path.join(output_dir, "test_target.csv"), index=False)


if __name__ == '__main__':
    split()
