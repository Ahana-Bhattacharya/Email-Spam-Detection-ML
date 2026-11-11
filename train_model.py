
import pandas as pd
import os
from ucimlrepo import fetch_ucirepo

# Fetch Spambase dataset
print("Loading dataset...")

spambase = fetch_ucirepo(id=94)

# Get input features
X = spambase.data.features

# Get output labels
y = spambase.data.targets

# Combine features and labels
df = pd.concat([X, y], axis=1)

# Display dataset
print("\nFirst 5 rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display spam and non-spam counts
target = y.columns[0]

print("\nEmail Categories:")
print(df[target].value_counts())

# Create dataset folder if it doesn't exist
os.makedirs("dataset", exist_ok=True)

# Save dataset
df.to_csv("dataset/spambase.csv", index=False)

print("\nDataset saved successfully!")
