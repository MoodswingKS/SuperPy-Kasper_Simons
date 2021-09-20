# Imports
import argparse
# from datetime import date
from arg_functions import super_inventory, super_bought, super_sold
from create_csv import create


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


def main():
    # global parser init
    parser = argparse.ArgumentParser(description="SUPERPY")
    
    mainparsers = parser.add_subparsers(dest='options')
    mainparsers.required = True
    
    # buy parser
    buy_parser = mainparsers.add_parser('buy', help="Buy products")
    buy_parser.add_argument('--product', type=str, help='product name', required=True)
    buy_parser.add_argument('--amount', type=int, help='product amount', default=1)
    buy_parser.add_argument('--buy_price', type=float, help='buy price per product', required=True)
    buy_parser.add_argument('--exp_date', type=str, help='expiration date of product', required=True)
    # dest='exp_date'
    # optional date of buying

    # sell parser
    sell_parser = mainparsers.add_parser('sell', help="Sell products")
    sell_parser.add_argument('--product', type=str, help='product name', required=True)
    sell_parser.add_argument('--amount', type=int, help='product amount', default=1)
    sell_parser.add_argument('--sell_price', type=float, help='sell price per product', required=True)
    # might need date of selling
    
    # inventory parser
    inv_parser = mainparsers.add_parser('inventory', help="Get a list of products")
    inv_parser.add_argument('show', help='Get a list of products')

    args = parser.parse_args()
    return choose_args(args)

def choose_args(args):
    if args.options == 'inventory':
        # if args.options.inventory == 'show':
        print(super_inventory.options('show'))
    elif args.options == 'buy':
        super_bought.buy(args.product, args.amount, args.buy_price, args.exp_date)
    elif args.options == 'sell':
        print('sell')





if __name__ == '__main__':
    main()

