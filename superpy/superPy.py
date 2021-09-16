import argparse
from parser_text import parser_epilog, subparsers


# parser = argparse.ArgumentParser(
#     formatter_class=argparse.RawTextHelpFormatter,
#     description=__doc__,
#     epilog=parser_epilog,
#     )
# parser.set_defaults(func=None)

# parser.parse_args()
    
#     # _subparsers = parser.add_subparsers(
#     #     dest="subparser_name",
#     #     description=subparsers,
#     # )

import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))