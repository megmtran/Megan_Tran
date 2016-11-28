sent = input("Enter a sentence: ")

def replace(sent):
    if sent.count (" ") == 0:
        return sent
    else:
        return sent[0:sent.index(" ")]+ "_" + replace(sent[sent.index(" ")+1:len(sent)])
    
print (replace(sent))
