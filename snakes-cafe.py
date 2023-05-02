print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print("** To quit at any time, type 'quit' **")
print("**************************************")

menu = {
    "appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "desserts": ["Ice Cream", "Cake", "Pie"],
    "drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

order = {}

print("\n".join(["\n{}:\n{}".format(k.capitalize(), "\n".join(
    ["- {}".format(i) for i in v])) for k, v in menu.items()]))

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

while True:
    customer_order = input("> ")

    if customer_order.lower() == "quit":
        print("Exiting")
        break

    found = False
    for k, v in menu.items():
        if customer_order.capitalize() in v:
            found = True
            if customer_order in order:
                order[customer_order] += 1
            else:
                order[customer_order] = 1
            print(
                f"** {order[customer_order]} order(s) of {customer_order} has been added to your meal **")
            break

    if not found:
        print(
            f"** Sorry, {customer_order} is not on our menu. Please try again. **")

if order:
    print("\nYour order summary:")
    for item, quantity in order.items():
        print(f"{quantity} {item}")
else:
    print("You did not order anything.")
