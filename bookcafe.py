import json
import os

# File paths
MENU = 'menu.json'
BOOK = 'books.json'
ORDERS = 'orders.json'

# Load or initialize data
def load_json(file_path, default_data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        with open(file_path, 'w') as f:
            json.dump(default_data, f, indent=2)
        return default_data

menu = load_json(MENU, {
    'food': {'Sandwich': 5.99, 'Cake': 4.50, 'Cookies': 2.99, 'Salad': 6.99},
    'drinks': {'Coffee': 3.50, 'Tea': 2.99, 'Hot Chocolate': 3.99, 'Juice': 2.50}
})

books = load_json(BOOK, {
    'The Great Gatsby': 15.99,
    'To Kill a Mockingbird': 14.99,
    'Pride and Prejudice': 12.99,
    '1984': 13.99
})

orders = load_json(ORDERS, [])

# Save in JSON file
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def display_items():
    print("\n--- Food Menu ---")
    for item, price in menu['food'].items():
        print(f"{item}: £{price:.2f}")
    print("\n--- Drinks Menu ---")
    for item, price in menu['drinks'].items():
        print(f"{item}: £{price:.2f}")
    print("\n--- Books Available ---")
    for book, price in books.items():
        print(f"{book}: £{price:.2f}")

def place_order():
    order = {'food': [], 'drinks': [], 'books': [], 'total': 0}

    for menu_items in ['food', 'drinks']:
        print(f"\n{menu_items.title()} Menu:")
        for item, price in menu[menu_items].items():
            if input(f"Would you like {item} (£{price:.2f})? (yes/no): ").lower() == 'yes':
                order[menu_items].append(item)
                order['total'] += price

    print("\nBooks Available:")
    for book, price in books.items():
        if input(f"Would you like {book} (£{price:.2f})? (yes/no): ").lower() == 'yes':
            order['books'].append(book)
            order['total'] += price

    print("\nEnter contact details:")
    order['name'] = input("Full Name: ")
    order['address'] = input("Address: ")
    order['phone'] = input("Phone: ")

    orders.append(order)
    save_json(ORDERS, orders)
    print(f"\nOrder successfully placed! Total: £{order['total']:.2f}")

def update_menu():
    print("\n1. Add Item\n2. Remove Item")
    choice = input("Choose an option: ")
    menu = input("food or drinks: ").lower()

    if update_menu not in menu:
        print("Invalid menu")
        return

    if choice == '1':
        item = input("Item name: ")
        price = float(input("Price(£): "))
        menu[update_menu][item] = price
        print("Item added")
    elif choice == '2':
        item = input("Item to remove: ")
        if item in menu[update_menu]:
            del menu[update_menu][item]
            print("Item removed")
        else:
            print("Item not found")

    save_json(MENU, menu)

def view_orders():
    if not orders:
        print("\nNo orders taken yet")
        return

    for i, order in enumerate(orders, 1):
        print(f"\nOrder #{i} - {order['name']}")
        print(f"Address: {order['address']}")
        print(f"Phone: {order['phone']}")
        if order['food']: print("Food:", ', '.join(order['food']))
        if order['drinks']: print("Drinks:", ', '.join(order['drinks']))
        if order['books']: print("Books:", ', '.join(order['books']))
        print(f"Total: £{order['total']:.2f}")

def main():
    print(r"""
        (( ((
          )) ))
        ..........
        | Book   |]
        |  Café  |]
        |___APP__|
         |      |
        (________)
            """)
    while True:
        print("1. Customer\n2. Employee\n3. Exit")
        choice = input("Select: ")

        if choice == '1':
            while True:
                print("\n**** Customer Menu ****")
                print("1. View Menu and Books\n2. Place Order\n3. Back")
                c = input("Choose: ")
                if c == '1': display_items()
                elif c == '2': place_order()
                elif c == '3': break
        elif choice == '2':
            while True:
                print("\n**** Employee Menu ****")
                print("1. Update Menu\n2. View Orders\n3. Back")
                e = input("Choose: ")
                if e == '1': update_menu()
                elif e == '2': view_orders()
                elif e == '3': break
        elif choice == '3':
            print("\n****Thank you and visit Book Cafe App again soon!****\n")
            break
        else:
            print("Invalid input")

if __name__ == main():
    main(__name__)