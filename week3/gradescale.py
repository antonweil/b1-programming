#infinite loop to gather many iterations of scores
while True:
    #try/except to exclude errors for non integers
    try:
        #gather user input of scores
        score = int(input("Enter score (0–100): "))
        if 0 <= score <= 100:
            #end infinite loop by entering an integer over 100
            break
        else:
            print("Thats not a valid score. Try again.")
    except ValueError:
        print("Thats not even a number. Try again.")

#dropping number scale
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "E"
else:
    grade = "F"

#print final result
print("your grade: ", grade)

#encouragement for good grades
if grade == "A" or grade == "B":
    print("thats great! Keep it up!")