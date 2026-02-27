from __future__ import annotations

from pathlib import Path

import joblib

from house_prices.config import load_config
from house_prices.data import load_csv


def main() -> None:
    config = load_config()

    test_df = load_csv(config.paths.test_csv)
    model = joblib.load(config.paths.model_output)

    predictions = model.predict(test_df)

    out_df = test_df[[config.train.id_column]].copy()
    out_df[config.train.target_column] = predictions

    output_path = Path(config.paths.predictions_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(output_path, index=False)

    print(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    main()
