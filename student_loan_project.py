# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:42:12 2023

@author: Tommy
"""

#PART A
# Define loan term dictionary
term_dict = {
    7499: 10,
    9999: 12,
    19999: 15,
    39999: 20,
    59999: 25,
    60000: 30
}

# Get number of college years
while True:
    try:
        years = int(input("Enter the number of college years money is borrowed: "))
        if years <= 0:
            print("Please enter a positive integer for the number of college years.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for the number of college years.")

# Initialize lists to store loan information for each year
typeStud_list = []
loan_list = []
subRate_list = []
unsubRate_list = []

# Get loan information for each year
for i in range(years):
    yearnum = str(i + 1)
    while True:
        typeStud = input("Enter I for Independent or D for Dependent student for year " + yearnum + ": ").upper()
       
        if typeStud == "I" or typeStud == "D":
            break
        else:
            print("Please enter either I or D for the type of student.")
            continue
    while True:
        try:
            loan = float(input("What is the total loan amount for year (must be a positive number): $"))
            if loan <= 0:
                print("Please enter a positive number for the loan amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the loan amount.")
    while True:
        try:
            subRate = float(input("What is the subsidized loan interest rate for year  (must be a positive number): "))
            if subRate <= 0:
                print("Please enter a positive number for the subsidized loan interest rate.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the subsidized loan interest rate.")
    while True:
        try:
            unsubRate = float(input("What is the unsubsidized loan interest rate for year (must be a positive number): "))
            if unsubRate <= 0:
                print("Please enter a positive number for the unsubsidized loan interest rate.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the unsubsidized loan interest rate.")
   
    # Store loan information for this year in the lists
    typeStud_list.append(typeStud)
    loan_list.append(loan)
    subRate_list.append(subRate)
    unsubRate_list.append(unsubRate)

# Calculate total loan amount and term length
total_loan = sum(loan_list)
for key in sorted(term_dict.keys()):
    if total_loan <= key:
        term_length = term_dict[key]
        break

# Print loan summary
print("\nLoan Summary:")
print("Total loan amount: ${:.2f}")
print("Term length:  years")
print("")

#PART B
#Total Amount Owed Six Months After Leaving College   


# Input data from Part A
years = 4
typeStud = ['D', 'D', 'I', 'I']
loan = [5000, 6000, 9000, 12000]
subRate = [0.05, 0.06, 0.06, 0.07]
unsubRate = [0.07, 0.08, 0.08, 0.09]

# Loan limit lists
subLoanLimit = [3500, 4500, 5500, 5500]
indepLoanLimit = [9500, 10500, 12500, 12500]
depLoanLimit = [5500, 6500, 7500, 7500]

# Debt payoff dictionary
debtDict = {7499: 10, 9999: 12, 19999: 15, 39999: 20, 59999: 25, 60000: 30}

# Calculate total loan amounts by type of loan
subLoan = [min(subLoanLimit[i], loan[i]) for i in range(years)]
unsubLoan = [max(0, loan[i] - subLoan[i]) for i in range(years)]
indepLoan = [min(indepLoanLimit[i], loan[i]) for i in range(years)]
depLoan = [min(depLoanLimit[i], loan[i]) for i in range(years)]

# Calculate total amount owed after six months of leaving college
totalBalance = sum(subLoan) + sum(unsubLoan)
interest = sum([subLoan[i] * subRate[i] * 0.5 for i in range(years)]) + \
           sum([unsubLoan[i] * unsubRate[i] * 0.5 for i in range(years)])
totalBalance += interest

# Adjust for debt repayment period
for key in sorted(debtDict.keys()):
    if totalBalance <= key:
        payoffPeriod = debtDict[key]
        break
else:
    payoffPeriod = debtDict[max(debtDict.keys())]

# Add extra interest for longer repayment periods
if payoffPeriod > 10:
    totalBalance += totalBalance * 0.05 * (payoffPeriod - 10)

# Format output
totalBalance = '${:,.2f}'.format(totalBalance)

print(f"Total owed after six months of leaving college is {totalBalance}.")

#Part C 
# Define a dictionary containing the consolidation rates and their corresponding total balance thresholds
consolidation_dict = {
    0.01: 10000,
    0.015: 20000,
    0.02: 30000,
    0.025: 40000,
    0.03: 60000,
    0.035: 80000,
    0.04: 100000
}

# Calculate the sub, unsub, independent, and dependent loan balances and interests
subLoan = [min(subLoanLimit[i], loan[i]) for i in range(years)]
unsubLoan = [max(0, loan[i] - subLoan[i]) for i in range(years)]
indepLoan = [min(indepLoanLimit[i], loan[i]) for i in range(years)]
depLoan = [min(depLoanLimit[i], loan[i]) for i in range(years)]

subBalance = sum(subLoan)
subInterest = sum([subLoan[i] * subRate[i] * payoffPeriod for i in range(years)])
unsubBalance = sum(unsubLoan)
unsubInterest = sum([unsubLoan[i] * unsubRate[i] * payoffPeriod for i in range(years)])
indepBalance = sum(indepLoan)
indepInterest = sum([indepLoan[i] * (subRate[i] + 0.04) * payoffPeriod for i in range(years)])
depBalance = sum(depLoan)
depInterest = sum([depLoan[i] * (subRate[i] + 0.04) * payoffPeriod for i in range(years)])

# Calculate the total balance and interest
totalBalance = subBalance + unsubBalance + indepBalance + depBalance
totalInterest = subInterest + unsubInterest + indepInterest + depInterest

# Find the consolidation rate that corresponds to the highest threshold below the total balance
for rate in sorted(consolidation_dict.keys(), reverse=True):
    if totalBalance >= consolidation_dict[rate]:
        consolidateRate = rate 
        break

# Calculate the consolidated interest and total consolidated balance
consolidatedInterest = totalBalance * consolidateRate
totalConsolidatedBalance = totalBalance + consolidatedInterest

# Calculate the number of years it will take to pay off the consolidated loan based on a monthly payment
# that is equal to or greater than 1% of the total balance
consolidatedYears = 30
while True:
    if consolidatedYears > 0:
        payment = totalConsolidatedBalance / (consolidatedYears * 12)
        if payment > totalBalance * 0.01 / 12:
            consolidatedYears -= 1
        else:
            break
    else:
        break

# Calculate the amount of consolidated interest paid over the consolidation period
consolidatedInterestPaid = consolidatedYears * 12 * payment - totalBalance

# Format the output as strings with commas and two decimal places
totalBalance = '${:,.2f}'.format(totalBalance)
totalInterest = '${:,.2f}'.format(totalInterest)
consolidatedInterestPaid = '${:,.2f}'.format(consolidatedInterestPaid)
consolidateRate = consolidateRate * 100

# Print the results
print(f"The consolidated interest rate is {consolidateRate:.2f}%.")
print(f"The years to pay off the consolidated loan is {consolidatedYears}.")
print(f"The total interest paid with consolidation is {consolidatedInterestPaid}.")

