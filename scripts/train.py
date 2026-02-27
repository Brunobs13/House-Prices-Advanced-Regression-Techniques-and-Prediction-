from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from house_prices.config import load_config
from house_prices.data import load_csv, split_train_features_target
from house_prices.features import build_preprocessor
from house_prices.model import build_regressor


def main() -> None:
    config = load_config()

    train_df = load_csv(config.paths.train_csv)
    X, y = split_train_features_target(train_df, config.train.target_column)

    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        test_size=config.train.validation_size,
        random_state=config.train.random_state,
    )

    preprocessor = build_preprocessor(X_train)
    regressor = build_regressor(config.train.model_type, config.train.random_state)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", regressor),
        ]
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_valid)

    rmse = float(np.sqrt(mean_squared_error(y_valid, predictions)))
    mae = float(mean_absolute_error(y_valid, predictions))

    metrics = {
        "rmse": rmse,
        "mae": mae,
        "validation_rows": int(len(X_valid)),
        "model_type": config.train.model_type,
    }

    model_path = Path(config.paths.model_output)
    metrics_path = Path(config.paths.metrics_output)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(pipeline, model_path)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Training completed.")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
