# Question 1
# Build a Shopping Cart
# Should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a list
# 3) User can add or delete items
# 4) User can see current shopping list
# 5) Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

def shopping_cart():
    # Make an empty cart list
    cart_list = []
    # Set valid commands to be accepted
    valid_cart_commands = ['add','remove','see','exit', 'empty']
    # Set a flag to break out of while loop
    done = False
    while not done:
        user_input = input("Would you like to add items, remove items, see contents, empty cart or exit shopping cart? ").lower()
        # Check for user input against acceptable commands
        if user_input in valid_cart_commands:
            if user_input == 'add':
                items = input("What would you like to add to the cart? ")
                cart_list.append(items)
                continue
            elif user_input == 'remove':
                remove_item = input("What would you like to remove from the cart? ")
                if remove_item in cart_list:
                    cart_list.pop(cart_list.index(remove_item))
                    print(f'{remove_item} has been removed from the cart ')
                else:
                    print(f'{remove_item} is not in the cart.')
            elif user_input== 'empty':
                if len(cart_list) == 0:
                    print("The cart is already empty")
                else:
                    cart_list.clear()
                    print("The cart has been emptied")
            elif user_input == 'see':
                if len(cart_list) == 0:
                    print("There's nothing in the cart.")
                else:
                    print(f'Here are the contents of your shopping cart: {cart_list}')
                    continue
            elif user_input == 'exit':
                if len(cart_list) == 0:
                    print("Thank you for checking out our store.")
                else:
                    print("Thank you for shopping with us!")
                done = True
        # Print message if user enters invalid input
        else:
            print("Please enter a valid option!")
            continue
    # Check if there is anything in the cart and display message accordingly
    if len(cart_list) == 0:
        print("We hope you find what you were looking for next time.")
    else:
        print(f'Here are the contents of your shopping cart: {cart_list}')


shopping_cart()