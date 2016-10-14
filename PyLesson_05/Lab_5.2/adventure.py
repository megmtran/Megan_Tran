choice1 = input("It's Halloween and you are out with a friend. You see a trail of your favorite candy. Do you and your friend follow it? ")
if choice1 == "no":
    scream = input("Good choice! No one would fall for that, right? You continue on house to house, ringing doorbells. But as you're leaving an \"empty\" house, a hand grabs you and pulls you in. Do you scream? ")
    if scream == "yes":
        fight = input("He doesn't seem to be startled by your scream, but rather pulls out a knife and tells you to shut up. Do you try to fight back? ")
        if fight == "yes":
            print ("You elbow him in the stomach, causing him to release his grip on you. You escape successfully! ")
        else:
            print ("He brings you into the basement, where you are tortured until police find you three years later.")
    else:
        escape = input("He brings you down to the basement, then leaves. Do you try to escape? ")
        if escape == "yes":
            print ("You run out of the basement. He sees you and knicks you with is knife, but you are able to return home safely.")
        else:
            print ("He comes back down with handcuffs. You remain in the basement until police find you three years later.")
else:
    age = int(input("That wasn't too smart...how old are you again? "))
    if age <= 13:
        troll = input("Oh! No wonder, you're just a little kiddo...you follow the trail until you come across a troll. Here's his riddle: Feed me and I live, yet give me a drink and I die. What am I? ")
        if troll == "fire":
            print ("Congrats! The troll walks off, revealing treasure chest full of candy! Your Halloween is a success! ")
        else:
            print ("The troll is unhappy with your answer. He makes you wash his moldy feet.")
    else:
        troll = input("Jeez, I thought you'd be smarter than that...you follow the trail until you come across a troll. Here's his riddle: Feed me and I live, yet give me a drink and I die. What am I? ")
        if troll == "fire":
            print ("Congrats! The troll walks off, revealing treasure chest full of candy and gold! Your Halloween is a success!")
        else:
            print ("The troll is unhappy with your answer. He chases you further into the forest, where you will be trapped forever.")    
