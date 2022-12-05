if [[ -z "${MODEL_PATH}" ]]; then
  export MODEL_PATH="../data/model.joblib"
fi

# Running unittests for predict endpoint
pytest

# Running series of requests
python -m test_requests