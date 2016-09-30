num1 = 1
num2 = 2
num3 = 3
avg = 4

def setNums (n1,n2,n3):
    global num1,num2,num3
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

def calcAvg (n1,n2,n3):
    global avg
    avg = (num1 + num2 + num3)/3

setNums (num1,num2,num3)
calcAvg (num1,num2,num3)

print ("The average of",num1,",",num2,",and",num3,"is {:.5f}".format (avg),".")
                 
