from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("models/xgboost_model.pkl")

# Load encoders
encoders = joblib.load("models/label_encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = encoders["Gender"].transform([request.form["Gender"]])[0]
    married = encoders["Married"].transform([request.form["Married"]])[0]
    dependents = encoders["Dependents"].transform([request.form["Dependents"]])[0]
    education = encoders["Education"].transform([request.form["Education"]])[0]
    self_employed = encoders["Self_Employed"].transform([request.form["Self_Employed"]])[0]
    property_area = encoders["Property_Area"].transform([request.form["Property_Area"]])[0]

    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_term = float(request.form["Loan_Amount_Term"])
    credit_history = float(request.form["Credit_History"])

    data = pd.DataFrame([[

        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area

    ]], columns=[

        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area"

    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)