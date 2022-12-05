import requests
from requests import Response

import logging
import pandas as pd
# from data_schemas import DataModel

logging.basicConfig(level=logging.INFO)


def read_data() -> pd.DataFrame:
    data_path = "../data/data.csv"
    data = pd.read_csv(data_path)
    data.drop("condition", axis=1)
    return data


def make_health_request() -> Response:
    logging.info("Making health request")
    response = requests.get("http://0.0.0.0:8000/health")
    return response


def make_predict_request(data: dict) -> Response:
    logging.info("Making prediction request")
    response = requests.post(
        "http://0.0.0.0:8000/predict",
        json=data
    )
    return response


def main():
    health_response = make_health_request()
    if health_response.status_code != 200:
        logging.info("Model is not yet ready, stopping requests.")
        return
    logging.info("Model is ready to be used")

    logging.info("Reading test data from file")
    data = read_data()
    logging.info("Data is ready to use.")

    for _, row in data.iterrows():
        request_data = dict(row)
        response = make_predict_request(request_data)
        logging.info("Request status code: " + str(response.status_code))
        logging.info("Prediction: " + str(response.json()["prediction"]))

    logging.info("All requests are done.")


if __name__ == "__main__":
    main()
