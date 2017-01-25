class MilesPerHour:
    def __init__(self,distance,hours,minutes):
        self.dist = distance
        self.hrs = hours
        self.mins = minutes
        self.mph = 0

    def setValues(self,newDist,newHrs,newMins):
        self.dist = newDist
        self.hrs = newHrs
        self.mins = newMins
        self.mph = 0

    def getDist(self):
        return self.dist
    def getHours(self):
        return self.hrs
    def getMins(self):
        return self.mins
    def getMPH(self):
        self.mph = self.dist/(self.hrs+self.mins/60.0)
        return self.mph

def main():
    dist = int(input("Enter a distance value: "))
    hrs = int(input("Enter a value for hours: "))
    mins = int(input("Enter a value for minutes: "))

    values1 = MilesPerHour(dist,hrs,mins)

    print(values1.getDist(),"miles in",values1.getHours(),"hours and",values1.getMins(),"minutes =",values1.getMPH())

    values1.setValues(50,1,5)
   
    print(values1.getDist(),"miles in",values1.getHours(),"hours and",values1.getMins(),"minutes =",values1.getMPH())

main()
