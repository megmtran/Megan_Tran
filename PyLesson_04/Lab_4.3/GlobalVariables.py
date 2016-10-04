num = 3
num2 = 4
sum = 9

def mkSum ():
    global sum, num , num2
    sum = num + num2

def numPrint ():
    global num, num2, sum
    print (num, "plus" , num2, "equals" , sum)

mkSum()
numPrint()
