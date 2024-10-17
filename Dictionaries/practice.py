"""
Practice Question:
You're building a simple inventory management
system. Create a dictionary where keys are
product names and values are corresponding
quantities. Write functions to :
Add new products to the inventory
Update product quantities
Calculate the total value of inventory based
on products prices stored in another dictionary
"""

inventory = {
    'Watch': 15,
    'Bracelet': 50,
    'Cup': 20,
    'Bucket': 10,
    'Plate': 100
}

inventory_prices = {
    'Watch': 300,
    'Bracelet': 20,
    'Cup': 100,
    'Bucket': 50,
    'Plate': 10
}


def add_new_product():
    new_product = input('Enter product: ').strip().capitalize()
    new_product_quantity = int(input('Enter quantity: ').strip())
    inventory[new_product] = new_product_quantity


def update_product():
    updated_product = input('Enter product: ').strip().capitalize()
    if updated_product not in inventory:
        print('Product not in inventory.')
        return
    new_quantity = int(input('Enter new quantity: ').strip())
    inventory[updated_product] = new_quantity


def total_value():
    for item in inventory:
        if item in inventory:
            value = inventory[item] * inventory_prices[item]
            print(f'{item}: R{value}')
        else:
            print('Price not set for this item.')
