# Concession Stand Program
# Store all products and their prices.

menu = {
    1: ("Small Popcorn", 4.00),
    2: ("Medium Popcorn", 5.50),
    3: ("Large Popcorn", 7.00),
    4: ("Caramel Popcorn", 6.50),
    5: ("Chinese Popcorn", 6.50),

    6: ("Small Soda", 2.50),
    7: ("Medium Soda", 3.50), 
    8: ("Large Soda", 4.50),
    9: ("Bottled Water", 2.00),
    10: ("Lemonade", 3.50),
    11: ("Iced Tea", 3.50),

    12: ("Hot Dog", 5.50), 
    13: ("Chili Dog", 6.50),
    14: ("Pretzel", 4.50),
    15: ("Nachos", 6.00),
    16: ("Cheese Nachos", 7.00),
    17: ("Chicken Nuggets", 6.50),

    18: ("Chocolate Bar", 3.00),
    19: ("Gummy Candy", 2.50),
    20: ("Chips", 3.00),
    21: ("Cookies", 3.50),
    22: ("Donut", 3.00),

    23: ("Ice Cream", 4.00),
    24: ("Sundae", 5.00),
    25: ("Churros", 4.50),
    26: ("Brownie", 4.00),

    27: ("Popcorn + Soda", 8.00),
    28: ("Hot Dog + Soda", 9.00),
    29: ("Popcorn + Candy + Soda", 11.00),
    30: ("Nachos + Soda", 8.50)
}

def show_menu():
    # Display the consession stand menu.
    print("\n" + "=" * 55)
    print("                 🎞️ CONCESSION STAND")
    print("=" * 55)

    print("\n🍿 POPCORN")
    for number in range(1, 6):
        name, price = menu[number]
        print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n🥤 DRINKS")
    for number in range(6, 12):
            name, price = menu[number]
            print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n🌭 HOT FOOD")
    for number in range(12, 18):
        name, price = menu[number]
        print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n🍫 CANDY & SNACKS")
    for number in range(18, 23):
        name, price = menu[number]
        print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n🍦 DESSERTS")
    for number in range(23, 27):
        name, price = menu[number]
        print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n🎁 COMBOS")
    for number in range(27, 31):
        name, price = menu[number]
        print(f"{number:2}. {name:<25} ${price:.2f}")

    print("\n 0. Checkout")
    print("=" * 55)

def get_item_choice():
    # Keep asking until the user selects a valid menu item.
    while True:
         try:
              choice = int(input("\nChoose an item: "))

              if choice == 0:
                   return 0
              if choice in menu:
                   return choice

              print("❌ Invalid item number!")

         except ValueError:
              print("❌ Please enter a valid number!")

def get_quantity():
     # Keep asking until the user enters a valid quantity.
     while True:
          try:
               quantity = int(input("Enter quantity: "))

               if quantity > 0:
                    return quantity

               print("❌ Quantity must be greater than zero!")

          except ValueError:
               print("❌ Please enter a whole number!")

def add_to_order(order, choice, quantity):
     # Get the selected product's name and price.
     name, price = menu[choice]

     # Calculate the subtotal for this item.
     subtotal = price * quantity

     # Add the item to the order.
     order.append((name, price, quantity, subtotal))

     print(f"\n✅ Added {quantity} * {name} to your order!")
     print(f"Subtotal: ${subtotal:.2f}")

def show_receipt(order):
     # Display the final receipt as a table.
     print("\n" + "=" * 75)
     print("                           🧾 RECEIPT")
     print("-" * 75)

     total = 0

     for name, price, quantity, subtotal in order:
          print(
               f"{name:<28} "
               f"${price:>8.2f} "
               f"{quantity:>8} "
               f"${subtotal:>12.2f}"
          )

          total += subtotal

     print("-" * 75)
     print(f"{'TOTAL: ':>61} ${total:>10.2f}")
     print("=" * 75)
     print("              Thank you for your order! 🎞️")
     print("=" * 75)

def main():
    # Store all items selected by the customer.
    order = []

    print("\n🍿 Welcome to the Concession Stand! 🍿")

    while True:
        show_menu()

        choice = get_item_choice()

        # Finish the order if the user chooses Checkout.
        if choice == 0:
            break

        quantity = get_quantity()

        add_to_order(order, choice, quantity)

    # Check whether the customer selected anything.
    if not order:
        print("\n❌ Your order is empty.")
        print("Thank you for visiting! 👋🏻")
        return

    show_receipt(order)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
     main()
