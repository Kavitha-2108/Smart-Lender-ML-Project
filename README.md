---

## 📊 Machine Learning Model

The Smart Lender application uses an **XGBoost Classifier** trained on historical loan application data to predict whether a loan should be approved or rejected.

### Input Features

The prediction is based on the following applicant details:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-Applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

### Prediction Output

After submitting the application, the system displays:

- ✅ Loan Approved
- ❌ Loan Rejected
- 📈 Approval Confidence (%)
- 📉 Rejection Risk (%)

The confidence scores help users understand how confident the machine learning model is about its prediction.

---

## 📷 Project Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 📋 Loan Application Form

![Prediction Form](screenshots/prediction.png)

---

### ✅ Loan Approved

Displays the loan approval status along with the approval confidence and rejection risk.

![Approved](screenshots/approved.png)

---

### ❌ Loan Rejected

Displays the loan rejection status along with the approval confidence and rejection risk.

![Rejected](screenshots/rejected.png)

---
