#create list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#skip print step if number is divisible by 2
for number in numbers:
    if number % 2 != 0:
        continue
    print(number)