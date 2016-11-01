num = int(input("Enter a number: "))
n = num
rev = 0
while n > 0:
    rev *= 10
    rev += n % 10
    n = int(n/10)

print (num,"reversed is",rev)
