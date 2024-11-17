# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv('../data/raw/your_data.csv')
df.head()

# Save processed data
# df.to_csv('../data/processed/processed_data.csv', index=False)