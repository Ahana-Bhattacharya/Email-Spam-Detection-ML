
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/spambase.csv")

# Dataset information
print("Dataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Spam and non-spam count
print("\nEmail Categories:")
print(df["Class"].value_counts())

# Visualize spam vs non-spam
plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="Class", hue="Class", palette="Set2", legend=False)

plt.title("Spam vs Non-Spam Email Distribution")
plt.xlabel("Email Category (0 = Not Spam, 1 = Spam)")
plt.ylabel("Number of Emails")

plt.savefig("dataset/email_distribution.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(15, 10))

sns.heatmap(
    df.corr(),
    cmap="coolwarm",
    annot=False
)

plt.title("Feature Correlation Heatmap")
plt.savefig("dataset/correlation_heatmap.png")
plt.show()

print("\nEDA completed successfully!")
