# Finding input Gross Income and number of dependents
gross_income = float(input("Enter the taxpayer's Gross Income (in $): "))
numbers_of_dependents = int(input("Enter number of dependents: "))

# For calculating and printing Tax
standard_deduction = 10000   #to be charged on all taxpayers in $
dependent_deduction = 3000    # in $
taxable_income = gross_income - standard_deduction - (dependent_deduction * numbers_of_dependents)
tax = taxable_income * 0.2   # 20% tax rate chared on all taxpayers
print("Tax is:", tax)
