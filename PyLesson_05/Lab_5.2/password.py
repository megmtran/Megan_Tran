def recursion ():
    user = input ("Username: ")
    passwd = input ("Password: ")
    if user == "sokumika" and passwd == "ham":
        print ("You are granted access!")
    else:
        if user == "sokumika":
            print ("Your password is incorrect!")
            recursion ()
        elif passwd == "ham":
            print ("Your username is incorrect!")
            recursion ()
        else:
            print ("Your username and password are incorect!")
            recursion ()

recursion ()
