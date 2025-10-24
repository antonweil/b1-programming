while True:
    try:
        score = int(input("Enter score (0–100): "))
        if 0 <= score <= 100:
            break
        else:
            print("Thats not a valid score. Try again.")
    except ValueError:
        print("Thats not even a number. Try again.")

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

print("your grade: ", grade)

if grade == "A" or grade == "B":
    print("thats great! Keep it up!")