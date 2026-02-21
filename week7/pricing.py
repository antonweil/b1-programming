value_map = {
    "Electronics":0.1,
    "Clothing":0.15,
    "Books":0.05,
    "Home":0.12,
    "Premium":0.05,
    "Budget":0.02
}
# map values for all applicable discounts


# define discount function, based on price & discount (in percent) => discount & final_price
def discountCalc(price, discount_p):
    discount = price * discount_p
    final_price = price - discount

    return discount, final_price

stri = []
try:
    with open("products.txt", "r") as file:
        for line in file:
            product = tuple(line.strip().split(","))
            stri.append(product)
    print("QUARTERLY FINANCE REPORT")
except FileNotFoundError:
    print("Error: The directory or file was not found.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


entry = []
i = 0
for products in stri:
    name, price, category, level = products
    results = [value_map.get(item) for item in products]
    try:
        discount, final = discountCalc(float(products[1]), float(results[2]))
    except ValueError:
        print(f"Error: {products[1]} or {results[2]} are not valid numbers")
    entry.append((products[0], discount, final))

    output=(f"product name: {entry[i][0]}, final price: {entry[i][2]:.2f}, total discount applied: {entry[i][1]:.2f}\n")
    print(output)
    try:
        if i==0:
            with open("pricing_report.txt", "w") as file:
                file.write("===FINANCIAL REPORT===\n")
        else:
            with open("pricing_report.txt", "a") as file:
                file.write(output)
    except FileNotFoundError:
        print("Error: The directory or file was not found.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    i=i+1