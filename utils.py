import numpy as np
import joblib

def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    
    data = [[Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
    Loan_Amount_Term, Credit_History, Property_Area]]

    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(data)

    return prediction


