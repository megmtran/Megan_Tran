
import math
class Distance:
    def__init__(self,x1,y1,x2,y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2

    def setValues(self,nx1,ny1,nx2,ny2):
        self.xOne = nx1
        self.yOne = ny1
        self.xTwo = nx2
        self.yTwo = ny2

    def getMPH (self):
        distance = math.sqrt((xTwo-xOne)*(xTwo-xOne)+(yTwo-yOne)*(yTwo-yOne))
        return mph

def main ():
    x1 = int(input("Enter the first x-coordinate: "))
    y1 = int(input("Enter the first y-coordinate: "))
    x2 = int(input("Enter the second x-coordinate: "))
    y2 = int(input("Enter the seconf y-coordinate: "))

    dist = coords(x1,y1,x2,y2)

    print("distance = {10.2}".format(dist))
