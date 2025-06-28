import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure result3 folder exists
os.makedirs("../data/result3", exist_ok=True)

# Load the feature-engineered dataset
data = pd.read_csv("../data/result2/feature_engineered_dataset.csv")

# 1️⃣ Cuisines with the highest average ratings
if "Cuisines" in data.columns and "Aggregate rating" in data.columns:
    cuisines_ratings = data.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
    print("\nTop 10 Cuisines with Highest Average Ratings:")
    print(cuisines_ratings)

    # Plot
    plt.figure(figsize=(10,5))
    cuisines_ratings.plot(kind="bar", color="skyblue")
    plt.title("Top 10 Cuisines with Highest Average Ratings")
    plt.xlabel("Cuisine")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../data/result3/top_10_cuisines_by_rating.png", dpi=300)
    plt.show()
    print("Saved 'top_10_cuisines_by_rating.png' in your result3 folder.")
else:
    print("\nRequired columns for cuisines analysis not found.")

# 2️⃣ Analyze customer preferences using votes and ratings
if "Votes" in data.columns and "Aggregate rating" in data.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(x="Aggregate rating", y="Votes", data=data, alpha=0.5)
    plt.title("Votes vs Aggregate Rating")
    plt.xlabel("Aggregate Rating")
    plt.ylabel("Votes")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../data/result3/votes_vs_rating.png", dpi=300)
    plt.show()
    print("Saved 'votes_vs_rating.png' in your result3 folder.")

    # Correlation check
    correlation = data["Aggregate rating"].corr(data["Votes"])
    print(f"\nCorrelation between Votes and Aggregate Rating: {correlation:.4f}")
else:
    print("\nRequired columns for votes vs rating analysis not found.")
