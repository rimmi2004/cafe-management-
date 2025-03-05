# Define the restaurant menu
menu = {
    "pizza": 400,
    "garlic bread": 120,
    "salad": 220,
    "mojito": 140,
    "burger": 232,
    "pasta": 330,
    "coffee": 100
}

# Greet the customer
print("WELCOME TO OUR CAFE")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs {price}")

order_total = 0

# Ordering process in a loop
while True:
    item = input("\nEnter the name of the item you want to order: ").strip().lower()
    
    if item in menu:
        order_total += menu[item]
        print(f"{item.capitalize()} has been added to your order.")
    else:
        print("Sorry, the item is not available in our menu. Please choose from the menu.")

    another_order = input("Would you like to order something else? (yes/no): ").strip().lower()
    if another_order != "yes":
        break

# Display total amount
print(f"\nTotal amount to pay: Rs {order_total}")

# Payment method
payment_method = input("Would you like to pay by Cash or Card? ").strip().lower()
if payment_method in ["cash", "card"]:
    print(f"Thank you for your payment by {payment_method.capitalize()}. Enjoy your meal!")
else:
    print("Invalid payment method. Please pay at the counter.")
