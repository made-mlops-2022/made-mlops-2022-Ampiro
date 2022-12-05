from pydantic import BaseModel, validator


class DataModel(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    @validator("*")
    def check_on_none(cls, v):
        if v is None:
            raise ValueError("Data must not contain None fields")
        return v

    @validator("age")
    def age_must_be_from_train_distribution(cls, v):
        if v < 29 or v > 77:
            raise ValueError("Age must be from same value range as train data")
        return v

    @validator("sex")
    def sex_is_binary(cls, v):
        if v not in [0, 1]:
            raise ValueError("Sex must be binary [0 or 1]")
        return v

    @validator("cp")
    def cp_in_its_range(cls, v):
        if v not in [0, 1, 2, 3]:
            raise ValueError("cp must be in [0, 1, 2, 3]")
        return v

    @validator("trestbps")
    def trestbps_validation(cls, v):
        if v < 94 or v > 200:
            raise ValueError(
                "trestbps must be from same value range as train data"
            )
        return v

    @validator("chol")
    def chol_validation(cls, v):
        if v < 126 or v > 564:
            raise ValueError(
                "chol must be from same value range as train data"
            )
        return v

    @validator("fbs")
    def fbs_is_binary(cls, v):
        if v not in [0, 1]:
            raise ValueError("fbs must be binary [0 or 1]")
        return v

    @validator("restecg")
    def restecg_validation(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("restecg must be in [0, 1, 2]")
        return v

    @validator("thalach")
    def thalach_validation(cls, v):
        if v < 71 or v > 202:
            raise ValueError(
                "thalach must be from same value range as train data"
            )
        return v

    @validator("exang")
    def exang_is_binary(cls, v):
        if v not in [0, 1]:
            raise ValueError("exang must be binary [0 or 1]")
        return v

    @validator("oldpeak")
    def oldpeak_validation(cls, v):
        if v < 0.0 or v > 6.2:
            raise ValueError(
                "oldpeak must be from same value range as train data"
            )
        return v

    @validator("slope")
    def slope_validation(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("slope must be in [0, 1, 2]")
        return v

    @validator("ca")
    def ca_validation(cls, v):
        if v not in [0, 1, 2, 3]:
            raise ValueError("ca must be in [0, 1, 2, 3]")
        return v

    @validator("thal")
    def thal_validation(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("thal must be in [0, 1, 2]")
        return v


class PredictionModel(BaseModel):
    prediction: int

    @validator("prediction")
    def prediction_is_binary(cls, v):
        if v not in [0, 1]:
            raise ValueError("prediction must be binary [0, 1]")
        return v

    def __str__(self) -> str:
        return str(self.prediction)
