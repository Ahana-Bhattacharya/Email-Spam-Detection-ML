
import pandas as pd

print("Loading dataset...")

df = pd.read_csv("dataset/spambase.csv")

print("Original dataset shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum().sum())

# Separate features and target
X = df.drop("Class", axis=1)
y = df["Class"]

print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)

# Save cleaned dataset
df.to_csv("dataset/cleaned_spambase.csv", index=False)

print("\nCleaned dataset saved successfully!")
