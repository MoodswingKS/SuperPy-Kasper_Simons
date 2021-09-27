import os
import csv
import pandas as pd
import argparse
from datetime import date, datetime, timedelta

from pandas.io.parsers import read_csv


"""
[INVENTORY]
class -> check the list
def CHECK ID
def CHECK PRODUCT_NAME
"""
class Inventory():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.inventory_path = os.path.join(data_paths, 'inventory.csv')
        self.expiration_path = os.path.join(data_paths, 'expiration.csv')
    
    def options(self, option):
        if option == 'show':
            if os.path.isfile(self.inventory_path):
                with open(self.inventory_path, newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader, None)
                    for row in reader:
                        print(row)

    """
    [REMOVE]
    def -> remove product if expired
    check [INVENTORY list] on expiration_date
        if day != exp_date or day < exp_date
            make new inventory list with only these rows
        else:
            print rows to csv with discarded items report
    """
    
    def remove_products(self):
        data = []
        exp_data = []
        # filter inventory  
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
class -> check the list
check product_name on [INVENTORY check product_name]
    if exists, change amount
write report on new products
"""

class Bought():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.bought_path = os.path.join(data_paths, 'bought.csv')
    
    def buy(self, product_name, amount, buy_price, exp_date):
        if os.path.isfile(self.bought_path):
            with open(self.bought_path, 'a', newline='') as csv_file:
                id_product = getID(product_name)
                writer = csv.writer(csv_file)
                writer.writerow([id_product, product_name, amount, buy_price, exp_date])
            csv_file.close()


"""
[SELL]
class -> check the list
check product_name on [INVENTORY check product_name]
    if exists, check id and amount
    if amount correct, change to new amount
write to report
"""

class Sold():
    def __init__(self):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.sold_path = os.path.join(data_paths, 'sell.csv')
    
    def check_if_exists(self, product_name, random_def):
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
                if amount > float(self.sell_amount):
                    msg = "Product amount not in inventory"
                    raise argparse.ArgumentError(msg)                
                
                writer.writerow([id_product, product_name, amount, sell_price, sell_date])
            csv_file.close()


"""
[ADVANCE TIME]
def -> define what today is and move forward in time

"""

"""
[REVENUE]
"""

def getProfit(options):
    price_a = 0
    price_b = 0
    if os.path.isfile(super_sold.sold_path):
        with open(super_sold.sold_path, newline='') as sold_file:    
            reader = csv.reader(sold_file)
            list_reader = list(reader)
            for row in list_reader:
                total = float(row[2]) * float(row[3])
                price_a += total
            sold_file.close()

    if os.path.isfile(super_bought.bought_path):
        with open(super_bought.bought_path, newline='') as bought_file:
            reader = csv.reader(bought_file)
            list_reader = list(reader)
            for row in list_reader:
                total = float(row[2]) * float(row[3])
                price_b += total
            bought_file.close()

    if options == 'revenue':
        print(price_a)
    if options == 'costs':
        print(price_b)
    if options == 'profit':
        print(price_a - price_b)
        
"""
[UPDATE]
def -> auto update new lists based on buy, sell, discarded list
    compare lists to [INVENTORY], 
    rewrite [INVENTORY] list
    clear all other lists after
"""
def auto_update(options):
    # options: buy sell
    data = []
    new_list = []
    # create the new list
    # create the data
    # change amount in new list with data amount
    # if amount == 0, remove item
    # write new_list to inv_file

    if os.path.isfile(super_inventory.inventory_path):
            with open(super_inventory.inventory_path, newline='') as new_file:    
                reader = csv.reader(new_file)
                list_reader = list(reader)
                for row in list_reader:
                    new_list.append(row)
            new_file.close()

    # if options == 'buy':
    #     if os.path.isfile(super_bought.bought_path):
    #         with open(super_bought.bought_path, newline='') as buy_file:    
    #             reader = csv.reader(buy_file)
    #             list_reader = list(reader)
    #             for row in list_reader:
    #                 data.append(row)
    #         buy_file.close()
    #         with open(super_bought.bought_path, 'w', newline='') as buy_file_new:    
    #             writer = csv.writer(buy_file_new)
    #             writer.writerows("")
    #         buy_file_new.close()

    if options == 'sell':
        if os.path.isfile(super_sold.sold_path):
            with open(super_sold.sold_path, 'r', newline='') as sell_file:    
                reader = csv.reader(sell_file)
                list_reader = list(reader)
                for row in list_reader:
                    data.append(row)
            sell_file.close()
            with open(super_bought.bought_path, 'w', newline='') as sell_file_new:    
                # sell_file_new.truncate()
                # need to find out how to clear csv
                pass
            sell_file_new.close()

        new_inventory = []
        for obj in new_list:
            for item in data:
                if obj[1] == item[1]:
                    new_amount = int(obj[2]) - int(item[2])
                    if new_amount < 1:
                        obj[2] = new_amount
                        new_inventory.append(obj)
                    # else:
                    #     new_inventory.remove(obj)
                
        print(new_inventory)


        with open(super_inventory.inventory_path, 'w', newline='') as inv_file:    
            writer = csv.writer(inv_file)
            writer.writerows("")
            writer.writerows(new_inventory)
        inv_file.close()
                

    # inv_file.close()
    
    # check if match in inventory
    # make new inventory list with or without the item or change item amount
    # empty match list (sold, bought)



"""
[CONVERT]
def -> convert to json or html 
"""
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

"""
[CREDITS]
def -> print credits
    AT THE END, CHANGE HELP PARSERS EVERYWHERE!
"""

"""
[OTHER FUNCTIONS]
getID to retrieve id
    if product exists, change product amount
    if not, give a new id with length list + 1

check if date is valid in parser arguments
"""
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
                    return row[0]
            else:
                return len(list_reader) + 1


# CHECK IF DATE IS VALID IN PARSER ARGUMENTS
def valid_date(s):
    try:
        return datetime.strptime(s, "%d-%m-%Y").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

super_inventory = Inventory()
super_bought = Bought()
super_sold = Sold()

def global_date(time=int):
    dir_path = os.getcwd()
    time_file = os.path.join(dir_path, 'time.txt')

    if time == 0:
        with open(time_file, mode='r') as c_date:
            for line in c_date:
                return line[-10:]

    else:
        with open(time_file, mode='r+') as current_date:
            for line in current_date:
                text = line[-10:]
                old_date = datetime.strptime(text, '%d/%m/%Y')
                new_date = old_date + timedelta(days=time)
                write_date = datetime.strftime(new_date, '%d/%m/%Y')
                current_date.write(write_date)
                print(write_date)
                return write_date
        current_date.close()





