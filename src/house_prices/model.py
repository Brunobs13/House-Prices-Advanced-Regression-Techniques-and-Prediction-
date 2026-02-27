from __future__ import annotations

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge


SUPPORTED_MODELS = {"ridge", "random_forest"}


def build_regressor(model_type: str, random_state: int):
    if model_type == "ridge":
        return Ridge(alpha=1.0)

    if model_type == "random_forest":
        return RandomForestRegressor(
            n_estimators=400,
            max_depth=None,
            min_samples_split=4,
            min_samples_leaf=2,
            random_state=random_state,
            n_jobs=-1,
        )

    raise ValueError(f"Unsupported model_type '{model_type}'. Supported: {sorted(SUPPORTED_MODELS)}")
