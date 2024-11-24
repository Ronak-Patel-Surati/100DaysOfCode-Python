# This project is about make a CLi shopping cart project for pro linux users

foods = []
prices = []
total = 0

print("Press q to exit")
while True:
    food = input("Enter a Food/product to buy: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("---- Your Cart ----")

for food in food:
    print(food, end=" ")
for price in prices:
    total += price

print(f"\nYour Total is: ${total}")
