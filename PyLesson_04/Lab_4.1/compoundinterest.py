def loan (r, p, n, t):
    a = p * (1 + r / n)**(n*t)
    return ("${:4.2f}".format (a))

r = float (input ("Enter the interest rate: "))
p = float (input ("Enter the principal amount: "))
n = float (input ("Enter the number of times the loan is compounded per year: "))
t = float (input ("Enter the life of the loan in years: "))

print ("Your total payment amount is",loan (r, p, n, t),".")

