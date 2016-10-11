import random
player = random.randint(1,6)
comp = random.randint (1,6)

print ("You rolled a" , player, ".")
print ("The computer rolled a" , comp, ".")

if player > comp:
    print ("The winner is you!")

if not player > comp:
    print ("The winner is the computer!")
