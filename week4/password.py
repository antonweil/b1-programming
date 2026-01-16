#create variables
passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]
compliant = 0
non_compliant = 0

#for loop for every given password
for password in passwords:
    #check length with len function
    if(len(password)) < 8:
        print(f"{password} is too short")
        #add to non-compliant counter
        non_compliant += 1
        #skip rest of the iteration if non compliant
        continue
        #same as above, different check function
    elif not any(c.islower() for c in password):
        print(f"{password} contains no lowercase")
        non_compliant += 1
        continue
        #same as above, different check function
    elif not any(c.isupper() for c in password):
        print(f"{password} contains no uppercase")
        non_compliant += 1
        continue
        #same as above, different check function
    elif not any(c.isdigit() for c in password):
        print(f"{password} contains no digits")
        non_compliant += 1
        continue
        #if all checks are passed, print password with "valid" message and add to compliant counter
    else:
        print(f"password {password} is valid")
        compliant += 1
print(f"total: {compliant} compliant passwords and {non_compliant} non compliant passwords")