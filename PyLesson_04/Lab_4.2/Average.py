num1 = float (input ("Enter the first number: "))
num2 =  float (input ("Enter the second number: "))
num3 =  float (input ("Enter the third number: "))

def average (num1,num2,num3):
    avg = (num1 + num2 + num3)/3
    return avg

print ("The average of" , num1 , "," , num2 , ",and" , num3 , "is {:.5f}".format (average (num1,num2,num3)) , ".")

