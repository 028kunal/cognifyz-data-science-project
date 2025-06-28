import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure result2 folder exists
os.makedirs("../data/result2", exist_ok=True)

# Load dataset
data = pd.read_csv("../data/Dataset.csv")

# 1️⃣ Table booking percentage
if "Has Table booking" in data.columns:
    table_booking_counts = data["Has Table booking"].value_counts()
    print("\nTable Booking Counts:")
    print(table_booking_counts)

    table_booking_percentage = (table_booking_counts / len(data)) * 100
    print("\nTable Booking Percentage:")
    print(table_booking_percentage)
else:
    print("\nColumn 'Has Table booking' not found in dataset.")

# 1️⃣ Online delivery percentage
if "Is delivering now" in data.columns:
    online_delivery_counts = data["Is delivering now"].value_counts()
    print("\nOnline Delivery Counts:")
    print(online_delivery_counts)

    online_delivery_percentage = (online_delivery_counts / len(data)) * 100
    print("\nOnline Delivery Percentage:")
    print(online_delivery_percentage)
else:
    print("\nColumn 'Is delivering now' not found in dataset.")

# 2️⃣ Compare average ratings with/without table booking
if "Has Table booking" in data.columns and "Aggregate rating" in data.columns:
    avg_rating_table_booking = data[data["Has Table booking"] == "Yes"]["Aggregate rating"].mean()
    avg_rating_no_table_booking = data[data["Has Table booking"] == "No"]["Aggregate rating"].mean()

    print(f"\nAverage Rating (Table Booking): {avg_rating_table_booking:.2f}")
    print(f"Average Rating (No Table Booking): {avg_rating_no_table_booking:.2f}")

    plt.figure(figsize=(6,4))
    plt.bar(["Table Booking", "No Table Booking"], [avg_rating_table_booking, avg_rating_no_table_booking], color=["skyblue", "lightgreen"])
    plt.title("Average Ratings: Table Booking vs No Table Booking")
    plt.ylabel("Average Aggregate Rating")
    plt.tight_layout()
    plt.savefig("../data/result2/table_booking_vs_rating.png", dpi=300)
    plt.show()
    print("Saved 'table_booking_vs_rating.png' in your result2 folder.")
else:
    print("\nRequired columns for average rating comparison not found.")

# 3️⃣ Online delivery availability across price ranges
if "Price range" in data.columns and "Is delivering now" in data.columns:
    delivery_price_group = data.groupby("Price range")["Is delivering now"].value_counts().unstack().fillna(0)
    print("\nOnline Delivery Availability Across Price Ranges:")
    print(delivery_price_group)

    delivery_price_group.plot(kind="bar", stacked=True, figsize=(8,5), colormap="tab20")
    plt.title("Online Delivery Across Different Price Ranges")
    plt.xlabel("Price Range")
    plt.ylabel("Number of Restaurants")
    plt.legend(title="Is Delivering Now")
    plt.tight_layout()
    plt.savefig("../data/result2/online_delivery_vs_price_range.png", dpi=300)
    plt.show()
    print("Saved 'online_delivery_vs_price_range.png' in your result2 folder.")
else:
    print("\nRequired columns for price range vs online delivery analysis not found.")
