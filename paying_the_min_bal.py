
def paying_the_min( balance, annualInterestRate, monthlyPaymentRate):
    ''' Calculate the credit card balance after one year if a person only pays the
    minimum monthly payment required.
    balance:            Outstanding balance on the credit card
    annualInterestRate: Annual interest rate as a decimal
    monthlyPaymentRate: Minimum monthly payment rate as a decimal'''

    monthlyInterestRate = annualInterestRate / 12.0
    totalPaid = 0.0
    for i in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * balance
        totalPaid += minimumMonthlyPayment
        monthlyUnpaidBalance  = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        print('Month: {0}'.format(i+1))
        print('Minimum monthly payment: {0}'.format(round(minimumMonthlyPayment, 2)))
        print('Remaining balance: {0}'.format(round(balance, 2)))
    print('Total paid: {0}'.format(round(totalPaid, 2)))
    print('Remaining balance: {0}'.format(round(balance, 2)))

def main():
    paying_the_min(4842, 0.2, .04)

if __name__ == '__main__':
    main()
