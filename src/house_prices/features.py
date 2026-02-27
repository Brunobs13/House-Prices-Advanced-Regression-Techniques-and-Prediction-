from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def infer_feature_groups(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    numeric_features = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = df.select_dtypes(exclude=["number"]).columns.tolist()
    return numeric_features, categorical_features


def build_preprocessor(df: pd.DataFrame) -> ColumnTransformer:
    numeric_features, categorical_features = infer_feature_groups(df)

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
