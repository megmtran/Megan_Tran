sent = input("Please enter a sentence: ")
top = 0
while top < sent.count("a") > 0:
    sent = sent[0 : sent.index("a")] + "@" + sent[sent.index("a")+1 : len(sent)]

print (sent)
