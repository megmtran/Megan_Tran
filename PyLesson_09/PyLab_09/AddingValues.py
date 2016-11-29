myList = []

for i in range (0,8):
    myList.append(i*4)

output = ""
j = 0
for i in myList:
    output+= str(i)
    if j < len(myList):
        output += ", "
    j +=1

print (output)
