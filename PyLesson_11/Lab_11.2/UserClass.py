import random

class User:
    def __init__(self,fName,lName,avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)
    def setUser (self,newFirst,newLast,newAvat):
        self.firstName = newFirst
        self.lastName = newLast
        self.avatar = newAvat
    def getFirst(self):
        return self.firstName
    def getLast(self):
        return self.lastName
    def getAvatar(self):
        return self.avatar
    def getUserID(self):
        return self.UserID

    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                               "\nLast Name: " + self.lastName + \
                               "\nAvatar: " + self.avatar + \
                               "\nUser ID#: " + str(self.userID)

def main():
    fName = input("First Name: ")
    lName = input("Last Name: ")
    public = input("Would you like to use a public avatar? Y or N? ")
    if public == "n":
        user1 = User(fName,lName)
    else:
        avat = input("Avatar Name: ")
        user1 = User(fName,lName,avat)
    print(user1.__str__())
        

main()
