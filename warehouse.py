"""
Program: Warehouse control
Author: Ladarius Brooks
Functionality:
    -Register Items
        - id (auto generated): int
        - title: str
        - category: str
        - Stock: int
        - price: float

"""

# imports
from menu import print_menu, clear, print_item, print_header
from item import Item
import pickle



# global vars
catalog = []
last_id = 0
data_file = 'warehouse.data'
# functions

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') #wb => create/overwrite the file
    pickle.dump( catalog, writer)
    writer.close()
    print('Data saved!')

def deserialze_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file, 'rb') #rb => read binary, throw exception if file does not exist
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id + 1

        how_many = len(catalog)
        print(' Deserialized ' + str(how_many) + ' items')
    except:
        print("Error, no data loaded")

def register_item():
    global last_id
    try:
        print_header("Register new Item")
        title = input('Please provide the Title: ')
        category = input('Please provide the Category: ')
        stock = int(input('Please provide the Stock: '))
        price = float(input('Please provide the Price: '))

        the_item = Item(last_id, title, category, stock, price)
        last_id += 1
        # add the obj to the list
        catalog.append(the_item)


        count = len(catalog)
        print(" Item saved, you have " + str(count) + " items in your catalog")

    except ValueError:
        print("*Error, provide valid numbers")
    except:
        print("*Error, verify data and try again!")

def display_catalog():
    print_header("Your catalog")
    for item in catalog:
        print_item(item)

def display_out_of_stock():
    print_header("Items out of stock")
    for item in catalog:
        if(item.stock == 0):
             print_item(item)
        
def total_stock_value():
    print_header("Total stock value")
    total = 0.0
    for item in catalog:
        total += item.stock * item.price

    print('The total is: $' + str(total))

def update_price():
    display_catalog()
    id = input("Please choose an id: ")
    found = False
    for item in catalog:
        if(str(item.id)== id):
            found = True
            price = float(input('Provide new Price $')) # always check data types
            item.price = price

    if(not found):
        print("*Error, invalid Id. Try again.")
    
def delete_item():
    display_catalog()
    id = input("Please choose an id: ")
    found = False
    for item in catalog:
        if(str(item.id)== id):
            found = True
            delete = input("This item will be deleted ")
            if(delete == "ok"):
                catalog.remove(item)
                print("Item has been deleted")
                serialize_catalog()

    if(not found):
        print("*Error, invalid Id. Try again.")


def update_item_stock():
    display_catalog()
    id = input("Please choose an id: ")
    found = False
    for item in catalog:
        if(str(item.id)== id):
            found = True
            stock = int(input('Provide new stock amount ')) # always check data types
            item.stock = stock

    if(not found):
        print("*Error, invalid Id. Try again.")

def display_category():
    print_header("These are your categories")
    temp = []
    for item in catalog:
        if(not item.category in temp):
            temp.append(item.category)
            print(item.category)

def cheap_products():
    print_header("This is your cheapest product")
    cheapest = catalog[0]
    for item in catalog:
        if(item.price < cheapest.price):
            cheapest = item

    print_item(cheapest)
        
def expensive_products():
    print_header("The 3 most expensive products")
    prices = []
    for item in catalog:
        prices.append(item.price)

    prices.sort(reverse=True)

    for item in catalog:
        if(item.price == prices[0]):
            print_item(item)
    
    for item in catalog:
        if(item.price == prices[1]):
            print_item(item)

    for item in catalog:
        if(item.price == prices[2]):
            print_item(item)  

    


# instructions
deserialze_catalog()
input('Press Enter to continue...')



opc = ' '
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')

    if(opc == '1'):
        register_item()
        serialize_catalog()

    elif(opc == '2'):
        # create a function, call, travel the list and display the item.title

        display_catalog()

    elif(opc == '3'):
        # call the fn
        # create the fn
        # if it.stock is equal to 0
        # display_item
        display_out_of_stock()

    elif(opc == '4'):
        total_stock_value()

    elif(opc == '5'):
        update_price()
        serialize_catalog()

    elif(opc == '6'):
        delete_item()

    elif(opc == '7'):
        update_item_stock()
        serialize_catalog()

    elif(opc == '8'):
        display_category()

    elif(opc == '9'):
        cheap_products()

    elif(opc == '10'):
        expensive_products()

    input('Press Enter to continue...')
