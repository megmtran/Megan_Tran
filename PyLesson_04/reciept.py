def receipt(item, price):
    print ("*" , "{:>10} ........\t{:10.2f}".format (item, price))
              
item1 = input ("Please enter item one: ")
price1 = float(input ("Please enter the price: "))
item2 = input ("Please enter item two: ")
price2 = float(input ("Please enter the price: "))
item3 = input ("Please enter item three: ")
price3 = float(input ("Please enter the price: "))
subtotal = price1 + price2 + price3
tax = 0.08 * subtotal
total = subtotal + tax

print ("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
receipt (item1, price1)
receipt (item2, price2)
receipt (item3, price3)
receipt ("Subtotal:", subtotal)
receipt ("Tax:", tax)
receipt ("Total:", total)
print ("_______________________________________")
print ("* Thank you for your support *")
