
num = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

output = ""

for i in range (0,num,num2):
    output = output + str(i) + "\t"


print (output)
