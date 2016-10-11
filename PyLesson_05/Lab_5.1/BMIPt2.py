ht = int(input("Enter your height in inches: "))
wt = int(input("Enter your weight in pounds: "))

bmi = 0
cond = "undetermined"
    
def calcBMI (h,w):
    global bmi,cond
    bmi = 703 * w / (h**2)
    if bmi < 18.5:
        cond = "underweight"
    elif bmi < 24.9:
        cond = "normal"
    elif bmi < 29.9:
        cond = "overweight"
    elif bmi < 34.9:
        cond = "obese"
    elif bmi < 39.9:
        cond = "very obese"
    elif bmi > 39.9:
        cond = "morbidly obese"

calcBMI (ht,wt)

print ("Your BMI is",bmi,".")
print ("You are",cond,".")
