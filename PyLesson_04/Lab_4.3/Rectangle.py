length = 4
width = 5
perim = 0

def setNums (l,w):
    global length,width
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

def calcPerim (l,w):
    global perim
    perim = 2 * (length + width)

setNums (length,width)
calcPerim (length,width)

print ("Your rectangle is {:.5f}".format (perim) , "ft around.")
