num = int(input("Enter a number: "))
sum = 0
n = num

while n > 0:
    sum += n % 10
    n = int(n/10)

print ("The sum of the digits in",num,"is",sum)

