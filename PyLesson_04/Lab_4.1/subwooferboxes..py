
def main (h,l,w):
    v = (h * l * w)
    return (v/1728)

h = float (input ("Enter the height: "))
l = float (input ("Enter the length: "))
w = float (input ("Enter the width: "))

print("Your box will be {:5.2f}".format(main (h,l,w)),"cubic feet.")
