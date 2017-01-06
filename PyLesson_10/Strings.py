go = input("Please enter 16 strings: ")
spList = go.split(" ")
print(spList)
wordsList = []
spot = 0
for i in range (0,4):
    output = ""
    wordsList.append([])
    for j in range (0,4):
        wordsList[i].append(spList[spot])
        output += "{:10}".format(wordsList[i][j])
        spot += 1
    print(output)
