num = int(input("Enter a number: "))

def luck(num):
    if num > 0:
        if (num % 10 == 7):
            return 1 + luck(int(num/10))
        else:
            return 0 + luck(int(num/10))
    else:

        return 0

print(luck(num)) 
    
