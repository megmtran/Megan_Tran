w1 = input("Enter a word: ")
w2 = input("Enter a second word: ")
w3 = input("Enter a third word: ")

def makeCenter (word):
    if (len(word)>=20):
        return word
    else:
        return makeCenter(" " + word + " ")

print (makeCenter(w1))
print (makeCenter(w2))
print (makeCenter(w3))
