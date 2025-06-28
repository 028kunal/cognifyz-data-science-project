import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("../data/Dataset.csv")

# 1️⃣ Scatter Plot: Restaurant locations
if "Latitude" in data.columns and "Longitude" in data.columns:
    plt.figure(figsize=(10,6))
    plt.scatter(data["Longitude"], data["Latitude"], alpha=0.3, s=10, c='blue')
    plt.title("Restaurant Locations (Longitude vs Latitude)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../data/result1/restaurant_locations_scatter.png", dpi=300)
    plt.show()
    print("Saved 'restaurant_locations_scatter.png' in your data folder.")
else:
    print("\nLatitude and/or Longitude columns not found in the dataset for plotting.")

# 2️⃣ Analyze distribution across cities
if "City" in data.columns:
    top_cities = data["City"].value_counts().head(10)
    print("\nTop 10 Cities with Most Restaurants:")
    print(top_cities)

    plt.figure(figsize=(10,5))
    sns.barplot(x=top_cities.values, y=top_cities.index, palette="viridis")
    plt.title("Top 10 Cities with Most Restaurants")
    plt.xlabel("Number of Restaurants")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig("../data/result1/top_10_cities_restaurants.png", dpi=300)
    plt.show()
    print("Saved 'top_10_cities_restaurants.png' in your data folder.")
else:
    print("\n'City' column not found for city-wise analysis.")

# 3️⃣ Correlation between location and aggregate rating
if "Aggregate rating" in data.columns and "Latitude" in data.columns and "Longitude" in data.columns:
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Longitude", y="Latitude", hue="Aggregate rating", data=data, palette="cool", alpha=0.6)
    plt.title("Restaurant Locations Colored by Aggregate Rating")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Rating")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../data/result1/restaurant_locations_with_ratings.png", dpi=300)
    plt.show()
    print("Saved 'restaurant_locations_with_ratings.png' in your data folder.")
else:
    print("\nCannot plot correlation as required columns are missing.")
