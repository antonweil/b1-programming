passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]
#8 chars, 1 upper, 1 lower, 1 digit

compliant = 0
non_compliant = 0

for password in passwords:
    if(len(password)) < 8:
        print(f"{password} is too short")
        non_compliant += 1
        continue
    elif not any(c.islower() for c in password):
        print(f"{password} contains no lowercase")
        non_compliant += 1
        continue
    elif not any(c.isupper() for c in password):
        print(f"{password} contains no uppercase")
        non_compliant += 1
        continue
    elif not any(c.isdigit() for c in password):
        print(f"{password} contains no digits")
        non_compliant += 1
        continue
    else:
        print(f"password {password} is valid")
        compliant += 1
print(f"total: {compliant} compliant passwords and {non_compliant} non compliant passwords")