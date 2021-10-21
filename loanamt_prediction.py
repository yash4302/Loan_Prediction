import math
#salary in rs pending emi of any sort in rs years of loan required and other sources of income
sal=float(input("enter salary "))
emi=float(input("enter pending emi "))
yr=float(input("enter years "))
oth=float(input("enter other income "))

if sal==0:
    sal=1
if yr<=0:
    yr=1
#our criteria to provide loan is that minimum 10000 salary should be given else loan elgible is 0
if sal+oth<10000:
    loan=0
#loans in which year is 1 gives highest accuracy to the true value
else:
    if yr==1:
        loan=float(pow(1.00112935,10000))*(sal+oth)/10000
    else:
#the loan amount for certain period of year fluctuates much because of an undetermined constant
#here the constant is 46.5(subject to change as we move towards accuracy)
        loan=sal*47*(math.log(yr,10))
#incase person has pending loan deduct the money of it
    loan=loan-(float(pow(1.00938504,1000))*emi/1000)

print(loan)
        