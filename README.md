# House Prices - Advanced Regression Techniques and Prediction

Production-structured machine learning project for the Kaggle competition **House Prices: Advanced Regression Techniques**.

## Project Overview

This repository predicts residential sale prices by converting a notebook-only workflow into a modular, reproducible ML pipeline with CI, tests, and interview-ready documentation.

## Business Problem

Real-estate pricing models require robust handling of mixed feature types, missing values, and reproducible evaluation. Notebook-only experiments are difficult to operationalize and review. This project addresses that by providing a clean training/prediction architecture suitable for portfolio and technical interviews.

## Architecture Diagram (Textual)

```text
Kaggle CSV files (data/raw/train.csv, test.csv)
                    |
                    v
Data Layer (src/house_prices/data.py)
- load datasets
- split features/target
                    |
                    v
Feature Layer (src/house_prices/features.py)
- numeric median imputation
- categorical most-frequent imputation
- one-hot encoding
                    |
                    v
Model Layer (src/house_prices/model.py)
- Ridge / RandomForest regressor factory
                    |
                    v
Pipeline Scripts (scripts/train.py, scripts/predict.py)
- fit + validate
- persist model + metrics
- generate submission CSV
                    |
                    v
Artifacts (artifacts/model.joblib, metrics.json, submission.csv)
```

## Tech Stack

- Python 3.11+
- pandas, numpy
- scikit-learn
- PyYAML
- pytest
- GitHub Actions

## Project Structure

```text
.
├── .github/workflows/ci.yml
├── configs/
│   └── config.yaml
├── data/
│   └── README.md
├── docs/
│   ├── portfolio_ready.md
│   ├── repository_audit.md
│   └── technical_deep_dive.md
├── notebooks/
│   └── house_prices_kaggle_original.ipynb
├── scripts/
│   ├── predict.py
│   └── train.py
├── src/house_prices/
│   ├── __init__.py
│   ├── config.py
│   ├── data.py
│   ├── features.py
│   └── model.py
├── tests/
│   ├── test_features.py
│   └── test_pipeline.py
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## Setup Instructions (Step-by-step)

1. Clone repository:

```bash
git clone https://github.com/Brunobs13/House-Prices-Advanced-Regression-Techniques-and-Prediction-.git
cd House-Prices-Advanced-Regression-Techniques-and-Prediction-
```

2. Install dependencies:

```bash
make install
```

3. Download Kaggle data and place files at:

- `data/raw/train.csv`
- `data/raw/test.csv`

4. Train model:

```bash
make train
```

5. Generate predictions:

```bash
make predict
```

6. Run tests:

```bash
make test
```

## CI/CD Overview

The GitHub Actions workflow executes on push and pull requests:

- install dependencies
- run test suite
- block regressions before merge

## Data Versioning Strategy

Competition data is external and should not be committed to Git. The project stores only code and reproducible configs. For enterprise-grade data lineage, DVC can be introduced to version immutable data snapshots and feature sets.

## Model Tracking Strategy

Current baseline stores metrics in `artifacts/metrics.json`. To scale experiment governance, integrate MLflow for:

- parameter tracking
- metric comparisons
- artifact lineage
- model registry promotion

## Deployment Strategy

Current deployment target is offline batch scoring. Production evolution path:

1. Package model and preprocessor as versioned artifact.
2. Expose scoring through API or batch job runner.
3. Add model registry and staged promotion.
4. Add monitoring for feature drift and prediction drift.

## Security Considerations

- no hardcoded credentials
- `.env.example` provided for local environment patterns
- `.gitignore` blocks accidental data/artifact leakage
- competition datasets kept outside Git history

## Lessons Learned

- converting notebooks into modules improves maintainability and review quality
- deterministic config + scripts significantly improve reproducibility
- tests on preprocessing and pipeline shape catch common regressions early

## Future Improvements

1. Add cross-validation leaderboard with multiple models and stacking.
2. Add feature importance and SHAP-based explainability reports.
3. Add Optuna hyperparameter optimization.
4. Add MLflow experiment tracking.
5. Add API inference layer for real-time scoring.

## Additional Technical Documents

- Audit report: `docs/repository_audit.md`
- Deep technical analysis: `docs/technical_deep_dive.md`
- Portfolio-ready assets: `docs/portfolio_ready.md`
