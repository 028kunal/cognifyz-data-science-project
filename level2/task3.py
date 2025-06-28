import pandas as pd
import os

# Ensure result2 folder exists
os.makedirs("../data/result2", exist_ok=True)

# Load dataset
data = pd.read_csv("../data/Dataset.csv")

# 1️⃣ Create new features

# Feature: Restaurant Name Length
if "Restaurant Name" in data.columns:
    data["Restaurant Name Length"] = data["Restaurant Name"].astype(str).apply(len)
    print("\nFeature 'Restaurant Name Length' created.")
else:
    print("\n'Restaurant Name' column not found for feature creation.")

# Feature: High Rating Indicator (1 if rating >= 4, else 0)
if "Aggregate rating" in data.columns:
    data["High Rating"] = data["Aggregate rating"].apply(lambda x: 1 if x >= 4 else 0)
    print("Feature 'High Rating' created.")
else:
    print("'Aggregate rating' column not found for feature creation.")

# Feature: Price Category Label
if "Price range" in data.columns:
    def price_label(x):
        if x == 1:
            return "Budget"
        elif x == 2:
            return "Mid-Range"
        elif x == 3:
            return "Premium"
        else:
            return "Luxury"
    data["Price Category"] = data["Price range"].apply(price_label)
    print("Feature 'Price Category' created.")
else:
    print("'Price range' column not found for feature creation.")

# 2️⃣ Encode categorical columns

# Encode 'Has Table booking'
if "Has Table booking" in data.columns:
    data["Has Table booking Encoded"] = data["Has Table booking"].map({"Yes": 1, "No": 0})
    print("Encoded 'Has Table booking' to numeric.")
else:
    print("'Has Table booking' column not found for encoding.")

# Encode 'Is delivering now'
if "Is delivering now" in data.columns:
    data["Is delivering now Encoded"] = data["Is delivering now"].map({"Yes": 1, "No": 0})
    print("Encoded 'Is delivering now' to numeric.")
else:
    print("'Is delivering now' column not found for encoding.")

# 3️⃣ Save the cleaned, feature-engineered dataset
output_path = "../data/result2/feature_engineered_dataset.csv"
data.to_csv(output_path, index=False)
print(f"\nFeature-engineered dataset saved as '{output_path}' for Level 3 modeling.")
