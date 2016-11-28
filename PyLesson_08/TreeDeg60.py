wd = input("Enter a word: ")
stop = len(wd)
start = 0
def tree(wd,start,stop):
    if start <= stop:
        print ("{:>15}".format(wd[0:start]))
        start += 1
        tree(wd,start,stop)
tree(wd,start,stop)
