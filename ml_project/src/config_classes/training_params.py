from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="RandomForestClassifier")
    random_state: int = field(default=42)
    model_params: dict = field(
        default_factory=lambda: {
            'criterion': 'gini',
            'max_depth': 5,
            'n_estimators': 10
        }
    )
