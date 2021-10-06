import os
import csv
from datetime import datetime, timedelta
import argparse
dir_path = os.getcwd()
data_paths = f'{dir_path}/data/'

def valid_date(s):
    # CHECK IF DATE IS VALID IN PARSER ARGUMENTS
    try:
        return datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def global_date(start, time=int):
    """
    [ADVANCE TIME]
    """
    time_file = os.path.join(dir_path, 'time.txt')

    if start == 'start':
        with open(time_file, mode='r+') as c_date:
            for line in c_date:
                current = datetime.now().date()
                write_date = datetime.strftime(current, '%d/%m/%Y')
                c_date.write(write_date)
                return write_date

    if start == 'none':
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

def csv_to_temporary_list(action, csv_file_name):
    """
    Helper function that 'does' something with a csv file
    """
    temporary_list = []
    csv_path = os.path.join(data_paths, f'{csv_file_name}')
    
    if action == 'create_list':
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            list_reader = list(reader)
            for row in list_reader:
                temporary_list.append(row)
        file.close()
        return temporary_list

    if action == 'get_amount':
        with open(csv_path, newline='') as file:
            amount = 0
            reader = csv.reader(file)
            for row in reader:
                total = int(row[2]) * float(row[3])
                amount += total
        file.close()
        return amount

def get_item_or_max(path, product_name, exp_date):
    """
    return id as a string or an int
    """
    exp_match = datetime.strftime(exp_date, '%d/%m/%Y')
    max_value = 0
    for item in path:
        if product_name == item[1] and exp_match == item[-1]:
            return item[0]
        elif product_name == item[1]:
            new_id = f'{item[0]}{exp_date}'
            new_id_string = new_id.replace('-', '')
            return new_id_string
        max_value = max(item[0])
    return int(max_value) 

def getID(product_name, exp_date):
    """
    return id if exists - or create a new one
    check if name matches bought, check if exp_date matches
    check if name matches inventory, check if exp_date matches
    create a new id based on max value id in inventory and bought
    """
    temp_inventory = csv_to_temporary_list('create_list', 'inventory.csv')
    temp_bought = csv_to_temporary_list('create_list', 'bought.csv')
    value_bought = get_item_or_max(temp_bought, product_name, exp_date)
    value_inv = get_item_or_max(temp_inventory, product_name, exp_date)

    if type(value_bought) == str:
        return value_bought
    elif type(value_inv) == str:
        return value_inv
    
    elif value_bought > value_inv:
        return int(value_bought)+1
    return int(value_inv)+1
        
