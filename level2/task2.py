import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure result2 folder exists
os.makedirs("../data/result2", exist_ok=True)

# Load dataset
data = pd.read_csv("../data/Dataset.csv")

# 1️⃣ Most common price range
if "Price range" in data.columns:
    price_counts = data["Price range"].value_counts()
    most_common_price_range = price_counts.idxmax()
    print(f"\nMost Common Price Range: {most_common_price_range} with {price_counts.max()} restaurants")
else:
    print("\nColumn 'Price range' not found in dataset.")

# 2️⃣ Average rating for each price range
if "Price range" in data.columns and "Aggregate rating" in data.columns:
    avg_rating_per_price = data.groupby("Price range")["Aggregate rating"].mean().sort_index()
    print("\nAverage Rating for Each Price Range:")
    print(avg_rating_per_price)

    # Plotting
    plt.figure(figsize=(8,5))
    avg_rating_per_price.plot(kind="bar", color="lightblue")
    plt.title("Average Aggregate Rating Across Price Ranges")
    plt.xlabel("Price Range")
    plt.ylabel("Average Aggregate Rating")
    plt.tight_layout()
    plt.savefig("../data/result2/avg_rating_per_price_range.png", dpi=300)
    plt.show()
    print("Saved 'avg_rating_per_price_range.png' in your result2 folder.")
else:
    print("\nRequired columns for price range rating analysis not found.")

# 3️⃣ Identify the color with the highest average rating
if "Rating color" in data.columns and "Price range" in data.columns and "Aggregate rating" in data.columns:
    avg_rating_color = data.groupby("Rating color")["Aggregate rating"].mean()
    top_color = avg_rating_color.idxmax()
    top_color_value = avg_rating_color.max()
    print(f"\nRating Color with Highest Average Rating: {top_color} ({top_color_value:.2f})")

    # Optional: visualize
    plt.figure(figsize=(8,5))
    avg_rating_color.sort_values().plot(kind="bar", color="salmon")
    plt.title("Average Aggregate Rating by Rating Color")
    plt.xlabel("Rating Color")
    plt.ylabel("Average Aggregate Rating")
    plt.tight_layout()
    plt.savefig("../data/result2/avg_rating_by_color.png", dpi=300)
    plt.show()
    print("Saved 'avg_rating_by_color.png' in your result2 folder.")
else:
    print("\n'Rating color' or required columns not found for color analysis.")
