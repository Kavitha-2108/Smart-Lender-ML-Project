# 🏦 Smart Lender – AI-Powered Loan Approval Prediction

Smart Lender is an AI-powered web application that predicts whether a loan application is likely to be **Approved** or **Rejected** using Machine Learning. The application is built using **Python, Flask, XGBoost, and Scikit-learn**, providing a simple, fast, and user-friendly interface for loan eligibility prediction.

---

# 🌐 Live Application

https://smart-lender-ml-project.onrender.com

---

# 🎥 Demo Video

https://drive.google.com/file/d/1fUuPdI_bI1_qs9hF-lbvRaZO6vtQJEuC/view?usp=drive_link

---

# 📂 GitHub Repository

https://github.com/Kavitha-2108/Smart-Lender-ML-Project

---

# 📌 Project Overview

Smart Lender is a Machine Learning-based loan approval prediction system designed to assist banks and financial institutions in evaluating loan applications. Users provide applicant details through an interactive web interface, and the trained XGBoost model predicts whether the loan application is likely to be approved or rejected.

The application demonstrates the integration of Machine Learning with web technologies to provide real-time predictions.

---

# ✨ Features

- 🤖 AI-powered loan approval prediction
- 🌐 User-friendly Flask web application
- 📊 Machine Learning model using XGBoost
- ⚡ Real-time prediction results
- 💾 Trained model stored using Joblib
- 🎨 Responsive and attractive user interface
- 📈 Fast and accurate loan eligibility prediction
- ☁️ Deployed on Render

---

# 🛠 Technologies Used

### Programming Language
- Python

### Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Web Development
- Flask
- HTML5
- CSS3
- JavaScript

### Deployment
- Render
- Git
- GitHub

---

# 📂 Project Structure

```text
Smart-Lender-ML-Project/
│
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
│   │
│   ├── models/
│   │   ├── label_encoders.pkl
│   │   └── xgboost_model.pkl
│   │
│   ├── static/
│   │   ├── bank.jpg
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── app.py
│   ├── train_model.py
│   ├── loan_prediction.csv
│   └── requirements.txt
│
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
│
├── screenshots/
├── Procfile
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Kavitha-2108/Smart-Lender-ML-Project.git
```

---

## 2. Navigate to the Project Folder

```bash
cd Smart-Lender-ML-Project
cd "5. Project Development Phase"
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Flask Application

```bash
python app.py
```

---

## 5. Open in Browser

```
http://127.0.0.1:5000
```

---

# 🔄 Project Workflow

1. User enters applicant details through the web interface.
2. Flask receives and validates the input.
3. The trained XGBoost model processes the applicant data.
4. The model predicts whether the loan will be approved or rejected.
5. The prediction result is displayed instantly to the user.

---

# 📊 Machine Learning Model

The Smart Lender application uses the **XGBoost Classifier** for loan approval prediction.

### Data Preprocessing

- Handling missing values
- Label Encoding for categorical variables
- Feature preparation
- Model training using historical loan data

The trained model and label encoders are saved as:

- `xgboost_model.pkl`
- `label_encoders.pkl`

These files are loaded by the Flask application to provide real-time predictions.

---

# 📋 Input Features

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

---

# 📈 Prediction Output

- ✅ Loan Approved
- ❌ Loan Rejected

---

# 🚀 Deployment

The application is deployed using **Render**.

Live Application:

https://smart-lender-ml-project.onrender.com/

---

# 🚀 Future Enhancements

- User Authentication
- Database Integration
- Loan History Management
- Admin Dashboard
- Email Notifications
- PDF Report Generation
- Explainable AI (XAI)
- Multi-user Support
- Cloud Database Integration
- Performance Optimization

---

# 👩‍💻 Author

**Ankireddypalli Kavitha**

GitHub Profile:

https://github.com/Kavitha-2108

Project:

**Smart Lender – AI-Powered Loan Approval Prediction**

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Your support is greatly appreciated!
