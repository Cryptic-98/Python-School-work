# creating a dictionary
country_capitals = {
    'South Africa': 'Pretoria',
    'New Zealand': 'Auckland',
    'Zambia': 'Lusaka'
}
# in this case South Africa is the key, and Pretoria is the value. ↑
# accessing elements of a dictionary ↓
print(country_capitals)
# or access using the key value:
print(country_capitals['South Africa'])
print(country_capitals['Zambia'])
# adding an item to a dictionary
country_capitals['Germany'] = 'Berlin'
country_capitals['Russia'] = 'Moscow'
print(country_capitals)
# iterating values using a loop
for country in country_capitals:
    print(country)
for capital in country_capitals:
    print(country_capitals[capital])

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


def main():
    print('Welcome to your Simple Inventory System')
    userChoice = input('Enter action: ').strip().lower()
    print('1. View Products')
    print('2. Add a product')
    print('3. Update a product')
    print('4. View product prices')
    print('5. View total value of products')
    print('Press Q to quit')
    while userChoice not in [1, 2, 3, 4, 'q']:
        print('Invalid Entry. Please choose the following options: \n [1, 2, 3, 4, q]')


def view_product():
    for product, quantity in product_quantities.items():
        print(f'{product}: \nNumber of items: {quantity}')


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
        print('Product unavailable')
        return
    new_quantity = input('New quantity: ')
    product_quantities[select_product] = new_quantity
    print(f'Quantity for {select_product} updated to {new_quantity}')


def total_value():
    for item in product_quantities:
        if item in product_prices:
            value = product_quantities[item] * product_prices[item]
            print(f'{item}: R {value}')
        else:
            print(f'No price set for {item}')

# ask user number of items they want to enter [for loop]
# append to the dictionary
