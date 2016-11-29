myList = [1,2,3,4,5]

print(myList[2])
print(myList[:2])
print(myList[2:3])
print(myList)

output=""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
    j+=1

print(output)
    
