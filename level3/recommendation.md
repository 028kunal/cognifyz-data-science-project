# Recommendations and Insights – Data Science Internship

## Overview

As part of my Data Science Internship with Cognifyz Technologies, I performed comprehensive **exploratory data analysis, feature engineering, and predictive modeling** on a restaurant dataset to derive actionable insights for restaurant business strategy.

The analysis involved cleaning and preparing the dataset, identifying key patterns in customer ratings and preferences, building predictive models to forecast ratings, and visualizing critical metrics for effective decision-making.

---

## Key Insights

### Table Booking
- Only 12% of restaurants in the dataset offer table booking.
- However, restaurants with table booking tend to have significantly higher average ratings (3.44) compared to those without table booking (2.56).
- This indicates that offering table booking may contribute to higher customer satisfaction and perceived service quality.

### Online Delivery
- Only 0.3% of restaurants currently offer online delivery services.
- Restaurants with higher price ranges generally receive better ratings, indicating a potential opportunity for premium restaurants to expand into online delivery and maintain service quality expectations.

### Ratings vs Price
- Restaurants in price ranges 3 and 4 have the highest average ratings (approximately 3.7–3.8), showing a positive relationship between price range and customer satisfaction.
- Most restaurants, however, are in price range 1, which has lower ratings (~2.0), suggesting that while budget-friendly options are common, they may struggle with customer satisfaction.

### Top Cuisines
- Cuisines such as American, Burger, and Seafood consistently receive the highest ratings (4.9), indicating strong customer preferences towards these offerings.
- Restaurants can consider adding or promoting these cuisines to align with customer tastes.

### Predictive Modeling
- A Random Forest Regressor provided the best predictive performance for forecasting restaurant ratings compared to Linear Regression and Decision Trees.
- The Random Forest model achieved the highest R² score of 0.29, indicating it captured the patterns in the dataset moderately well, useful for indicative forecasting.

### Votes vs Ratings
- There is a moderate positive correlation (0.31) between customer votes and aggregate ratings.
- This shows that higher-rated restaurants often receive more customer interactions, but other factors like visibility and marketing likely also play roles.

---

## Recommendations

### Enable Table Booking
Restaurants should consider implementing table booking systems to enhance the customer experience, as data indicates a link between table booking availability and higher ratings.

### Consider Online Delivery Expansion
Restaurants, particularly in the premium and mid-range categories, can explore online delivery to reach new customer segments while maintaining quality, leveraging higher ratings to build trust in online orders.

### Focus on High-Rated Cuisines
Adding or focusing on cuisines with consistently high ratings, such as American and Seafood, can help attract customers and improve the restaurant's overall rating.

### Marketing Strategy
Restaurants can use their high customer ratings as part of their marketing strategies on social media and food delivery platforms to build credibility and attract a larger audience.

### Data-Driven Decisions
Regular analysis of customer ratings, votes, and preferences should be integrated into business decisions, enabling restaurants to adjust their offerings dynamically in response to customer feedback and trends.

---

## Acknowledgment

This analysis was completed as part of the **Cognifyz Data Science Internship**, strengthening my practical skills in:

- Data cleaning and preparation
- Exploratory data analysis and visualization
- Feature engineering for machine learning
- Predictive modeling and evaluation
- Translating data analysis into actionable business strategies
