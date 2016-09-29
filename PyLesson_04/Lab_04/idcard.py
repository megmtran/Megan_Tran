def idcard (item1, item2):
    print ("*" , "{:<17}\t{:>17}".format (item1, item2) , "*")
    
first = input ("Enter your first name: ")
last = input ("Enter your last name: ")
title = input ("Enter your title: ")
school = input ("Enter the school site: ")
year = input ("Enter the school year: ")
subject = input ("What is your subject? ")

print ("*******************************************")
idcard (school, year)
idcard (first, last)
idcard (title, subject)
print ("*******************************************")
