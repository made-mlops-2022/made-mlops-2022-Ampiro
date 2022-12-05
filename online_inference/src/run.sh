if [[ -z "${MODEL_PATH}" ]]; then
  export MODEL_PATH="../data/model.joblib"
fi

# Starting server
uvicorn endpoints:app --host 0.0.0.0 --port 8000 --reload