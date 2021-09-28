import os
import csv
import pandas as pd
import argparse
from datetime import datetime
from helpers import getID, global_date
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
            if os.path.isfile(self.inventory_path):
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
        if os.path.isfile(self.inventory_path):
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
        if os.path.isfile(self.expiration_path):
            with open(self.expiration_path, 'a', newline='') as exp_file:
                writer = csv.writer(exp_file)
                writer.writerows(exp_data)
            exp_file.close()
        # rewrite inventory with non-expired
        if os.path.isfile(self.inventory_path):
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
        if os.path.isfile(self.bought_path):
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

        if os.path.isfile(inventory_path):
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
        if os.path.isfile(self.sold_path):
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
    price_a = 0
    price_b = 0
    if os.path.isfile(super_sold.sold_path):
        with open(super_sold.sold_path, newline='') as sold_file:    
            reader = csv.reader(sold_file)
            for row in reader:
                total_a = int(row[2]) * float(row[3])
                price_a += total_a
            sold_file.close()

    if os.path.isfile(super_bought.bought_path):
        with open(super_bought.bought_path, newline='') as bought_file:
            reader = csv.reader(bought_file)
            for row in reader:
                total = int(row[2]) * float(row[3])
                price_b += total
            bought_file.close()

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







