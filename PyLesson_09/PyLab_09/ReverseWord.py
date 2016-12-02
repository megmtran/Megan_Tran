words = ["cat", "souji", "kuroh", "mika", "kazu"]
print ("In order...")
output = ""

for i in words:
    output += i + " "
print (output)

print("")

print("Reversed...")
def reverse (array):
    for i in reversed(array):
        print (i,end=' ')
reverse (words)

