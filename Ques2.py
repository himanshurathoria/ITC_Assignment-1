# program to calculate income tax
print ("Please enter you Gross Income to the nearest penny. Your income should be more than $10000")
g_income = float(input())
print ("Please enter the number of dependents you have")
dep = int(input())
income = float (g_income - 10000 - (dep * 3000))
print ("Your taxable income is = $", income)
tax = float (20/100 * income)
print ("Your income tax= $", tax)
