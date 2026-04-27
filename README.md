# 📊 Customer Retention and Churn Analysis
### Data Science & Analytics Internship Task 2 — Future Interns 2026

---

## 👤 Author
**Khethani Mugeri**  

---

## 📌 Project Overview

This project presents a full customer churn and retention analysis for a 
telecommunications company.

The goal is to answer real business questions such as:
- Why are customers leaving the platform?
- Which customer segments are most likely to churn?
- How long do customers typically stay active?
- What actions can improve customer retention?

---

## 📁 Project Structure
---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core analysis and visualisation |
| Pandas | Data loading, cleaning, and analysis |
| Matplotlib | Dashboard layout and chart creation |
| Anaconda / Spyder | Development environment |
| LaTeX (Overleaf) | Professional report writing |

---

## 📊 Dataset

**Telco Customer Churn Dataset**  
Source: [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

| Feature | Detail |
|---------|--------|
| Rows | 7,043 |
| Churned Customers | 1,869 |
| Churn Rate | 26.54% |
| Total Revenue | $16,056,168.70 |
| Churned Revenue | $2,862,926.90 |
| Key Columns | CustomerID, Contract, PaymentMethod, InternetService, Tenure, MonthlyCharges, TotalCharges, Churn |

---

## 🔍 Analysis Performed

### ✅ Stage 1 — Data Loading & Preparation
- Loaded CSV using Pandas
- Fixed TotalCharges column (converted to numeric)
- Created Senior Citizen label (0/1 to Non-Senior/Senior)

### ✅ Stage 2 — KPI Calculation
- Total customers, churned customers, churn rate
- Retention rate
- Total revenue and churned revenue

### ✅ Stage 3 — Churn Analysis
- Churn rate by contract type
- Churn rate by payment method
- Churn rate by internet service
- Churn rate by senior citizen status
- Churn rate by tenure (monthly breakdown)
- Overall churn distribution

### ✅ Stage 4 — Dashboard & Visualisation
- 6 KPI cards (Total Customers, Churned, Churn Rate, Retention Rate, Total Revenue, Churned Revenue)
- 6-panel professional dashboard
- Saved as high-resolution pdf

---

## 📈 Key Findings

| Area | Finding | Value |
|------|---------|-------|
| Overall Churn Rate | Above industry benchmark | 26.54% |
| Retention Rate | Customers retained | 73.46% |
| Highest Churn Segment | Month-to-month contracts | 42.71% |
| Lowest Churn Segment | Two-year contracts | 2.83% |
| Riskiest Payment Method | Electronic check | 45.29% |
| Safest Payment Method | Credit card (automatic) | 15.24% |
| Highest Churn Service | Fiber optic internet | 41.89% |
| Senior Citizen Churn | Nearly double non-senior | 41.68% |
| Highest Risk Period | Early tenure | Months 1–5 |
| Revenue Lost to Churn | Churned customer revenue | $2,862,926.90 |

---

## 💡 Business Recommendations

1. 🔵 **Incentivise Long-Term Contracts** — Month-to-month customers churn ore than two-year customers
2. 🔵 **Promote Automatic Payments** — Electronic check users churn at 45.29% vs 15.24% for auto-pay
3. 🔵 **Invest in Early Onboarding** — Churn is highest in the first 1–5 months of tenure
4. 🔵 **Investigate Fiber Optic Quality** — Premium service with highest churn suggests unmet expectations
5. 🔵 **Senior Customer Retention Programme** — Senior citizens churn at nearly double the non-senior rate
6. 🔴 **Prioritise Retention Over Acquisition** — $2.86M lost to churn; retaining customers is 5 times cheaper than acquiring new ones

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/telco-churn-analysis.git
```

2. Install dependencies:
```bash
conda install pandas matplotlib numpy
```

3. Place `Telco_Customer_Churn.csv` in the project folder and update the path:
```python
df = pd.read_csv(r'C:\Anaconda3\Churn Analysis\Telco_Customer_Churn.csv')
```

4. Run the analysis:
```bash
Churn Analysis code.py
```

5. The dashboard will be saved as `Churn_Dashboard.pdf`

---

## 📜 License
This project was completed as part of the Future Interns Data Science Internship Programme 2026.

---
