import random
mattempts = 10
attempts = 0
score = 0

while attempts < mattempts:
    num = random.randint(0,10)
    print("your guess:")
    guess = int(input())
    if guess == num:
        print("you did it")
        score += 1
    else:
        print ("wrong :(")
    print("your score ", score)
    attempts +=1
    print("correct:", num)
