
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_spambase.csv")

# Create dataset folder if needed
os.makedirs("dataset", exist_ok=True)

# Spam distribution
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Class",
    hue="Class",
    palette="Set2",
    legend=False
)

plt.title("Spam vs Not Spam Distribution")
plt.xlabel("Email Class (0 = Not Spam, 1 = Spam)")
plt.ylabel("Number of Emails")

plt.tight_layout()

# Save graph
plt.savefig("dataset/spam_distribution.png")

print("Visualization created successfully!")
print("Graph saved at dataset/spam_distribution.png")

# Close graph without opening a window
plt.close()
