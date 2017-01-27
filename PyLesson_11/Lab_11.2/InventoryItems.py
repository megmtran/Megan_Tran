import random

class Inventory:
    def __init__(self,manufacturer,name,category = "",price = ""):
        self.man = manufacturer
        self.nm = name
        self.cat = category
        self.prc = price
        self.UPC = random.randint(1000000000,10000000000)
        
    def setInventory (self,newMan,newNm,newCat,newPrc):
        self.man = newMan
        self.nm = newNm
        self.cat = newCat
        self.prc = newPrc

    def getMan(self):
        return self.man
    def getNm(self):
        return self.nm
    def getCat(self):
        return self.cat
    def getPrc(self):
        return self.prc
    def getUPC(self):
        return self.UPC

    def __str__(self):
        return "Inventory Info...\nManufacturer: " + self.man + \
                                "\nName: " + self.nm + \
                                "\nCategory: " + self.cat + \
                                "\nPrice: $" + str(self.prc) + \
                                "\nUPC#: " + str(self.UPC)

def main():
    manufacturer = input("Manufacturer: ")
    name = input("Name: ")
    info = input("Entering category and price information? Y or N? ")
    if info == "n":
        item1 = Inventory(manufacturer,name)
    else:
        category = input("Category: ")
        price = int(input("Price: "))
        item1 = Inventory(manufacturer,name,category,price)
    print(item1.__str__())

main()
