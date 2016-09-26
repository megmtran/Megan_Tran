length =float (input ("Enter the length: "))
width = float (input ("Enter the width: "))

def calcPerim (length, width):
    perim = 2 * ( length + width)

def print (perim):
    print ("Your rectangle is {:10.5f}".format (calcPerim (length, width)) , "ft around.")
              
print (perim)              
