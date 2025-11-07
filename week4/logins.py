#create list for usernames & logins
login_attempts = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

fails = {}
print("checking login attempts")

#creates loop for each line in login_attempts
for username, status in login_attempts:
    #check for failiures in second slot of tuple (line)
    if status == "failed":
        #checks if it is the first recorded failiure, create new entry if not
        if username in fails:
            fails[username] += 1
        else:
            fails[username] = 1

#creates loop for each entry of fails
for username in fails:
    #check if more than 3 failed attempts happened & prints accordingly
    if fails[username] >= 3:
        print(f"dangerous logon by user {username}")
    else:
        print(f"no danger detected by user {username}, despite failiure")
print("check done")