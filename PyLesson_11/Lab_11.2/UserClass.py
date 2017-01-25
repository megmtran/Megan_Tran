import random

class User:
    def __init__(self,fName = "",lName = "",avat = ""):
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

def main():
    user1 = User()
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    public = input("Would you like to use a public avatar? Y or N? ")
    if public == "n":
        user1 = User(firstName,lastName)
    else:
        user1 = User(firstName,lastName,avatar)

    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                               "\nLast Name: " + self.lastName + \
                               "\nAvatar: " + self.avatar + \
                               "\nUser ID#: " + str(self.userID)
main()
