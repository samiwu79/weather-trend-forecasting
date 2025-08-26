import pandas as pd
import numpy as np
from pathlib import Path

RAW = Path("data/GlobalWeatherRepository.csv")
CLEAN = Path("data/cleaned_weather.csv")

sample = pd.read_csv(RAW, nrows=5, low_memory=False)
display(sample.head())
print("Columns (first 20):",list(sample.columns)[:20],"...")

df = pd.read_csv(RAW, low_memory=False)
df.shape, df.columns.tolist()[:20]
