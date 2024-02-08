from crypt import methods
from tokenize import Name
from flask import Flask, render_template, request
from utils import preprocessdata

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    # For using 'POST' method to get form data
    if request.method == 'POST':

        Gender = request.form.get('Gender')              
        Married = request.form.get('Married')             
        Education = request.form.get('Education')           
        Self_Employed = request.form.get('Self_Employed')       
        ApplicantIncome = request.form.get('ApplicantIncome')     
        CoapplicantIncome = request.form.get('CoapplicantIncome')   
        LoanAmount = request.form.get('LoanAmount')          
        Loan_Amount_Term = request.form.get('Loan_Amount_Term')    
        Credit_History = request.form.get('Credit_History')      
        Property_Area = request.form.get('Property_Area')

        # Changing the str form data to numeric data type (int/float)
        Gender = int(Gender)
        Married = int(Married)
        Education = int(Education)
        Self_Employed = int(Self_Employed)
        ApplicantIncome = int(ApplicantIncome)
        CoapplicantIncome = int(CoapplicantIncome) 
        LoanAmount = int(LoanAmount)
        Loan_Amount_Term = int(Loan_Amount_Term)
        Credit_History = int(Credit_History)
        Property_Area = int(Property_Area)

        result = preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
        LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)

        return render_template('predict.html', Loan_Status=result)


    # For using 'GET' method to get form data

    # if request.method == 'GET':
    #     Name = request.args.get('name')
    #     return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)