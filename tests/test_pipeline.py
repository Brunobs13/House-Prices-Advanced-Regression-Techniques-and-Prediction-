from __future__ import annotations

import pandas as pd
from sklearn.pipeline import Pipeline

from house_prices.features import build_preprocessor
from house_prices.model import build_regressor


def test_pipeline_training_and_prediction() -> None:
    df = pd.DataFrame(
        {
            "Id": [1, 2, 3, 4, 5],
            "LotArea": [8450, 9600, 11250, 9550, 14260],
            "OverallQual": [7, 6, 7, 7, 8],
            "Neighborhood": ["CollgCr", "Veenker", "CollgCr", "Crawfor", "NoRidge"],
            "Street": ["Pave", "Pave", "Grvl", "Pave", "Pave"],
            "SalePrice": [208500, 181500, 223500, 140000, 250000],
        }
    )

    X = df.drop(columns=["SalePrice"])
    y = df["SalePrice"]

    preprocessor = build_preprocessor(X)
    regressor = build_regressor("ridge", random_state=42)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", regressor),
        ]
    )

    pipeline.fit(X, y)
    predictions = pipeline.predict(X)

    assert len(predictions) == len(X)
    assert float(predictions[0]) > 0.0
