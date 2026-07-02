# 📊 Digital Onboarding Optimization
### A Product Analytics + Data Science + Lean Six Sigma Case Study

> A complete end-to-end Product Analytics case study built with synthetic data, demonstrating how data-driven experimentation can improve a digital onboarding experience.

---

## 📖 Overview

Digital onboarding is one of the most critical journeys in any digital product. Small UX frictions can dramatically reduce conversion, increase customer support demand, and negatively impact revenue.

This repository presents a **fully anonymized** Product Analytics case study inspired by a real-world digital onboarding optimization initiative.

The project combines **Lean Six Sigma**, **Product Analytics**, **Statistics**, **Experimentation**, and **Business Analytics** to investigate why users abandon the onboarding process and how product improvements can increase conversion.

> **Important**
>
> Every dataset contained in this repository is **100% synthetic** and generated exclusively for portfolio purposes.
>
> No confidential information, customer data, proprietary metrics, screenshots, internal systems, or company references are included.

---

# 🎯 Business Problem

Users can either:

- Upload their identity document immediately
- Postpone the upload

Behavioral analysis indicates that users who postpone document submission are significantly less likely to complete the onboarding journey.

The objective is to identify:

- where users abandon the funnel
- which customer segments are most affected
- the statistical impact of onboarding friction
- the expected business value of improving the experience

---

# 🎯 Project Goals

- Improve onboarding conversion
- Reduce onboarding abandonment
- Increase identity verification completion
- Reduce customer support demand
- Estimate financial impact
- Demonstrate Product Analytics best practices

---

# 📂 Repository Structure

```text
digital-onboarding-case-study/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── onboarding_users.csv
│   ├── events.csv
│   ├── support_calls.csv
│
├── notebooks/
│   ├── 01_Data_Generation.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Funnel_Analysis.ipynb
│   ├── 04_User_Segmentation.ipynb
│   ├── 05_Hypothesis_Testing.ipynb
│   ├── 06_AB_Test.ipynb
│   ├── 07_Financial_Impact.ipynb
│   ├── 08_Dashboard.ipynb
│
├── sql/
│   ├── funnel.sql
│   ├── retention.sql
│   ├── support.sql
│
├── dashboard/
│   └── streamlit_app.py
│
├── docs/
│   ├── Executive_Summary.pdf
│   └── Business_Presentation.pdf
│
└── images/
```

---

# 📊 Synthetic Dataset

The repository contains three synthetic datasets.

## onboarding_users.csv

User-level onboarding information.

Variables include:

- acquisition channel
- device
- region
- customer profile
- onboarding progression
- upload behavior
- approval outcome
- upload time

---

## events.csv

Event-level tracking table representing a modern Product Analytics implementation.

Examples:

- app_opened
- onboarding_started
- personal_data_completed
- document_screen_viewed
- upload_now
- upload_later
- document_submitted
- identity_approved

---

## support_calls.csv

Synthetic customer support interactions generated from onboarding behavior.

Variables include:

- support reason
- handling time
- first-contact resolution
- timestamps

---

# 📈 Analysis Pipeline

## 01 — Data Generation

Generates a realistic synthetic ecosystem including:

- 100,000 users
- 500k+ product events
- support interactions
- behavioral variables
- realistic onboarding outcomes

---

## 02 — Exploratory Data Analysis

- Data Quality Assessment
- KPI Overview
- User Distribution
- Device Analysis
- Channel Analysis
- Regional Analysis
- Correlation Matrix
- Business Insights

---

## 03 — Funnel Analysis

Builds the complete onboarding funnel.

Includes:

- Funnel Conversion
- Drop-off Analysis
- Conversion by Segment
- Funnel Heatmaps
- Behavioral Interpretation

---

## 04 — User Segmentation

Segments users by:

- Channel
- Device
- Region
- Customer Type
- Business Hours
- Document Readiness

Includes an Opportunity Index to prioritize improvements.

---

## 05 — Hypothesis Testing

Statistically validates the business hypothesis.

Methods include:

- Two-Proportion Z-Test
- Chi-Square Test
- Odds Ratio
- Confidence Intervals
- Effect Size

---

## 06 — A/B Test

Designs and simulates a controlled experiment.

Includes:

- Sample Size Calculation
- MDE
- Experiment Simulation
- Statistical Validation
- Business Interpretation

---

## 07 — Financial Impact

Business simulation estimating:

- Additional approved users
- Support cost reduction
- Incremental revenue
- ROI
- Payback
- Sensitivity Analysis

---

## 08 — Dashboard

Interactive dashboard prototype.

Includes:

- KPI Cards
- Funnel Dashboard
- Channel Performance
- Monthly Trends
- Segment Analysis

A complete Streamlit application is also included.

---

# 🧠 Business Questions

The project answers questions such as:

- Where do users abandon onboarding?
- Does postponing document upload reduce conversion?
- Which acquisition channels generate the best users?
- Which customer segments generate more support calls?
- What is the expected ROI of improving onboarding?
- Is the improvement statistically significant?
- Should the company launch an A/B test?

---

# 🛠 Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels
- Jupyter Notebook
- Streamlit
- SQL

---

# 📚 Analytics Techniques

- Product Analytics
- Funnel Analysis
- Behavioral Analytics
- User Segmentation
- Statistical Testing
- A/B Testing
- Financial Simulation
- KPI Design
- Business Storytelling
- Lean Six Sigma (DMAIC)

---

# 📄 Documentation

The repository also includes:

- Executive Summary (PDF)
- Business Presentation (PDF)
- SQL examples
- Interactive dashboard
- Complete notebook documentation

---

# ⚠ Disclaimer

This repository was developed exclusively for educational and portfolio purposes.

All datasets are artificially generated and do not represent any real company, customer, product, employee, business rule, or operational metric.

Any resemblance to real-world products or organizations is purely coincidental.
