# Project 1 **Urban Risk Analysis**


├── Business Problem

            ├── Context
            └── Defining, Solving, Improving

├── Data Pipeline

            ├── ETL (Extract Transform Load)

                        ├── Data Collection (Extract) — raw data into a tabular dataset:

                            ├── (Internal) Business Databases - from the company (mostly structured).
                            ├── (External) API Requests - from online APIs in JSON/CSV (unstructured).
                            └── (External) Web Scraping - from websites in HTML (unstructured).

                        ├── Data Wrangling (Transform) - tabular dataset into a clean, standardized, labeled structure.

                            ├── Familiarization — understand dataset.
                                ├── Dataset Exploration
                                ├── Dataset Glossary — define features' meanings.
                                └── Descriptive Statistics
                                    ├── Continuous Variables — numeric columns.
                                    └── Categorical Variables — non-numeric columns.

                            ├── Identifying → Correcting - detect and fix issues, skewed distributions.
                                ├── Bias in Data Collection — check class imbalances.
                                ├── Incomplete Data - handle missing values.
                                ├── Merging Datasets - join external complimentary data.
                                └── Formatting Datasets - normalize datatypes and formats.
                            
                            └── Training Labels — convert verbose into binary target.

                        └── Load - transformed dataset.

            └── EDA (Exploratory Data Analysis) - analyzed patterns between features and targets.

                        ├── Plot - visualize relationships between features and targets.
                        ├── Features Engineering - prepare dataset for modeling.
                        └── SQL - run structured queries on the Dataset for exploration and validation.

├── Data Visualization

├── Hypothesis
      
            └── Hypothesis Testing
  
├── Analysis
            
            └── Machine Learning

                ├── Supervised Learning            
                          ├── Linear Regression
                          ├── Stratified Analysis
                          ├── Interaction Terms
                          ├── Time Series Forecasting
                          ├── Logistic Regression
                          └── Advanced Learning
                                ├── CART
                                      └── Random Forest
                                ├── LASSO
                                └── Neural Networks

                └── Model Evaluating
                            ├── Confusion Matrix
                            ├── Accuracy / Precision / Recall / F1
                            └── Log Loss

└── Results

            └── Business Recommendation
