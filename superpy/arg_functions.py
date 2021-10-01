import os
import csv
import pandas as pd
import argparse
from datetime import datetime
from helpers import getID, global_date, csv_to_temporary_list
from pandas.io.parsers import read_csv

dir_path = os.getcwd()
data_paths = f'{dir_path}/data/'

"""
[INVENTORY]
"""
class Inventory():
    def __init__(self):
        self.inventory_path = os.path.join(data_paths, 'inventory.csv')
        self.expiration_path = os.path.join(data_paths, 'expiration.csv')
    
    def options(self, option):
        if option == 'show':
            with open(self.inventory_path, newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    print(row)

    """
    [REMOVE]
    """
    def remove_products(self):
        data = []
        exp_data = [] 
        current_date = global_date(time=0)
        this_date = datetime.strptime(current_date, "%d/%m/%Y").date()
        with open(self.inventory_path, 'r', newline='') as csv_file:    
            reader = csv.reader(csv_file)
            list_reader = list(reader)

            for row in list_reader:
                exp_date_format = datetime.strptime(row[3], "%d/%m/%Y").date()
                print(exp_date_format)
                if this_date != exp_date_format and this_date < exp_date_format:
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


"""
[BUY]
"""
class Bought():
    def __init__(self):
        self.bought_path = os.path.join(data_paths, 'bought.csv')
    
    def buy(self, product_name, amount, buy_price, exp_date):
        with open(self.bought_path, 'a', newline='') as csv_file:
            id_product = getID(product_name)
            writer = csv.writer(csv_file)
            new_exp_date = datetime.strftime(exp_date, "%d/%m/%Y")
            writer.writerow([id_product, product_name, amount, buy_price, new_exp_date])
        csv_file.close()

"""
[SELL]
"""
class Sold():
    def __init__(self):
        self.sold_path = os.path.join(data_paths, 'sell.csv')
    
    def check_if_exists(self, product_name):
        inventory_path = super_inventory.inventory_path

        with open(inventory_path, newline='') as inv_file:    
            reader = csv.reader(inv_file)
            list_reader = list(reader)
            for row in list_reader:
                if product_name == row[1]:
                        id_product = row[0]
                        self.sell_id = id_product
                        self.sell_amount = row[2]
                        return product_name
                else:
                    msg = "Product not in inventory"
                    raise argparse.ArgumentTypeError(msg)

    def sell(self, product_name, amount, sell_price, sell_date):
        with open(self.sold_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            id_product = self.sell_id
            new_sell_date = datetime.strftime(sell_date, "%d/%m/%Y")

            if amount > float(self.sell_amount):
                msg = "Product amount not in inventory"
                raise argparse.ArgumentError(msg)                
                
            writer.writerow([id_product, product_name, amount, sell_price, new_sell_date])
        csv_file.close()


"""
[REVENUE]
"""
def getProfit(options):
    price_a = csv_to_temporary_list('get_amount', super_sold.sold_path)
    price_b = csv_to_temporary_list('get_amount', super_bought.bought_path)

    if options == 'revenue':
        print(price_a)
    if options == 'costs':
        print(price_b)
    if options == 'profit':
        print(price_a - price_b)

"""
[CONVERT]
"""
def conversion(t):
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


"""
[UPDATE]
def -> auto update new lists based on buy, sell, discarded list
    compare lists to [INVENTORY],
    rewrite [INVENTORY] list
    clear all other lists after
"""
def auto_update(options):
    temp_inventory = csv_to_temporary_list('create_list', super_inventory.inventory_path)
    temp_bought = csv_to_temporary_list('create_list', super_bought.bought_path)
    temp_sold = csv_to_temporary_list('create_list', super_sold.sold_path)

    empty_list = []

    if options == 'sell':
        new_inventory = []
        sell_id_col = [item[0] for item in temp_sold]
        inven_amount_col = [item[2] for item in temp_inventory]
        inven_exp_date_col = [item[-1:] for item in temp_inventory]
        inven_id_col = [item[0] for item in temp_inventory]
        for item in temp_sold:
            if item[0] in inven_id_col:
                # print(temp_inventory[inven_id_col.index(item[0])], item)
                new_amount = int(inven_amount_col[inven_id_col.index(item[0])]) - int(item[2])
                old_exp_date = inven_exp_date_col[inven_id_col.index(item[0])]
                print(old_exp_date)
                if new_amount > 0:
                    new_product = [item[0], item[1], str(new_amount), old_exp_date]
                    new_inventory.append(new_product)
        for item in temp_inventory:
            if item[0] not in sell_id_col:
                new_inventory.append(item)
        print(new_inventory)

        with open(super_sold.sold_path, 'w', newline='') as _file:
            writer = csv.writer(_file)
            writer.writerows(empty_list)
        _file.close()

    if options == 'buy':
        new_inventory = []
        inven_amount_col = [item[2] for item in temp_inventory]
        inven_exp_date_col = [item[-1:] for item in temp_inventory]
        inven_id_col = [item[0] for item in temp_inventory]
        buy_id_col = [item[0] for item in temp_bought]
        for item in temp_bought:
            if item[0] in inven_id_col:
                # print(temp_inventory[inven_id_col.index(item[0])], item)
                new_amount = int(inven_amount_col[inven_id_col.index(item[0])]) + int(item[2])
                new_product = [item[0], item[1], str(new_amount), item[4]]

                new_inventory.append(new_product)
        for item in temp_bought:
            if item[0] not in inven_id_col:
                new_inventory.append(item)
        for item in temp_inventory:
            if item[0] not in buy_id_col:
                new_inventory.append(item)
        print(new_inventory)

        with open(super_bought.bought_path, 'w', newline='') as _file:
            writer = csv.writer(_file)
            writer.writerows(empty_list)
        _file.close()

    with open(super_inventory.inventory_path, 'w', newline='') as inv_file:
        writer = csv.writer(inv_file)
        writer.writerows(new_inventory)
    inv_file.close()



