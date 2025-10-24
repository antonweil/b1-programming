cpin = "1293"

attempts = 0
mattempts = 4
logon = False

while attempts < mattempts:
    print("attempt ", attempts + 1, "of ", mattempts)
    attempts += 1
    pin = input("Enter PIN: ")
    
    if pin == cpin:
        print("correct.")
        logon = True
        break
    else:
        print("wrong.")
if logon == True:
    print("logged on. number of attempts: ", attempts)