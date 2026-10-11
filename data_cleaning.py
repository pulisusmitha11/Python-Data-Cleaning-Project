import pandas as pd
import matplotlib.pyplot as plt

# Create sample student data
data = {
    "Name": ["Ravi", "Sita", "Ravi", "Raju", None],
    "Age": [20, 21, 20, None, 22],
    "Marks": [85, 90, 85, 75, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

# Save cleaned data to Excel
df.to_excel("cleaned_data.xlsx", index=False)

# Create marks chart
df.plot(x="Name", y="Marks", kind="bar", legend=False)
plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

print("\nProject completed successfully!")