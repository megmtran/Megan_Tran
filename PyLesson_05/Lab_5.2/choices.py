number = int(input("Please enter a number: "))

if number > 4:
    print("It meets the first condition!")
    if number <= 10:
        print("It meets both conditions!")

else:
    print("It meets none of the conditions!")



mathOrWords = int(input("Woudl you like to..."+
                        "\n 1. Do a math problem"+
                        "\n 2. Answer a question"))

if mathOrWords == 1:
    mathAnswer = int(input("What is 2 x 2? ")
    if mathAnswer == 4:
        print("Correct!")
    else:
        print ("No! Wrong! You lose!")

else:
    wordAnswer = input("Who said the phrase \"Whatever you are, be a good one.\"?")
    if wordAnswer == "Abraham Lincoln":
        print ("Correct!")
    else:
        print("No! Wrong! You lose!")
