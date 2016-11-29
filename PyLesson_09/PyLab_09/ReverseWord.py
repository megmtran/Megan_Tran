words = [cat, souji, kuroh, mika, kazu]
print ("In order...")
for i in words:
    print(words[i])
print("")
print("Reversed...")
output = ""
for i in range(len(words),0,-1):
    output += words[i-1]
print(output)
