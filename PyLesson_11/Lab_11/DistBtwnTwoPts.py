
import math
class distance:
    def __init__(self,x1,y1,x2,y2):
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
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

def main ():
    x1 = int(input("Enter the first x-coordinate: "))
    y1 = int(input("Enter the first y-coordinate: "))
    x2 = int(input("Enter the second x-coordinate: "))
    y2 = int(input("Enter the seconf y-coordinate: "))

    coords = distance(x1,y1,x2,y2)

    print("distance = ",coords.getMPH())

main()
