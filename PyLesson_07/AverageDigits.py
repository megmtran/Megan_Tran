
num = int(input("Enter a number: "))
digits = 0
avg = 0
n = num
while n > 0:
    digits += 1
    avg += n % 10
    n = int(n/10)
avg = avg/digits

print ("The average of the digits in",num,"is",avg)
        
