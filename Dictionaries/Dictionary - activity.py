"""
Practice Question:
Your building a simple inventory management
system. Create a dictionary where keys are
product names and values are corresponding
quantities. Write functions to :
Add new products to the inventory
Update product quantities
Calculate the total value of inventory based
on products prices stored in another dictionary
"""
product_quantities = {
    'Vaseline': 10,
    'Cereal': 5,
    'Posters': 15,
    'Computers': 2
}
product_prices = {
    'Vaseline': 50,
    'Cereal': 70,
    'Posters': 20,
    'Computers': 3500
}


def view_product():
    for product, quantity in product_quantities.items():
        print(f'{product}: \nNumber of items: {quantity}')
    userChoice = input('Press R to return to Main Menu: ').strip().upper()
    while userChoice != 'R':
        print('Invalid Entry')
        userChoice = input('Press R to return to Main Menu: ').strip().upper()
    return main()


def add_product():
    newProduct = input('Enter new product: ').strip().capitalize()
    quantity = input('Enter quantity: ')
    product_quantities[newProduct] = quantity
    userChoice = input('Would you like to add a new product? (y/n): ').strip().lower()
    while userChoice not in ['y', 'n']:
        print('Invalid input. Please enter "y" or "n".')
        userChoice = input('Would you like to add a new product? (y/n): ').strip().lower()
    while userChoice == 'y':
        newProduct = input('Enter new product: ')
        product_quantities[newProduct] = input('Enter quantity: ')
        userChoice = input('Would you like to add a new product? (y/n): ').strip().lower()
        while userChoice not in ['y', 'n']:
            print('Invalid input. Please enter "y" or "n".')
            userChoice = input('Would you like to add a new product? (y/n): ').strip().lower()
    else:
        main()


def update_quantity():
    select_product = input('Item being updated: ').strip().capitalize()
    if select_product not in product_quantities:
        print('Product unavailable. \n\nReturned to Main Menu\n')
        return main()
    new_quantity = input('New quantity: ')
    product_quantities[select_product] = new_quantity
    print(f'Quantity for {select_product} updated to {new_quantity}\n')
    userChoice = input('Press R to return to Main Menu: ').strip().upper()
    while userChoice != 'R':
        print('Invalid Entry')
        userChoice = input('Press R to return to Main Menu: ').strip().upper()
    return main()


def product_price():
    for product, price in product_prices.items():
        print(f'{product}: R {price}')
    userChoice = input('Press R to return to Main Menu: ').strip().upper()
    while userChoice != 'R':
        print('Invalid Entry')
        userChoice = input('Press R to return to Main Menu: ').strip().upper()
    return main()


def total_value():
    for item in product_quantities:
        if item in product_prices:
            value = product_quantities[item] * product_prices[item]
            print(f'{item}: R {value}\n')
            userChoice = input('Press R to return to Main Menu').strip().upper()
            while userChoice != 'R':
                print('Invalid Entry')
                userChoice = input('Press R to return to Main Menu').strip().upper()
            return main()
        print(f'No price set for {item}')
        userChoice = input('Press R to return to Main Menu: ').strip().upper()
        while userChoice != 'R':
            print('Invalid Entry')
            userChoice = input('Press R to return to Main Menu: ').strip().upper()


def main():
    while True:
        print('\n\nWelcome to your Simple Inventory System')
        print('1. View Products')
        print('2. Add a product')
        print('3. Update a product')
        print('4. View product prices')
        print('5. View total value of products')
        print('Press Q to quit')
        userChoice = input('Enter action: ')
        if userChoice == '1':
            view_product()
        elif userChoice == '2':
            add_product()
        elif userChoice == '3':
            update_quantity()
        elif userChoice == '4':
            product_price()
        elif userChoice == '5':
            total_value()
        elif userChoice == 'q':
            print('Exiting...')
            break
        else:
            print('Invalid Entry. Please choose one of the following options: [1, 2, 3, 4, 5, q]')


main()
