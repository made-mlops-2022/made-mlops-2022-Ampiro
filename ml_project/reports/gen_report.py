import pandas_profiling
import pandas as pd


def main():
    """ Generating HTML file with EDA from pandas profiling
    """
    data = pd.read_csv("../data/raw/heart_cleveland_upload.csv")
    profile = pandas_profiling.ProfileReport(data)
    profile.to_file("eda_report.html")


if __name__ == "__main__":
    main()
