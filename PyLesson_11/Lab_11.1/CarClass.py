class Car:
    def __init__(self,p,i,e,t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setCustom (self,newPaint,newInterior,newEngine,newTires):
        self.paint = newPaint
        self.interior = newInterior
        self.engine = newEngine
        self.tires = newTires

    def getPaint (self):
        return self.paint
    def getInterior (self):
        return self.interior
    def getEngine (self):
        return self.engine
    def getTires (self):
        return self.tires

def main ():
    paint = input("Enter a choice for paint: ")
    interior = input("Enter a choice for interior: ")
    engine = input("Enter a choice for engine: ")
    tires = input("Enter a choice for tires: ")

    features = Car(paint,interior,engine,tires)

    print("Your vehicle is ready......")
    print("Paint:   ",features.getPaint())
    print("Interior:   ",features.getInterior())
    print("Engine:   ",features.getEngine())
    print("Tires:   ",features.getTires())

main()
