PYTHON ?= python3

.PHONY: install train predict test clean

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

train:
	PYTHONPATH=src $(PYTHON) scripts/train.py

predict:
	PYTHONPATH=src $(PYTHON) scripts/predict.py

test:
	PYTHONPATH=src $(PYTHON) -m pytest -q

clean:
	rm -rf .pytest_cache __pycache__ src/house_prices/__pycache__ tests/__pycache__
