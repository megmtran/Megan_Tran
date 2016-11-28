wd = input("Enter a word: ")
stop = len(wd)
start = 0
def tree(wd,start,stop):
    if start <= stop:
        print (wd[0:start])
        start += 1
        tree(wd,start,stop)

print ("{:>10}").format(tree(wd,start,stop))
