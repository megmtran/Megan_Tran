side = float (input ("Enter the  length of a side: "))

def calcSurf (side):
    sa = 6 * (side**2)
    return sa

print ("The surface area of a cube with" , side , "sides is {:.5f}".format (calcSurf (side)) , ".")
