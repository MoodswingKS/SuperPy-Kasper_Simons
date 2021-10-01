import os
import csv
from datetime import datetime, timedelta
import argparse
dir_path = os.getcwd()
data_paths = f'{dir_path}/data/'

"""
getID to retrieve id
"""


def getID(product_name):
    inventory_path = os.path.join(data_paths, 'inventory.csv')
    buy_path = os.path.join(data_paths, 'bought.csv')
    count = 0

    with open(buy_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        list_reader = list(reader)
        if len(list_reader) < 1:
            return '1'
        for row in list_reader:
            if product_name == row[1]:
                return row[0]
        count = len(list_reader)
    csv_file.close()
    with open(inventory_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        list_reader = list(reader)
        for row in list_reader:
            if product_name == row[1]:
                return row[0]
        return len(list_reader) + count + 1
    



# CHECK IF DATE IS VALID IN PARSER ARGUMENTS
def valid_date(s):
    try:
        return datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


"""
[ADVANCE TIME]
"""


def global_date(time=int):
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

"""
Helper function that 'does' something with a csv file
"""
def csv_to_temporary_list(action, csv_file_name):
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

