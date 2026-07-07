import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import os

# Load dataset
data = pd.read_csv("loan_prediction.csv")

# Remove Loan_ID if present
if "Loan_ID" in data.columns:
    data.drop("Loan_ID", axis=1, inplace=True)

# Fill missing values
cat_cols = data.select_dtypes(include="object").columns
num_cols = data.select_dtypes(exclude="object").columns

cat_imputer = SimpleImputer(strategy="most_frequent")
num_imputer = SimpleImputer(strategy="median")

data[cat_cols] = cat_imputer.fit_transform(data[cat_cols])
data[num_cols] = num_imputer.fit_transform(data[num_cols])

# Encode categorical columns
encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# Split features and target
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "XGBoost": XGBClassifier(
        eval_metric="logloss",
        random_state=42
    )
}

best_model = None
best_accuracy = 0

print("\nModel Accuracies:\n")

for name, model in models.items():
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print(f"{name}: {acc*100:.2f}%")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(best_model, "models/xgboost_model.pkl")
joblib.dump(encoders, "models/label_encoders.pkl")

print("\nBest model saved successfully!")
print(f"Best Accuracy: {best_accuracy*100:.2f}%")