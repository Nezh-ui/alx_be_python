Monthly_income = input("What is your monthly income?  " )
Monthly_expenses  = input("What are your monthly expenses?  ")
Monthly_expenses = int(Monthly_expenses)
Monthly_income = int(Monthly_income)
Monthly_savings = Monthly_income - Monthly_expenses
Projected_Savings = (Monthly_savings * 12 + (Monthly_savings * 12 * 0.05))
print(Monthly_savings and Projected_Savings)
           