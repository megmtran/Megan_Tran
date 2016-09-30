side = 4
sa = 16

def setNums (sd):
    global side
    side = float(input("Enter the length of a side: "))

def calcSA (sd):
    global sa
    sa = 6 * (side**2)

setNums (side)
calcSA (side)

print ("The surface area of a cube whose sides are",side,"in length is {:.5f}".format (sa),".")
