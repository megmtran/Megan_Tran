def format (item,price):
    print ("*" , "{:<10}\t{:10.2f}".format (item, price))
i1 = input("Enter item one: ")
p1 = float(input("Enter the price of item one: "))
i2 = input("Enter item two: ")
p2 = float(input("Enter the price of item two: "))
i3 = input("Enter item three: ")
p3 = float(input("Enter the price of item three: "))
i4 = input("Enter item four: ")
p4 = float(input("Enter the price of item four: "))

subtotal = p1 + p2 + p3 + p4

disct = 0
def discount ():
    global disct
    if subtotal >= 2000:
        disct = subtotal * 0.15
    if subtotal < 2000:
        disct = 0
discount ()

tax  = 0.08 * subtotal
total = subtotal - disct + tax

print ("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
format (i1,p1)
format (i2,p2)
format (i3,p3)
format (i4,p4)
format ("Subtotal:",subtotal)
format ("Discount:",disct)
format ("Tax:",tax)
format ("Total:",total)
print ("_______________________________________")
print ("* Thank you for your support *")




           
           
