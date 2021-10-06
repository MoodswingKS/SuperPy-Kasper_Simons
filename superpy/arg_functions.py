import os
import csv
import pandas as pd
import argparse
from datetime import datetime
from helpers import getID, global_date, csv_to_temporary_list
from pandas.io.parsers import read_csv

dir_path = os.getcwd()
data_paths = f'{dir_path}/data/'

class Inventory():
    """
    [INVENTORY]
    """
    def __init__(self):
        self.inventory_path = os.path.join(data_paths, 'inventory.csv')
        self.expiration_path = os.path.join(data_paths, 'expiration.csv')
    
    def options(self, option):
        if option == 'show':
            temp_inv = csv_to_temporary_list('create_list', self.inventory_path)
            for row in temp_inv:
                print(row)
            return ''
    
    def update(self, options, updated_product):
        """
        [UPDATE]
        after buy / sell

        [BUY]:    check if exists, on id
                if exists, adjust new amount
                if not, add product

        [SELL]:   check id
                adjust amount
                if amount <= 1 change amount
                otherwise remove product
        
        """
        new_inventory = []
        temp_inventory = csv_to_temporary_list('create_list', 'inventory.csv')

        _id_col = [item[0] for item in temp_inventory]
        if options == 'buy' and updated_product[0] not in _id_col: 
            # when its a new product
            new_product = [updated_product[0], updated_product[1], updated_product[2], updated_product[-1]]
            new_inventory.append(new_product)
            
        for item in temp_inventory:
            if item[0] == updated_product[0]:
                # adjust amount and append
                if options == 'buy':
                    new_amount = int(item[2]) + int(updated_product[2])
                    new_product = [item[0], item[1], str(new_amount), item[-1]]
                    new_inventory.append(new_product)
                if options == 'sell':
                    # check value new amount
                    new_amount = int(item[2]) - int(updated_product[2])
                    if new_amount >= 1:
                        # if less than 1, the product doesn't need to be in inventory anymore
                        new_product = [item[0], item[1], str(new_amount), item[-1]]
                        new_inventory.append(new_product)
            else:
                new_inventory.append(item)
   
        with open(super_inventory.inventory_path, 'w', newline='') as inv_file:
            writer = csv.writer(inv_file)
            writer.writerows(new_inventory)
        inv_file.close()

    def remove_products(self):
        """
        [REMOVE]
        """
        data = []
        exp_data = [] 
        current_date = global_date('none')
        this_date = datetime.strptime(current_date, "%d/%m/%Y").date()
        with open(self.inventory_path, 'r', newline='') as csv_file:    
            reader = csv.reader(csv_file)
            list_reader = list(reader)

            for row in list_reader:
                exp_date_format = datetime.strptime(row[-1], "%d/%m/%Y").date()
                print(exp_date_format)
                if this_date != exp_date_format and this_date <= exp_date_format:
                    data.append(row)
                else:
                    exp_data.append(row)
        csv_file.close()
        print(data)
        # write filtered products that have expired
        with open(self.expiration_path, 'a', newline='') as exp_file:
            writer = csv.writer(exp_file)
            writer.writerows(exp_data)
        exp_file.close()
        # rewrite inventory with non-expired
        with open(self.inventory_path, 'w', newline='') as new_csv_file:    
            writer = csv.writer(new_csv_file)
            writer.writerows(data)
        new_csv_file.close()

class Bought():
    """
    [BUY]
    """
    def __init__(self):
        self.bought_path = os.path.join(data_paths, 'bought.csv')
    
    def buy(self, product_name, amount, buy_price, exp_date):
        with open(self.bought_path, 'a', newline='') as csv_file:
            id_product = getID(product_name, exp_date)
            writer = csv.writer(csv_file)
            new_exp_date = datetime.strftime(exp_date, "%d/%m/%Y")
            updated_product = [id_product, product_name, amount, buy_price, new_exp_date]
            writer.writerow(updated_product)
            super_inventory.update('buy', updated_product)
        csv_file.close()

class Sold():
    """
    [SELL]
    """
    def __init__(self):
        self.sold_path = os.path.join(data_paths, 'sell.csv')
    
    def check_if_exists(self, product_name):
        inventory_path = csv_to_temporary_list('create_list', 'inventory.csv')
        
        for item in inventory_path:
            if product_name == item[1]:
                id_product = item[0]
                self.sell_id = id_product
                self.sell_amount = item[2]
                return product_name
        msg = "Product not in inventory"
        raise argparse.ArgumentTypeError(msg)

    def sell(self, product_name, amount, sell_price, sell_date):
        with open(self.sold_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            # sell date becomes expiration date in getID?
            id_product = self.sell_id
            new_sell_date = global_date('none')
            if sell_date:
                new_sell_date = datetime.strftime(sell_date, "%d/%m/%Y")
            if amount > float(self.sell_amount):
                msg = "Product amount not in inventory"
                raise argparse.ArgumentError(msg)                
            updated_product = [id_product, product_name, amount, sell_price, new_sell_date]    
            writer.writerow(updated_product)
            super_inventory.update('sell', updated_product)
        csv_file.close()

def getProfit(options):
    """
    [REVENUE]
    """
    price_a = csv_to_temporary_list('get_amount', super_sold.sold_path)
    price_b = csv_to_temporary_list('get_amount', super_bought.bought_path)

    if options == 'revenue':
        print(price_a)
    if options == 'costs':
        print(price_b)
    if options == 'profit':
        print(price_a - price_b)

def conversion(t):
    """
    [CONVERT]
    """
    inventory_path = os.path.join(data_paths, 'inventory.csv')

    json_file = 'inventory.json'
    html_file = 'inventory.html'

    read_file = pd.read_csv(inventory_path)
    if t == 'json':
        read_file.to_json(json_file, orient='records')
    if t == 'html':
        read_file.to_html(html_file, show_dimensions=True)

super_inventory = Inventory()
super_bought = Bought()
super_sold = Sold()
