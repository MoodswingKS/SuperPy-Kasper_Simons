# Imports
import argparse
from datetime import datetime
from arg_functions import global_date, conversion, getProfit, auto_update
from arg_functions import super_inventory, super_bought, super_sold
from parser_text import parser_text, help_me
from helpers import valid_date

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

this_date = datetime.now().date()

def main():
    # global parser init
    parser = argparse.ArgumentParser(description="SUPERPY")
    mainparsers = parser.add_subparsers(dest='options')
    mainparsers.required = True
    
    buy_parser = mainparsers.add_parser('buy', help=help_me)
    buy_parser.add_argument('-p', '--product', type=str, required=True)
    buy_parser.add_argument('-a', '--amount', type=int, default=1)
    buy_parser.add_argument('-b', '--buy_price', type=float, required=True)
    buy_parser.add_argument('-e', '--exp_date', type=valid_date, required=True)
    # sell parser
    sell_parser = mainparsers.add_parser('sell')
    sell_parser.add_argument('-p', '--product', type=str, required=True)
    sell_parser.add_argument('-a', '--amount', type=int, default=1)
    sell_parser.add_argument('-s', '--sell_price', type=float, required=True)
    sell_parser.add_argument('-sd', '--sell_date', type=valid_date, required=True)
    # inventory parser
    inv_parser = mainparsers.add_parser('inventory')
    inv_parser.add_argument('show')
    # advance time parser
    adv_parser = mainparsers.add_parser('advance')
    adv_parser.add_argument('-d', '--days', type=int, required=True)
    # revenue parser
    rev_parser = mainparsers.add_parser('eco')
    rev_parser.add_argument('-o', '--option', type=str, required=True)
    # remove expired products parser
    remove_parser = mainparsers.add_parser('remove')
    remove_parser.add_argument('-d', '--day', type=valid_date, default=global_date)
    # convert parser
    conv_parser = mainparsers.add_parser('convert')
    conv_parser.add_argument('-t', '--type', type=str, required=True)
    # credits parser
    credit_parser = mainparsers.add_parser('credits')
    credit_parser.add_argument('super')
    # updater
    update_parser = mainparsers.add_parser('update')
    update_parser.add_argument('-t', '--type', type=str, required=True)
    # help parser
    help_parser = mainparsers.add_parser('help')
    help_parser.add_argument('help')

    args = parser.parse_args()
    choose_args(args)

def choose_args(args):
    if args.options == 'inventory':
        print(super_inventory.options('show'))
    elif args.options == 'buy':
        super_bought.buy(args.product, args.amount, args.buy_price, args.exp_date)
    elif args.options == 'sell':
        super_sold.check_if_exists(args.product)
        super_sold.sell(args.product, args.amount, args.sell_price, args.sell_date)
    elif args.options == 'convert':
        conversion(args.type)
    elif args.options == 'credits':
        parser_text('credits')
    elif args.options == 'remove':
        super_inventory.remove_products()
    elif args.options == 'eco':
        getProfit(args.option)
    elif args.options == 'advance':
        global_date(args.days)
    elif args.options == 'update':
        auto_update(args.type)
    elif args.options == 'help':
        parser_text('main')

if __name__ == '__main__':
    main()

