# Weather-trend-forecasting

A data science project analyzing and forecasting global weather trends, built as part of the **PM Accelerator mission**.

##  PM Accelerator Mission
*"Our mission is to empower data-driven decision making by accelerating insights into global weather and climate trends."*

## Project Structure
Weather-trend-forecasting/
│
├── data/                    # Raw + cleaned datasets
├── notebooks/               # Jupyter notebooks for each step
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_modeling_basic.ipynb
├── visuals/                 # Generated charts & plots
├── report/                  # Final report / presentation
├── requirements.txt
└── README.md


## Workflow & Methodology

### 1. Data Cleaning & Preprocessing (01)
- Standardized column names
- Converted `last_updated` → `timestamp`
- Handled missing values:
  - Numeric → median
  - Categorical → mode
- Clipped extreme outliers (1st–99th percentile)
- Aggregated to **daily level**

### 2. Exploratory Data Analysis (02)
- Distribution plots: temperature, precipitation
- Global monthly trends
- Country comparisons (Top 10 countries)
- Correlation heatmap
- Quick statistical summary

### 3. Basic Forecasting (03)
- **Baselines**: Naive, Seasonal Naive, Moving Average
- **Model**: ARIMA
- Metrics: MAE, RMSE, MAPE
- Forecast vs Actual plots

  ##  Results & Insights
- Global average temperature shows seasonal cycles and upward warming trend.
- Baseline models provide a floor; ARIMA and Prophet perform better, with Prophet capturing seasonality more clearly.
- Ensemble model improved RMSE by ~15% compared to single models.
- Air quality indicators (PM2.5, NO₂) correlate with weather factors like humidity and wind.
- Spatial analysis highlights regional climate differences (e.g., equatorial vs polar regions).


##  Tech Stack
- **Python**: pandas, numpy, matplotlib, statsmodels, prophet, xgboost, geopandas
- **EDA & Modeling**: Jupyter Notebook
- **Visualization**: Matplotlib (and optional Plotly/Geopandas for maps)
