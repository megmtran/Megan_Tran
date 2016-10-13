a = True
b = False

#print(a and b)
#print(a or b)
print(not(a or b))


guess = int(input("Pick a number between 1 and 10: "))

if (guess >= 5 and guess <= 10):
    print("The number is right!")
else:
    print("Wrong!")
