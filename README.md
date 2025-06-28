# 🍽️ Restaurant Rating Analysis – Cognifyz Data Science Internship

![Project Status](https://img.shields.io/badge/status-completed-brightgreen)


## 📌 Project Overview

This repository contains my **end-to-end Data Science Internship Project with Cognifyz Technologies**, where I performed:

✅ **Data Cleaning & Preprocessing**  
✅ **Exploratory Data Analysis (EDA)**  
✅ **Feature Engineering**  
✅ **Predictive Modeling using Machine Learning**  
✅ **Actionable Business Recommendations**

The project analyzes a restaurant dataset to derive insights on customer ratings, pricing strategies, cuisines, and customer preferences while building predictive models to forecast restaurant ratings.

---

## 🚀 Objectives

- Understand **factors influencing restaurant ratings**.
- Identify **top cuisines and optimal price ranges** for better customer satisfaction.
- Build **predictive models (Linear Regression, Decision Tree, Random Forest)** to forecast restaurant ratings.
- Provide **data-driven recommendations** for restaurants to improve customer engagement and business growth.

---

## 🛠️ Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn)
- **Git & GitHub** for version control and project management
- **Markdown** for clean documentation

---

## 📊 Project Structure

📁 data/
📁 result1/ → Level 1 plots
📁 result2/ → Level 2 plots & feature-engineered dataset
📁 result3/ → Level 3 model evaluation and customer preference plots

📁 level1/ → Data cleaning and EDA scripts
📁 level2/ → Descriptive analysis, price analysis, feature engineering
📁 level3/ → Predictive modeling, customer preference analysis

📄 recommendations.md → Key insights and business recommendations
📄 README.md → Project overview and documentation


---

## 📈 Key Insights

- **Table Booking**:
  - Only 12% of restaurants offer table booking, but these have higher ratings (3.44 vs 2.56).
- **Online Delivery**:
  - Only 0.3% offer online delivery; higher price ranges show potential for premium delivery.
- **Pricing & Ratings**:
  - Higher price ranges (3 & 4) correlate with better ratings (~3.7–3.8).
- **Top Cuisines**:
  - American, Burger, and Seafood cuisines receive the highest ratings (4.9).
- **Predictive Modeling**:
  - Random Forest achieved the best predictive performance (R² = 0.29).
- **Votes vs Ratings**:
  - A moderate positive correlation (0.31) suggests higher-rated restaurants receive more customer engagement.

---

## 🤖 Machine Learning

Trained **Linear Regression, Decision Tree, and Random Forest models** to predict restaurant ratings using engineered features:
- Restaurant Name Length
- High Rating Indicator
- Price Range
- Table Booking & Delivery Encoded Flags

**Random Forest performed best**, capturing non-linear patterns in the data.

---

## 📌 Recommendations

- Enable **table booking** to improve customer satisfaction and ratings.
- Consider **online delivery expansion** for premium and mid-range restaurants.
- Focus on **high-rated cuisines** for menu alignment.
- Leverage **high ratings in marketing** for credibility.
- Use **data-driven decisions** to adjust strategies dynamically.

For detailed recommendations, refer to [`recommendations.md`](./recommendations.md).

---

## 🏆 Acknowledgment

This project was completed as part of the **Cognifyz Data Science Internship**, strengthening my practical skills in:

- Data Cleaning and EDA
- Feature Engineering
- Predictive Modeling
- Business Insight Generation
- Clean, structured workflow using Git and GitHub

---

## 📌 How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/028kunal/cognifyz-data-science-project.git
cd cognifyz-data-science-project
pip install pandas matplotlib seaborn scikit-learn

cd level1
python task1.py
python task2.py
python task3.py

cd ../level2
python task1.py
python task2.py
python task3.py

cd ../level3
python task1.py
python task2.py

Visual outputs will be saved in data/result1/, data/result2/, data/result3/.
