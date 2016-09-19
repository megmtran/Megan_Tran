def receipt(item1, price1, item2, price2, item3, price3):
    print ("*" , "{:.>10}\t{:10.2f}".format (item1 , price1))
    print ("*" , "{:.>10}\t{:10.2f}".format (item2 , price2))
    print ("*" , "{:.>10}\t{:10.2f}".format (item3 , price3))
    print ("*" , "{:.>10}\t{10.2f}".format ("Subtotal:" , subtotal))
    print ("*" , "{:.>10}\t{10.2f}".format ("Tax:" , tax))
    print ("*" , "{:.>10}\t{10.2f}".format ("Total:" , total))
           
item1 = input ("Please enter item one: ")
price1 = int(input ("Please enter the price: "))
item2 = input ("Please enter item two: ")
price2 = int(input ("Please enter the price: "))
item3 = input ("Please enter item three: ")
price3 = int(input ("Please enter the price"))
subtotal = price1 + price2 + price3
tax = 0.08 * subtotal
total = subtotal + tax

print ("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")

receipt (item1, price1, item2, price2, item3, price3)

print ("_______________________________________")
print ("* Thank you for your support *")
