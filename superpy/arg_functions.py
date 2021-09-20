import os
import csv

class Products():
    def __init__(self, data_paths):
        dir_path = os.getcwd()
        data_paths = f'{dir_path}/data/'
        self.data_paths = data_paths


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
        # check inventory
        # if os.path.isfile(self.bought_path):
        #     with open(self.bought_path, newline='') as csv_file:
        #         reader = csv.reader(csv_file)
        #         next(reader, None)
        #         for line in reader:
        #             if product_name != line['product_name']:
        #                 product_id = len(line) + 1
        if os.path.isfile(self.bought_path):
            with open(self.bought_path, 'w', newline='') as csv_file:
                count = 100
                writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
                id_product = count + 1
                writer.writerow([id_product, product_name, amount, buy_price, exp_date])
            csv_file.close()

        

class Sold():
    pass

super_inventory = Inventory()
super_bought = Bought()
super_sold = Sold()