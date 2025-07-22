# Improved Fraud Detection System

## Project Overview

This project aims to build a robust fraud detection system using two real-world datasets:
- **E-commerce Fraud Data**: Contains user transactions, device/browser info, and fraud labels.
- **Credit Card Fraud Data**: Contains anonymized credit card transactions with fraud labels.

The goal is to explore, preprocess, and analyze these datasets, engineer meaningful features, visualize key patterns, and lay the groundwork for effective fraud detection modeling.

---

## Data Sources

- **E-commerce Fraud Data**: Includes user demographics, transaction times, device/browser info, and fraud labels.
- **Credit Card Fraud Data**: Contains anonymized features (V1–V28), transaction amounts, and fraud labels.

---

## Data Processing & Feature Engineering

- **Cleaning**: Removed duplicate records and corrected data types (e.g., timestamps).
- **Feature Engineering**:
  - For e-commerce data, engineered `time_since_signup` (time between signup and purchase).
  - Explored categorical features like browser, source, and sex for their relationship to fraud.

---

## Exploratory Data Analysis (EDA)

Key findings and visualizations:

### E-commerce Data

- **Class Imbalance**: Only ~9% of transactions are fraudulent.
  - ![Class Distribution](reports/figures/class_distribution.png)
- **Time Since Signup**: Fraudulent users tend to purchase sooner after signup.
  - ![Time Since Signup Distribution](reports/figures/time_since_signup_distribution.png)
- **Purchase Value**: Fraudulent transactions often have higher purchase values.
  - ![Purchase Value by Class](reports/figures/purchase_value_by_class.png)
- **Fraud Rate by Categorical Features**:
  - By browser: ![Fraud Rate by Browser](reports/figures/fraud_rate_by_browser.png)
  - By source: ![Fraud Rate by Source](reports/figures/fraud_rate_by_source.png)
  - By sex: ![Fraud Rate by Sex](reports/figures/fraud_rate_by_sex.png)

### Credit Card Data

- **Class Imbalance**: Only ~0.17% of transactions are fraudulent.
  - ![Credit Card Class Distribution](reports/figures/creditcard_class_distribution.png)
- **Transaction Amount**: Fraudulent transactions show distinct amount patterns.
  - ![Credit Card Amount by Class](reports/figures/creditcard_amount_by_class.png)
- **Anonymized Features**: Certain features (V10, V12, V14, V17) show different distributions for fraud vs. non-fraud.
  - ![V10](reports/figures/creditcard_V10_distribution.png)
  - ![V12](reports/figures/creditcard_V12_distribution.png)
  - ![V14](reports/figures/creditcard_V14_distribution.png)
  - ![V17](reports/figures/creditcard_V17_distribution.png)

---

## Project Structure

```
.
├── data/                  # Raw, intermediate, and processed data
├── notebooks/             # Jupyter notebooks for EDA and preprocessing
├── reports/
│   ├── figures/           # Generated plots
│   └── Interim_1_Report.md
├── src/                   # Source code for data processing, feature engineering, modeling
├── README.md
└── requirements.txt
```

---

## Getting Started

1. **Clone the repository** and set up a virtual environment.
2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Run the notebooks** in the `notebooks/` directory to reproduce the analysis and figures.

---

## Next Steps

- Implement and evaluate machine learning models for fraud detection.
- Perform model interpretation and explainability (see planned notebooks).

---

## Acknowledgements

- Datasets sourced from public repositories for educational purposes.
- Visualizations generated using Matplotlib and Seaborn.
