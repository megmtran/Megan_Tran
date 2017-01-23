class MilesPerHour:
    def__init__(self,distance,hours,minutes):
        self.dist = distance
        self.hrs = hours
        self.mins = minutes
        mph = 0

    def setValues(self,dis,hr,mns):
        self.dist = dis
        self.hrs = hr
        self.mins = mns
        mph = 0

    def getDist():
        return self.dist
    def getHours():
        return self.hrs
    def getMins():
        return self.mins
    def getMPH():
        mph = dist/(hrs+mins/60.0)
        return mph

def main():
    dist = input("Enter a distance value: ")
    hrs = input("Enter a value for hours: ")
    mins = input("Enter a value for minutes: ")

    values1 = MilesPerHour(dist,hrs,mins)

    print(values1.getDist(),"miles in",hrs+mins/60.0,"hours =",values1.getMPH)

    values1.setDist()
    values1.setHours()
    values1.setMins()

    print(values1.getDist(),"miles in",hrs+mins/60.0,"hours =",values1.getMPH)
