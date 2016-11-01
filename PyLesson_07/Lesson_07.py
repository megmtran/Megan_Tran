number = int(input("Please enter a number: "))

while number > 0:
    # %10 returns last digit on the right
    print (number % 10)
    #dividing by 10 shaves off last digit from the right
    number = int(number / 10)





num = int(input("Enter a number: "))
digits = 0
n = num

while n > 0:
    digits += 1
    n = int(n/10)

print ("There are",digits,"digits in",num)






sent = input("Please enter a String: ")

top = 0
while top < sent.count(" ") > 0:
    sent = sent[0 : sent.index(" ")] + sent[sent.index(" ")+1 : len(sent)]

print ("Without spaces..." + sent)
