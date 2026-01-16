
#define variables
cpin = "1293"
attempts = 0
mattempts = 4
logon = False

#define loop for all attempts
while attempts < mattempts:
    print("attempt ", attempts + 1, "of ", mattempts)
    #add to attempts
    attempts += 1
    #gather user input
    pin = input("Enter PIN: ")
    
    #validate input
    if pin == cpin:
        print("correct.")
        logon = True
        break
    else:
        print("wrong.")
#final evaluation
if logon == True:
    print("logged on. number of attempts: ", attempts)
elif logon == False:
    print("too many failed attempts. Account Lockout")