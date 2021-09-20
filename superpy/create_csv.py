import csv
import os


def create(csv_file, csv_type):
    dir_path = os.getcwd()
    data_list = f'{dir_path}/data/'
    file = f'{csv_file}.csv'
    file_path = os.path.join(data_list, file)


    with open(file_path, 'w', newline='') as new_file:
        new_csv = csv.writer(new_file)
        if csv_type != 'inventory':
            new_csv.writerows(csv_file)
        else:
            for row in csv_file:
                product = row[0]
                amount = row[1]
                new_csv.writerow([id, product, amount])
    print(f'Succesfully added {file} to {file_path}')

