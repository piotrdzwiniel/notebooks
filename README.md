## Bioinformatics

### Notebooks

1. [Risk Factors for Heart Disease on AI-Generated Data](#risk-factors-for-heart-disease-on-ai-generated-data)

---

### Risk Factors for Heart Disease on AI-Generated Data

The [notebook](https://github.com/piotrdzwiniel/notebooks/blob/master/bioinformatics/risk_factors_for_heart_disease_on_ai_data.ipynb)
titled **risk_factors_for_heart_disease_on_ai_data** explores the associations
between various risk factors and the likelihood of developing heart disease. The data used in
this notebook was generated using AI, providing a synthetic dataset that mimics real-world
clinical data.

#### Data

The dataset contains several features commonly linked to heart disease, such as age, sex,
resting blood pressure, serum cholesterol levels, chest pain type, fasting blood sugar, and
heart disease diagnosis. These features are analyzed to identify key risk factors for heart
disease.

#### Techniques Used

The notebook employs a variety of techniques, including:

- **Exploratory Data Analysis (EDA)** to understand the distribution of continuous variables
  like age, resting blood pressure, and serum cholesterol, as well as the frequency of
  qualitative variables such as sex, chest pain type, and fasting blood sugar.
- **Statistical inference** methods, such as the chi-square test of independence, are used to
  examine potential associations between sex and other categorical variables.
- **Logistic regression models** are built to predict the likelihood of heart disease based on
  combinations of variables like age, serum cholesterol, and resting blood pressure.

#### Findings

Key findings from the analysis include:

- Significant differences in the distribution of risk factors between males and females.
- Strong associations between heart disease diagnosis and features such as age, serum
  cholesterol, and resting blood pressure.
- The logistic regression model achieved reasonable accuracy in predicting heart disease risk,
  and precision and recall metrics were calculated to assess the model's performance.

Overall, this notebook provides a comprehensive analysis of heart disease risk factors using
AI-generated data, offering insights into how these factors interplay in predicting the
likelihood of developing heart disease.

