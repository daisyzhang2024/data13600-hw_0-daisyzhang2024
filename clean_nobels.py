import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('nobel-prize-laureates.csv')

# Just want awardYear, category, and name columns
df = df[['awardYear', 'category', 'name']]

# Save as same CSV file
df.to_csv('nobel-prize-laureates.csv', index=False)