# Imports
import argparse
from datetime import datetime, timedelta
from arg_functions import global_date, valid_date, conversion, auto_update, getProfit
from arg_functions import super_inventory, super_bought, super_sold
from parser_text import credits


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


this_date = datetime.now().date()


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
    sell_parser.add_argument('-sd', '--sell_date', type=valid_date, help='sell date - format dd/mm/yyyy', required=True)
    
    # inventory parser
    inv_parser = mainparsers.add_parser('inventory', help="Get a list of products")
    inv_parser.add_argument('show', help='Get a list of products')

    # advance time parser
    adv_parser = mainparsers.add_parser('advance', help="Tell me my profit over a certain period of time")
    adv_parser.add_argument('-t', '--time', help="amount of days", type=int, required=True)


    # reset day parser
    # reset_parser = mainparsers.add_parser('reset', help="Reset date")
    # reset_parser.add_argument('current', help="Reset current time", required=True)


    # revenue parser
    rev_parser = mainparsers.add_parser('eco', help="Revenue")
    rev_parser.add_argument('-o', '--option', type=str,  help="Type either 'revenue', 'costs' or 'profit'", required=True)

    # remove expired products parser
    remove_parser = mainparsers.add_parser('remove', help="Remove expired products from list")
    remove_parser.add_argument('-d', '--day', type=valid_date, help="remove products that have expired", default=global_date)

    # auto update parser
    auto_parser = mainparsers.add_parser('auto', help='Auto update inventory')
    auto_parser.add_argument('sell', help='update command')

    # convert parser
    conv_parser = mainparsers.add_parser('convert', help='conversion to other extension')
    conv_parser.add_argument('-t', '--type', type=str, help='type either json or html', required=True)

    # credits parser
    credit_parser = mainparsers.add_parser('credits', help="CREDITS")
    credit_parser.add_argument('super', help="Show me who made this!")

    args = parser.parse_args()
    return choose_args(args)

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
        credits()
    elif args.options == 'remove':
        super_inventory.remove_products()
    elif args.options == 'eco':
        getProfit(args.option)
    elif args.options == 'auto':
        # fix remove-product and use same logic for auto update
        auto_update(args.sell)
    elif args.options == 'advance':
        global_date(args.time)
    # elif args.options == 'reset':
    #     global_date()


if __name__ == '__main__':
    main()

