from __future__ import annotations

import pandas as pd

from house_prices.features import build_preprocessor, infer_feature_groups


def test_infer_feature_groups() -> None:
    df = pd.DataFrame(
        {
            "LotArea": [8450, 9600],
            "OverallQual": [7, 6],
            "Neighborhood": ["CollgCr", "Veenker"],
            "Street": ["Pave", "Pave"],
        }
    )

    numeric, categorical = infer_feature_groups(df)

    assert "LotArea" in numeric
    assert "Neighborhood" in categorical


def test_preprocessor_fit_transform() -> None:
    df = pd.DataFrame(
        {
            "LotArea": [8450, 9600, 11250],
            "OverallQual": [7, 6, 7],
            "Neighborhood": ["CollgCr", "Veenker", "CollgCr"],
            "Street": ["Pave", "Pave", "Grvl"],
        }
    )

    preprocessor = build_preprocessor(df)
    transformed = preprocessor.fit_transform(df)

    assert transformed.shape[0] == len(df)
