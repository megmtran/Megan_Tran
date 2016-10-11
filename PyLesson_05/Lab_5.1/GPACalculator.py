g1 = input ("Enter your letter grade in your first class: ")
g2 = input ("Enter your letter grade in your second class: ")
g3 = input ("Enter your letter grade in your third class: ")
g4 = input ("Enter your letter grade in your fourth class: ")
g5 = input ("Enter your letter grade in your fifth class: ")
g6 = input ("Enter your letter grade in your sixth class: ")
g7 = input ("Enter your letter grade in your seventh class: ")

def calcPoints (grade):
    if grade == "A" :
        return 4.0
    if grade == "B" :
        return 3.0
    if grade == "C" :
        return 2.0
    if grade == "D" :
        return 1.0
    if grade == "F" :
        return 0.0

GPA = float((calcPoints(g1)+calcPoints(g2)+calcPoints(g3)+calcPoints(g4)+calcPoints(g5)+calcPoints(g6)+calcPoints(g7))/7);

print ("Your GPA is {:.2}".format (GPA))
