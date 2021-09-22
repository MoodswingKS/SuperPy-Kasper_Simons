# Imports
import argparse
from datetime import datetime
# from datetime import date
from arg_functions import super_inventory, super_bought, super_sold, valid_date
from parser_text import credits
from create_csv import create


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


this_date = datetime.now().date()

# still need to make the date information
# can create a remove expired products with date information
# change help screen with the parsers
def main():
    # global parser init
    parser = argparse.ArgumentParser(description="SUPERPY")
    
    mainparsers = parser.add_subparsers(dest='options')
    mainparsers.required = True
    
    # buy parser
    buy_parser = mainparsers.add_parser('buy', help="Buy products")
    buy_parser.add_argument('-p', '--product', type=str, help='product name', required=True)
    buy_parser.add_argument('-a', '--amount', type=int, help='product amount', default=1)
    buy_parser.add_argument('-b', '--buy_price', type=float, help='buy price per product', required=True)
    buy_parser.add_argument('-e', '--exp_date', type=valid_date, help='expiration date of product - format dd/mm/yyyy', required=True)
    # dest='exp_date'
    # optional date of buying

    # sell parser
    sell_parser = mainparsers.add_parser('sell', help="Sell products")
    sell_parser.add_argument('-p', '--product', type=str, help='product name', required=True)
    sell_parser.add_argument('-a', '--amount', type=int, help='product amount', default=1)
    sell_parser.add_argument('-s', '--sell_price', type=float, help='sell price per product', required=True)
    sell_parser.add_argument('-e', '--exp_date', type=valid_date, help='expiration date - format dd/mm/yyyy', required=True)
    # might need date of selling
    
    # inventory parser
    inv_parser = mainparsers.add_parser('inventory', help="Get a list of products")
    inv_parser.add_argument('show', help='Get a list of products')

    # advance time parser
    adv_parser = mainparsers.add_parser('time', help="Tell me my profit over a certain period of time")
    adv_parser.add_argument('-t', '--time', help="amount of days", type=int, required=True)

    # remove expired products parser
    remove_parser = mainparsers.add_parser('remove-product', help="Remove expired products from list")
    remove_parser.add_argument('-t', '--time', type=str, help="remove products", default=this_date, required=True)

    # credits parser
    credit_parser = mainparsers.add_parser('credits', help="CREDITS")
    credit_parser.add_argument('super', help="Show me who made this!")

    args = parser.parse_args()
    return choose_args(args)

def choose_args(args):
    if args.options == 'inventory':
        # if args.options.inventory == 'show':
        print(super_inventory.options('show'))
    elif args.options == 'buy':
        super_bought.buy(args.product, args.amount, args.buy_price, args.exp_date)
    elif args.options == 'sell':
        super_sold.sell(args.product, args.amount, args.sell_price, args.exp_date)
    elif args.options == 'remove-product':
        pass
    elif args.options == 'time':
        pass    
    elif args.options == 'credits':
        credits()





if __name__ == '__main__':
    main()

