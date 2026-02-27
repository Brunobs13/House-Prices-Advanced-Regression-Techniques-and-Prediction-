from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def split_train_features_target(df: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    features = df.drop(columns=[target_column])
    target = df[target_column]
    return features, target
