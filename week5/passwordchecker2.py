import random
#[]

def check_min_length(password, min_len=8): 
    if len(password) > min_len:
       return True
    else:
        return False
    
def has_uppercase(password):
    if any(c.isupper() for c in password):
       return True
    else:
        return False
    
def has_lowercase(password):
    if any(c.islower() for c in password):
       return True
    else:
        return False
    
def has_digitcase(password):
    if any(c.isdigit() for c in password):
       return True
    else:
        return False
    
def has_special_char(password):
    specials = "!@#$%^&*()-_=+.:;,~'´`˜}{§/|¬”#£ﬁ^\·¯˙˚[]’—÷˛“^°"
    if any(c in specials for c in password):
        return True
    else:
        return False

def validation(password):
    is_valid = False
    dict = {}
    length = False
    upper = False
    lower = False
    digit = False
    special = False

    if check_min_length(password, 8):
        dict[length] = True
        print(f"password {password} is of sufficient length")
    else:
        print(f"password {password} is not of sufficient length")
        dict[length] = False

    if has_uppercase(password):
        dict[upper] = True
        print(f"password {password} contains an uppercase letter")
    else:
        print(f"password {password} does not contain an uppercase letter")
        dict[upper] = False

    if has_lowercase(password):
        dict[lower] = True
        print(f"password {password} contains a lowercase letter")
    else:
        print(f"password {password} does not contain a lowercase letter")
        dict[lower] = False

    if has_digitcase(password):
        dict[digit] = True
        print(f"password {password} contains a digit")
    else:
        print(f"password {password} does not contain a digit")
        dict[digit] = False

    if has_special_char(password):
        dict[special] = True
        print(f"password {password} contains a special character")
    else:
        print(f"password {password} does not contain a special character")
        dict[special] = False

    if all(dict.values()):
        is_valid = True
        print(f"this password ({password}) is strong")
    else:
        print(f"this password ({password}) is weak")
    
    encouragement(is_valid)

def encouragement(is_valid):
    positive_responses = [
    "Great job! Your password is strong",
    "Nice! That password is unbruteforceable",
    "Excellent choice — looks secure",
    "Top tier password!",
    "Perfect! Your password passes all checks"
    ]

    negative_responses = [
        "Hmm... that password looks weak",
        "Try adding more variety",
        "Too short or simple.",
        "That one’s easy to guess",
        "Nope, that password needs work"
    ]
    if is_valid:
        print(random.choice(positive_responses))
    else:
        print(random.choice(negative_responses))



print("your password: ")
validation(input())
