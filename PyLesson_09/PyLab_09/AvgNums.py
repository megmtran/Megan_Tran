
numbers = []
import random 
for i in range (0,10):
    numbers.append(random.randint(1,100))
print ("Numbers...")
output = ""

for i in numbers:
    output += str(i) + " "
print (output)
print (" ")
def average (nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)
print ("The average of the above numbers is...",average(numbers))

