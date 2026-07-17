# 🏦 Smart Lender – AI-Powered Loan Approval Prediction

Smart Lender is an AI-powered web application that predicts whether a loan application is likely to be **Approved** or **Rejected** using Machine Learning. The application is developed using **Python, Flask, XGBoost, and Scikit-learn**, providing a simple, fast, and user-friendly interface for loan eligibility prediction.

---

# 🌐 Live Application

https://smart-lender-ml-project.onrender.com/

---

# 🎥 Demo Video

https://drive.google.com/file/d/1hOw3sB-cznPaEGxVmvbvgfBdbYrA5reC/view?usp=drive_link

---

# 📂 GitHub Repository

https://github.com/Kavitha-2108/Smart-Lender-ML-Project

---

# 📌 Project Overview

Smart Lender is a Machine Learning-based web application designed to assist banks and financial institutions in evaluating loan applications. Users enter applicant details through an interactive web interface, and the trained **XGBoost** model instantly predicts whether the loan application is likely to be approved or rejected.

The project demonstrates the integration of Machine Learning with Flask to provide fast, reliable, and real-time loan eligibility predictions.

---

# ✨ Features

- 🤖 AI-powered loan approval prediction
- 🌐 User-friendly Flask web application
- 📊 Machine Learning model using XGBoost
- ⚡ Real-time prediction results
- 📈 Displays Approval Confidence and Rejection Risk
- 💾 Trained model saved using Joblib
- 🎨 Responsive and attractive user interface
- ☁️ Deployed on Render

---

# 🛠 Technologies Used

## Programming Language
- Python

## Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Web Development
- Flask
- HTML5
- CSS3
- JavaScript

## Deployment
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

## 2. Navigate to the Project Folder

```bash
cd Smart-Lender-ML-Project
cd "5. Project Development Phase"
```

## 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Flask Application

```bash
python app.py
```

## 5. Open the Application

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🔄 Project Workflow

1. The user enters loan applicant details.
2. Flask validates the submitted information.
3. Input data is transformed using the saved label encoders.
4. The trained XGBoost model predicts the loan status.
5. The system displays:
   - Loan Approved or Loan Rejected
   - Approval Confidence (%)
   - Rejection Risk (%)

---

# 📊 Machine Learning Model

The Smart Lender application uses an **XGBoost Classifier** trained on historical loan application data.

### Data Preprocessing

- Missing value handling
- Label Encoding
- Feature transformation
- Model training using XGBoost
- Model serialization using Joblib

Saved model files:

- `xgboost_model.pkl`
- `label_encoders.pkl`

These files are loaded by the Flask application during prediction.

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

After prediction, the application displays:

- ✅ Loan Approved
- ❌ Loan Rejected
- 📈 Approval Confidence (%)
- 📉 Rejection Risk (%)

The confidence values help users understand the certainty of the model's prediction.

---

## 🏠 Home Page

<img width="1883" height="1067" alt="home" src="https://github.com/user-attachments/assets/ab341566-1fde-41ef-b594-9bd26f83a8a2" />


## 📝 Prediction Form

<img width="1918" height="1078" alt="prediction" src="https://github.com/user-attachments/assets/3bc51a20-79d6-492b-97b9-187207888461" />


## ✅ Loan Approved

<img width="1918" height="1078" alt="approved" src="https://github.com/user-attachments/assets/506ddcdc-6c84-48e2-baa9-9de893231fda" />


## ❌ Loan Rejected

<img width="1917" height="1078" alt="rejected" src="https://github.com/user-attachments/assets/5aae9dda-ba80-421d-843e-8f273e1489ce" />

---

# 🚀 Deployment

**Hosting Platform:** Render

**Live URL**

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

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!
