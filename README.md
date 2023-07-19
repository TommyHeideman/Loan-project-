# Loan-project-
Part A:
This part is a script that allows the user to input loan information for each year of college. It begins by defining a dictionary term_dict, which maps total loan amounts to their corresponding loan terms (in years). Then, it prompts the user to input the number of college years money is borrowed (years). It validates the input and ensures it is a positive integer. It then initializes four empty lists to store loan information for each year: typeStud_list, loan_list, subRate_list, and unsubRate_list.

Next, it uses a loop to get loan information for each college year from the user. The user is prompted to input whether they are an "Independent" (I) or "Dependent" (D) student for each year, the total loan amount, the subsidized loan interest rate, and the unsubsidized loan interest rate. Each input is validated to ensure it is a valid number or character.

After gathering all the loan information, the total loan amount (total_loan) is calculated, and the loan term length is determined using the term_dict. The script then prints a loan summary showing the total loan amount and the term length.

Part B:
This part calculates the total amount owed six months after leaving college. It initializes some lists and a dictionary that define loan limits, repayment periods, and debt payoff periods. Then, it calculates the total loan amounts by type of loan (subsidized, unsubsidized, independent, and dependent) based on the loan information provided in Part A.

Next, it calculates the total amount owed after six months by summing the subloan, unsubloan, and interest accrued during the six-month grace period. The repayment period is determined based on the debtDict dictionary and adjusted for an additional interest rate if the period is longer than ten years.

Finally, it formats and prints the total amount owed after six months of leaving college.

Part C:
This part calculates the effect of loan consolidation on the student debt. It begins by defining a dictionary consolidation_dict, which contains consolidation rates and their corresponding total balance thresholds.

Then, it calculates the sub, unsub, independent, and dependent loan balances and interests based on the loan information provided in Part A.

Next, it determines the consolidation rate that corresponds to the highest threshold below the total balance and calculates the consolidated interest and total consolidated balance based on this rate.

After that, it calculates the number of years required to pay off the consolidated loan based on a monthly payment equal to or greater than 1% of the total balance. It calculates the amount of consolidated interest paid over the consolidation period.

Finally, it formats and prints the results, including the consolidated interest rate, the years to pay off the consolidated loan, and the total interest paid with consolidation.

Overall, this code performs various calculations related to student loans and helps users understand their debt repayment options and the implications of loan consolidation.
