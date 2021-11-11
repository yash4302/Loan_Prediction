import os
import joblib
from django.contrib import auth
from . import loanamt_prediction
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def root(request):
    return render(request,'root.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('root')
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username,password = password) #login
        if user is not None:
            auth.login(request,user)
            return redirect('root')
        else:
            return render(request,'login.html',{"WARNING":"Username or Password Wrong!"})

def signup(request):
    if request.user.is_authenticated:
        return redirect('root')
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if len(password) > 8:
                try:
                    user = User.objects.get(username = username)
                    return render(request,'signup.html',{"WARNING":"User Already Exists!"})
                except User.DoesNotExist:
                    user = User.objects.create_user(username,password = password) #signup
                    auth.login(request,user)
                    return redirect('root')
            else:
                return render(request,'signup.html',{"WARNING":"Password is Very Short!"})
        else:
            return render(request,'signup.html',{"WARNING":"Passwords Not Matching!"})

def predict(request):
    path = os.path.join(os.path.join(os.getcwd(),'loan_app'),"model_random_forest.pkl")
    print(path)
    model = joblib.load(path)

    loan_amount = request.POST.get('loan_amount')
    credit_score = request.POST.get('credit_score')
    annual_income = request.POST.get('annual_income')
    monthly_debt = request.POST.get('monthly_debt')
    years_credit_history = request.POST.get('years_credit_history')
    months_since_last_delinquent = request.POST.get('months_since_last_delinquent')
    number_of_open_accounts = request.POST.get('number_of_open_accounts')
    number_of_credit_problems =  request.POST.get('number_of_credit_problems')
    current_credit_balance =  request.POST.get('current_credit_balance')
    bankruptcies =  request.POST.get('bankruptcies')
    tax_liens =  request.POST.get('tax_liens')

    # select variables
    years_in_current_job = request.POST.get('years_in_current_job')
    term =  request.POST.get('term')
    purpose =  request.POST.get('purpose')
    home_ownership =  request.POST.get('home_ownership')

    # for loan term
    if term == 0:
        short_term = 1
    else:
        short_term = 0

    # for home ownership
    own_home = 0
    rent = 0
    if home_ownership == 'Own Home':
        own_home = 1
    elif home_ownership == 'Rent':
        rent = 1


    # for purpose of the loan
    car = 0
    house = 0
    debt = 0
    education = 0
    home_improvements = 0
    major_purchase = 0
    medical_bills = 0
    moving = 0
    other = 0
    renewable_loan = 0
    small_business = 0
    trip = 0
    vacation = 0
    wedding = 0

    if purpose == 'Home improvements':
        home_improvements = 1
    elif purpose == 'Debt consolidation':
        debt = 1
    elif purpose == 'House':
        house = 1
    elif purpose == 'Car':
        car = 1
    elif purpose == 'Major purchase':
        major_purchase = 1
    elif purpose == 'Take a trip':
        trip = 1
    elif purpose == 'Small business':
        small_business = 1
    elif purpose == 'Medical bills':
        medical_bills = 1
    elif purpose == 'Wedding':
        wedding = 1
    elif purpose == 'Vacation':
        vacation = 1
    elif purpose == 'Educational expenses':
        education = 1
    elif purpose == 'Moving':
        moving = 1
    elif purpose == 'Renewable Loan':
        renewable_loan = 1
    elif purpose == 'Other':
        other = 1

    order_of_variables = [[ loan_amount,credit_score,annual_income,monthly_debt,years_credit_history,months_since_last_delinquent,number_of_open_accounts,number_of_credit_problems,current_credit_balance,bankruptcies,tax_liens,years_in_current_job,short_term,own_home,rent,car,house,debt,education,home_improvements,major_purchase,medical_bills,moving,other,renewable_loan,small_business,trip,vacation,wedding ]]
    print(order_of_variables)
    prediction = model.predict(order_of_variables)
    return prediction[0]

@login_required(login_url = 'login')
def loan(request):
    years = [i for i in range(1,10)]
    if request.method == 'GET':
        return render(request,'loan.html',{'years':years})
    elif request.method == 'POST':
        prediction = predict(request)
        print(prediction)
        if prediction:
            return render(request,'loan.html',{'years':years,'msg':'Your Loan Will get Approved :)','prediction':prediction})
        else:
            return render(request,'loan.html',{'years':years,'msg':'Your Loan Will not get Approved :(','prediction':prediction})

@login_required(login_url = 'login')
def amount(request):
    if request.method == 'GET':
        return render(request,'amount.html')
    elif request.method == 'POST':

        monthly_income = int(request.POST.get('monthly_income'))
        emi =  int(request.POST.get('emi'))
        years =  int(request.POST.get('years'))
        other_income =  int(request.POST.get('other_income_monthly'))

        amount = int(loanamt_prediction.predict_min_amount(monthly_income,emi,years,other_income))

        return render(request,'amount.html',{'amount':amount})

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('root')
