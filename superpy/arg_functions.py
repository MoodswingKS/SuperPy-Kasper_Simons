import os
import csv
import argparse
from datetime import datetime

this_date = datetime.now().date()

class Inventory():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.inventory_path = os.path.join(data_paths, 'inventory.csv')
    
    def options(self, option):
        # check inventory
        if option == 'show':
            if os.path.isfile(self.inventory_path):
                with open(self.inventory_path, newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader, None)
                    for row in reader:
                        print(row)

# both next classes need to do a check on inventory before adding their items to find a possible id
class Bought():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.bought_path = os.path.join(data_paths, 'bought.csv')
    
    def buy(self, product_name, amount, buy_price, exp_date):
        if os.path.isfile(self.bought_path):
            with open(self.bought_path, 'w', newline='') as csv_file:
                id_product = getID(product_name)
                writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
                writer.writerow([id_product, product_name, amount, buy_price, exp_date])
            csv_file.close()
    # i should change inventory csv based on buying

        

class Sold():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.sold_path = os.path.join(data_paths, 'sell.csv')
    
    def sell(self, product_name, amount, sell_price, exp_date):
        if os.path.isfile(self.sold_path):
            with open(self.sold_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
                id_product = getID(product_name)
                writer.writerow([id_product, product_name, amount, sell_price, exp_date])
            csv_file.close()
    # I should change inventory csv after selling an item

def getID(product_name):
    dir_path = os.getcwd()
    data_paths = f'{dir_path}/data/'
    inventory_path = os.path.join(data_paths, 'inventory.csv')
    
    if os.path.isfile(inventory_path):
        with open(inventory_path, newline='') as csv_file:
            reader = csv.reader(csv_file)
            list_reader = list(reader)
            for row in list_reader:
                if product_name == row[1]:
                    return print(row[0])
            else:
                return len(list_reader) + 1

def remove_products(day):
    dir_path = os.getcwd()
    data_paths = f'{dir_path}/data/'
    inventory_path = os.path.join(data_paths, 'inventory.csv')
    remove_list = []

    if os.path.isfile(inventory_path):
        with open(inventory_path, newline='') as csv_file:    
            reader = csv.reader(csv_file)
            list_reader = list(reader)
            for row in list_reader:
                if day == row[3]:
                    remove_list.append(row)
        # with open(inventory_path, 'w', newline='') as csv_file:
        #         writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        #         writer.
        #     csv_file.close()
    

def valid_date(s):
    try:
        return datetime.strptime(s, "%d-%m-%y")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def timeLapse():
    # include function that buys stuff with time 
    # find product based on id in inventory, and buy something or / and sell something by random?
    # change the csv on variables 
    pass


super_inventory = Inventory()
super_bought = Bought()
super_sold = Sold()