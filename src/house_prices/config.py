from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class TrainConfig:
    target_column: str
    id_column: str
    validation_size: float
    random_state: int
    model_type: str


@dataclass(frozen=True)
class PathsConfig:
    train_csv: str
    test_csv: str
    model_output: str
    metrics_output: str
    predictions_output: str


@dataclass(frozen=True)
class ProjectConfig:
    train: TrainConfig
    paths: PathsConfig


def load_config(config_path: str | Path = "configs/config.yaml") -> ProjectConfig:
    path = Path(config_path)
    content = yaml.safe_load(path.read_text(encoding="utf-8"))

    train = TrainConfig(**content["train"])
    paths = PathsConfig(**content["paths"])
    return ProjectConfig(train=train, paths=paths)
