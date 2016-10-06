def receipt (item,price):
    print ("*" , "{:>10} ........\t{:10.2f}".format (item, price))
i1 = input("Enter item one: ")
p1 = float(input("Enter the price of item one: "))
i2 = input("Enter item two: ")
p2 = float(input("Enter the price of item two: "))
i3 = input("Enter item three: ")
p3 = float(input("Enter the price of item three: "))
i4 = input("Enter item four: ")
p4 = float(input("Enter the price of item four: "))
subtotal = p1 + p2 + p3 + p4
if subtotal > 2000:
    discount = subtotal * 0.15
if not subtotal > 2000:
    discount = 0
tax  = 0.08 * subtotal
total = subtotal - discount + tax

print ("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
receipt (i1,p1)
receipt (i2,p2)
receipt (i3,p3)
receipt (i4,p4)
receipt ("Subtotal:",subtotal)
receipt ("Discount:",discount)
receipt ("Tax:",tax)
receipt ("Total:",total)
print ("_______________________________________")
print ("* Thank you for your support *")




           
           
