# Portfolio-Ready Assets

## LinkedIn Version (Short)

Refactored a Kaggle house-price notebook into a production-structured ML project with modular pipeline code, config-driven training/prediction scripts, tests, CI, and interview-grade documentation.

## CV Version (Technical)

Designed and implemented a modular regression pipeline for the House Prices competition, migrating notebook logic into maintainable Python package layers (`config`, `data`, `features`, `model`). Added reproducible training and scoring scripts, automated tests, CI quality gates, and secure repository hygiene standards for professional code review and interview readiness.

## 60-Second Pitch

I transformed this project from a single notebook into a production-ready ML repository. The preprocessing and model logic now live in modular package layers, and training/prediction are script-driven with YAML configuration for reproducibility. I added tests and CI to prevent regressions and documented architecture, trade-offs, and scaling paths for interviews. This made the project much stronger from both engineering and MLOps perspectives while preserving the original modeling objective.

## 5-Minute Technical Pitch

The initial state was typical Kaggle workflow: notebook-centric, hard to reproduce, and difficult to scale. I decomposed it into four clear layers: configuration, data access, feature preprocessing, and model selection. This made the pipeline deterministic and easier to review.

I implemented script entrypoints for training and prediction. Training saves model artifacts and metrics, while prediction generates a submission-ready CSV with the exact expected schema. The preprocessing stack handles mixed feature types and missing values safely through a `ColumnTransformer`.

To improve engineering quality, I added unit tests for feature grouping and pipeline prediction behavior, and wired CI to run on every push/PR. I also hardened repository hygiene with `.gitignore`, env template, and a clear data policy that keeps competition data outside Git.

For production scale, the next path is straightforward: integrate MLflow for experiment tracking, add drift monitoring, and expose the model through an API or scheduled batch pipeline with staged environment promotion.
