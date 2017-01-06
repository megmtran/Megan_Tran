
numsList = []
import random
for i in range(0,4):
    numsList.append([])
    for j in range(0,4):
        numsList[i].append(random.randint(1,101))

for nums in numsList:
    output=""
    for num in nums:
        output += str(num) + " "
    print(output)
