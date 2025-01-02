#Define the menu of Cafe
menu = {
    'Coco Cola': 35,
    'Pizza': 99,
    'Burger': 120,
    'Sandwiches': 20,
    'Coffee': 80,
    'Tea': 30,
    'Soups': 50,
    'Pastries' : 60,
    'Salads': 70,
}

#Greet
print("Welcome to Canvas Cafe")
print("1.Coco Cola: Rs 35\n2.Pizza: Rs 99\n3.Burger: Rs 120\n4.Sandwiches: Rs 20\n5.Coffee: Rs 80\n6.Tea: Rs 30\n7.Soups: Rs 50\n8.Pastries : Rs 60\n9.Salads: Rs 70")

order_total = 0

# Loop to take multiple order
while True:
    item_1 = input("Enter the item you want to order: ")
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order")
    else:
        print("Sorry Sir/Ma'am, Ordered item {item_1} is not available yet!")

# Ask if they want to add another item
    Another_order = input("Do you want to add another item? (yes/no): ")
    if Another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")
print("Have a nice day Sir/Ma'am.")


