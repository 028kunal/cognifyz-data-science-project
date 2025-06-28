# Task 2 File
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("../data/Dataset.csv")

# 1️⃣ Basic Statistical Measures for Numerical Columns
print("\nBasic Statistical Measures using describe():")
print(data.describe())

# Computing mean, median, std for each numerical column
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

print("\nMean of numerical columns:")
print(data[numerical_cols].mean())

print("\nMedian of numerical columns:")
print(data[numerical_cols].median())

print("\nStandard Deviation of numerical columns:")
print(data[numerical_cols].std())

# 2️⃣ Explore Categorical Variables: Country Code, City, Cuisines
categorical_cols = ["Country Code", "City", "Cuisines"]

for col in categorical_cols:
    if col in data.columns:
        print(f"\nValue counts for '{col}':")
        print(data[col].value_counts().head(10))  # top 10 for brevity
    else:
        print(f"\nColumn '{col}' not found in dataset.")

# 3️⃣ Top Cuisines with the highest number of restaurants
if "Cuisines" in data.columns:
    top_cuisines = data["Cuisines"].value_counts().head(10)
    print("\nTop 10 Cuisines with the highest number of restaurants:")
    print(top_cuisines)

    # Plotting top cuisines
    plt.figure(figsize=(10,5))
    top_cuisines.plot(kind='bar')
    plt.title("Top 10 Cuisines by Number of Restaurants")
    plt.xlabel("Cuisines")
    plt.ylabel("Number of Restaurants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../data/result1/top_10_cuisines.png", dpi=300)
    plt.show()
    print("Saved plot as 'top_10_cuisines.png' in your 'data' folder.")
else:
    print("\n'Cuisines' column not found for analysis.")

# 4️⃣ Top Cities with the highest number of restaurants
if "City" in data.columns:
    top_cities = data["City"].value_counts().head(10)
    print("\nTop 10 Cities with the highest number of restaurants:")
    print(top_cities)

    # Plotting top cities
    plt.figure(figsize=(10,5))
    top_cities.plot(kind='bar', color='orange')
    plt.title("Top 10 Cities by Number of Restaurants")
    plt.xlabel("City")
    plt.ylabel("Number of Restaurants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../data/result1/top_10_cities.png", dpi=300)
    plt.show()
    print("Saved plot as 'top_10_cities.png' in your 'data' folder.")
else:
    print("\n'City' column not found for analysis.")
