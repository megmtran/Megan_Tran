length = float (input ("Enter the length: "))
width = float (input ("Enter the width: "))

def calcPerim (length, width):
    perim = 2 * ( length + width)
    return perim

calcPerim (length, width)
print ("Your rectangle is {:.5f}".format(calcPerim (length, width)) , "ft around.")
              
