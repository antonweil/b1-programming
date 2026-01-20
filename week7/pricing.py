def discount(price, discount_p):
    discount = (price / 100) * discount_p
    final_price = price - discount

    return discount, final_price

str = []
with open("products.txt", "r") as file:

    for line in file:
        str.append(line.split(","))

for i in range (0,len(str),1):
    for j in range (0,len(str)-1,1):
        print(str[i][j])