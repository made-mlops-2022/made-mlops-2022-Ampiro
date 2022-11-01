from dataclasses import dataclass, field
from typing import List


@dataclass()
class DataParams:
    cat_cols: List[str] = field(default_factory=lambda: [])
    cols_to_drop: List[str] = field(default_factory=lambda: [])
    target_col: str = field(default="condition")
