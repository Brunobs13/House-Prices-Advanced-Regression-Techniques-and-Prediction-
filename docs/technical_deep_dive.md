# Technical Deep Dive

## 1) Deep Architecture Explanation

### End-to-end project flow

1. Load train/test CSV from external data directory.
2. Split `SalePrice` target from training features.
3. Build preprocessing graph:
   - numeric: median imputation
   - categorical: most-frequent imputation + one-hot encoding
4. Build regression estimator by configuration.
5. Train pipeline and evaluate on validation split.
6. Persist model + metrics + submission outputs.

### Why these design decisions

- `ColumnTransformer` ensures robust mixed-type feature handling.
- Model factory keeps algorithm swap low-friction.
- YAML config centralizes runtime behavior and paths.
- Script entrypoints support CI and batch automation.

### Trade-offs

- Notebook flexibility reduced in favor of reproducibility.
- RandomForest baseline increases training time vs linear models.
- Current validation strategy is simple hold-out, not CV.

### Alternatives considered

- Full notebook-only flow (rejected: weak reproducibility)
- XGBoost/LightGBM first baseline (deferred: extra operational complexity)
- MLflow integration immediately (deferred: staged adoption)

## 2) Interview Questions - Junior Level

1. What is the role of `ColumnTransformer` in this pipeline?
2. Why do we impute missing values separately for numeric and categorical columns?
3. Why use one-hot encoding for categorical features?
4. What does RMSE represent in price prediction?
5. Why separate training and prediction scripts?
6. Why keep data outside Git in this project?

## 3) Interview Questions - Senior Level

1. How would you productionize this pipeline for batch and real-time use?
2. How would you detect and handle data drift post-deployment?
3. How would you design multi-environment model promotion (dev/stage/prod)?
4. How would you integrate MLflow and model registry governance?
5. What monitoring KPIs would you define for house price predictions?
6. How would you optimize training cost/performance at larger scale?

## 4) Critical Code Areas and Interview Focus

### `src/house_prices/features.py`

- Defines preprocessing contract and feature-group inference.
- Interview angle: correctness under missing values and unseen categories.

### `src/house_prices/model.py`

- Encapsulates model selection with deterministic random state.
- Interview angle: extensibility and model-switch safety.

### `scripts/train.py`

- Pipeline assembly, split strategy, metrics persistence.
- Interview angle: reproducibility and artifact lifecycle.

### `scripts/predict.py`

- Loads model artifact and generates Kaggle-format submission.
- Interview angle: interface contract and deployment consistency.

### `.github/workflows/ci.yml`

- Automated quality gate for test execution.
- Interview angle: minimum viable CI for ML codebases.
