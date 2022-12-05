import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from data_schemas import DataModel, PredictionModel


app = FastAPI()

model_path = os.environ["MODEL_PATH"]
model = joblib.load(model_path)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.post("/predict", response_model=PredictionModel)
def predict(data: DataModel) -> PredictionModel:
    pred_data = pd.DataFrame(data.dict(), index=[0])
    prediction = model.predict(pred_data)
    prediction = PredictionModel(prediction=prediction)
    return prediction


@app.get("/health", status_code=200)
def health():
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_425_TOO_EARLY,
            detail="Model is not ready"
        )
    return {"message": "Model is ready"}
