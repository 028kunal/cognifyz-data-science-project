import pandas as pd

# Load the dataset
data = pd.read_csv("../data/Dataset.csv")

# Display first few rows, shape, columns, datatypes, and missing values
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

print("\nShape of the Dataset (Rows, Columns):", data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nData Types of Each Column:")
print(data.dtypes)

print("\nMissing Values in Each Column:")
print(data.isnull().sum())

if "Aggregate rating" in data.columns:
    print("\nStatistics for 'Aggregate rating' Column:")
    print(data["Aggregate rating"].describe())

    print("\nValue Counts for 'Aggregate rating' Column:")
    print(data["Aggregate rating"].value_counts())
else:
    print("\n'Aggregate rating' column not found in the dataset.")



import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Handle Missing Values

print("\nMissing Values Before Handling:")
print(data.isnull().sum())

# Fill missing numerical columns with mean, categorical with mode
for column in data.columns:
    if data[column].isnull().sum() > 0:
        if data[column].dtype == 'object':
            mode_value = data[column].mode()[0]
            data[column].fillna(mode_value, inplace=True)
            print(f"Filled missing values in '{column}' with mode: {mode_value}")
        else:
            mean_value = data[column].mean()
            data[column].fillna(mean_value, inplace=True)
            print(f"Filled missing values in '{column}' with mean: {mean_value}")

print("\nMissing Values After Handling:")
print(data.isnull().sum())

# 2️⃣ Check Data Types
print("\nData Types After Preprocessing:")
print(data.dtypes)

# 3️⃣ Visualize 'Aggregate rating'
if "Aggregate rating" in data.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(data["Aggregate rating"], bins=20, kde=True)
    plt.title("Distribution of Aggregate Rating")
    plt.xlabel("Aggregate Rating")
    plt.ylabel("Frequency")
    plt.grid(True)
    # Save the figure before showing
    plt.savefig("../data/result1/aggregate_rating_distribution.png", dpi=300, bbox_inches='tight')

# Show the plot
    plt.show()

    print("Plot saved as 'aggregate_rating_distribution.png' inside your 'data' folder.")

else:
    print("\n'Aggregate rating' column not found for visualization.")
