sent = input("Enter a sentence: ")
def replace (string):
    if string.count(" ") == 0:
        return string 
    else:
        return string[0] + "_" + replace(string[1:])
    print (string)

replace (sent)
