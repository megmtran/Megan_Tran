
class Human:
    def __init__(self,h,e,s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def setHES(self,newHair,newEyes,newSkin):
        self.hair = newHair
        self.eyes = newEyes
        self.skin = newSkin

    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin

def main():
    hair = input("Enter a hair color: ")
    eyes = input("Enter a eye color: ")
    skin = input("Enter a skin color: ")

    newHuman = Human(hair,eyes,skin)

    print("My info...")
    print("Hair: ",newHuman.getHair())
    print("Eyes: ",newHuman.getEyes())
    print("Skin: ",newHuman.getSkin())

    newHuman.setHES("black","brown","white")

    print("Friend's info..")
    print("Hair: ",newHuman.getHair())
    print("Eyes: ",newHuman.getEyes())
    print("Skin: ",newHuman.getSkin())
    
main()
