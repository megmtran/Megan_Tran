rad = 0
a = 0

def setNum (r):
    global rad
    rad = float(input("Enter the radius: "))

def calcArea (r):
    global a
    a = 3.14 * (rad**2)

setNum (rad)
calcArea (rad)

print ("The area of a circle with radius",rad,"is {:.5f}".format (a),".")
