import os
import csv
import pandas as pd
import argparse
from datetime import datetime

from pandas.io.parsers import read_csv



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

super_inventory = Inventory()
super_bought = Bought()
super_sold = Sold()

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
    new_list = []

    if os.path.isfile(inventory_path):
        with open(inventory_path, newline='') as csv_file:    
            reader = csv.reader(csv_file)
            list_reader = list(reader)
            writer = csv.writer(new_list)
            for row in list_reader:
                if day != row[3]:
                    writer.writerow(row)
            csv_file = new_list
            csv_file.close()
    
def conversion(t):
    dir_path = os.getcwd()
    data_paths = f'{dir_path}/data/'
    inventory_path = os.path.join(data_paths, 'inventory.csv')

    json_file = 'inventory.json'
    html_file = 'inventory.html'

    read_file = pd.read_csv(inventory_path)
    if t == 'json':
        read_file.to_json(json_file, orient='records')
    if t == 'html':
        read_file.to_html(html_file, show_dimensions=True)

def valid_date(s):
    try:
        return datetime.strptime(s, "%d-%m-%Y")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def timeLapse():
    # include function that buys stuff with time 
    # find product based on id in inventory, and buy something or / and sell something by random?
    # change the csv on variables 
    pass

def auto_update(path):
    new_list = []
    path_to_use = ''
    check_inv = read_csv(super_inventory.inventory_path)
    new_inventory = csv.writer('new_inventory.csv')

    for row in check_inv:
        product = row[1]
        amount_inv = row[2]
        if path == 'buy':
            check_bought = read_csv(super_bought.bought_path)
            path_to_use = check_bought
            for row in check_bought:
                item = row[1]
                if item != product:
                    new_inventory.writerow[row]
                elif item == product:
                    amount = row[2]
                    

        

        # if path == 'sold':
        # check_sold = read_csv(super_sold.sold_path)
        # path_to_use = check_sold
    


    # check if match in inventory
    # make new inventory list with or without the item or change item amount
    # empty match list (sold, bought)

    if len(check_bought) < 1:
        pass

    if len(check_sold) < 1:
        pass

    if len(check_inv) < 1:
        pass

def getProfit(option):
    # function that checks all sold prices * amount
    # checks for buy price in inventory * amount in sell list
    # 
    check_inv = read_csv(super_inventory.inventory_path)
    check_bought = read_csv(super_bought.bought_path)
    check_sold = read_csv(super_sold.sold_path)

    check_inv_rev = 0
    for row in check_inv:
        pass

    if option == 'costs':
        # print(cost_amount)
        pass

     





