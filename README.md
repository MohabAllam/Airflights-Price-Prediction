# Airflights Price Prediction

Simple machine learning project for analyzing and modeling air flight data.

## 🔍 Project overview

This repository contains data, notebooks, models, and scripts for preprocessing, training, and running inference on air flight data. It is intended for experimentation and building models to predict flight-related outcomes (delays, status, etc.).

## 📁 Repository structure

- `Data/`
  - `raw/` — original/raw datasets
  - `clean/` — processed/cleaned datasets
- `metadata/` — dataset metadata and schemas
- `models/` — saved model artifacts and checkpoints
- `Notebooks/` — exploratory analysis and experiments (e.g. `Airflight Analysis ML.ipynb`)
- `src/` — project source code
  - `preprocessing.py` — data cleaning & feature engineering
  - `train.py` — training script
  - `inference.py` — run model predictions
  - `app.py` — lightweight app or API for serving the model

## ⚙️ Quick start

1. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare data:
   - Put raw files in `Data/raw/`
   - Run preprocessing if needed:

   ```bash
   python src/preprocessing.py
   ```

4. Train a model:

   ```bash
   python src/train.py
   ```

5. Run inference:

   ```bash
   python src/inference.py
   ```

6. (Optional) Start the app/API:

   ```bash
   python src/app.py
   ```

## 🧪 Notebooks

Open and run cells in `Notebooks/Airflight Analysis ML.ipynb` for exploratory analysis and reproducible experiments.
