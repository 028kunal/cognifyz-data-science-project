import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

# Ensure result3 folder exists
os.makedirs("../data/result3", exist_ok=True)

# Load the feature-engineered dataset
data = pd.read_csv("../data/result2/feature_engineered_dataset.csv")

# Check available columns
print("\nAvailable Columns:")
print(data.columns)

# 1️⃣ Select features and target
features = [
    "Restaurant Name Length",
    "High Rating",
    "Price range",
    "Has Table booking Encoded",
    "Is delivering now Encoded"
]

target = "Aggregate rating"

# Drop rows with missing target values if any
data = data.dropna(subset=[target])

X = data[features]
y = data[target]

# 2️⃣ Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3️⃣ Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}

# 4️⃣ Train, predict, and evaluate each model
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results[name] = {"MSE": mse, "R2 Score": r2}

    print(f"\nModel: {name}")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    # Visualization: Predicted vs Actual
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='teal')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Ratings")
    plt.ylabel("Predicted Ratings")
    plt.title(f"Actual vs Predicted Ratings - {name}")
    plt.tight_layout()
    plt.savefig(f"../data/result3/{name.replace(' ', '_').lower()}_pred_vs_actual.png", dpi=300)
    plt.show()
    print(f"Saved '{name}_pred_vs_actual.png' in your result3 folder.")

# Save evaluation results to CSV for documentation
results_df = pd.DataFrame(results).T
results_df.to_csv("../data/result3/model_evaluation_results.csv")
print("\nModel evaluation results saved in 'model_evaluation_results.csv' in your result3 folder.")
