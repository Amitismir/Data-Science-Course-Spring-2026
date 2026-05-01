# 🚗 Automobile Price Analysis — Feature Engineering & PCA

This assignment analyzes an automobile dataset to understand how technical and design features relate to **car price**, using a full ML-preprocessing pipeline:

- Data cleaning & visualization  
- Feature engineering (ratios, transformations, aggregations)  
- Feature selection (Mutual Information)  
- Dimensionality reduction (PCA)  
- Interpretation and visualization

---

## 🔍 Main Steps

1. **Exploratory Analysis**
   - Boxplots of price by body style and cylinders  
   - Line and bar charts for engine size, mpg, and price  

2. **Feature Engineering**
   - Ratio features: `hp_per_weight`, `compression_per_engine`, etc.  
   - Simple transforms: `log`, `sqrt`, and binning (e.g. engine size categories)  
   - Aggregations: `avg_hp_by_body_style`, `avg_engine_size_by_make`, `count_per_make`  
   - All features are built **only from inputs** (no target leakage from `price`).

3. **Preprocessing**
   - One-hot encoding for categorical variables  
   - Standardization of numeric features  

4. **Feature Selection**
   - **Mutual Information** to rank features by relevance to `price`  
   - Selection of the top features for modeling and PCA  

5. **PCA & Interpretation**
   - PCA on selected features  
   - ~95–97% of variance captured in the first 3 components  
   - Interpretation:
     - **PC1**: performance / size (hp, engine size, weight)  
     - **PC2**: fuel efficiency (mpg)  
     - **PC3**: weight–power balance  
   - 3D PCA scatter plot colored by price shows:
     - clusters of economy cars  
     - high‑performance, high‑price cars as outliers along PC1

---

## 🧠 Key Takeaways

- Thoughtful **feature engineering** is crucial for tabular problems:
  - *Nice to have* when raw features are already descriptive or using powerful non-linear models.
  - *Must have* when important relationships (e.g. power‑to‑weight) are not explicit, or when using linear / distance-based models.
- **PCA** helps reduce redundancy and reveals meaningful latent dimensions (performance, efficiency, size) that structure the automobile market.

---

## 🛠️ Tech Stack

- Python, Jupyter Notebook  
- `pandas`, `numpy`  
- `seaborn`, `matplotlib`  
- `scikit-learn` (StandardScaler, mutual_info_regression, PCA)

---

Amitis Mirabedini  
Electrical Engineering Undergraduate at Sharif University of Technology
