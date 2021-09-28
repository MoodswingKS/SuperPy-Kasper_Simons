from rich import pretty
from rich.console import Console
console = Console()

def credits():
    print("""
    #   ______     __  __     ______   ______     ______     ______   __  __    
    #  /\  ___\   /\ \/\ \   /\  == \ /\  ___\   /\  == \   /\  == \ /\ \_\ \   
    #  \ \___  \  \ \ \_\ \  \ \  _-/ \ \  __\   \ \  __<   \ \  _-/ \ \____ \  
    #   \/\_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\  \ \_\    \/\_____\ 
    #    \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/   \/_/     \/_____/ 
    #                                                                           
    #
    #      __  __     ______     ______     ______   ______     ______          
    #     /\ \/ /    /\  __ \   /\  ___\   /\  == \ /\  ___\   /\  == \         
    #     \ \  _"-.  \ \  __ \  \ \___  \  \ \  _-/ \ \  __\   \ \  __<         
    #      \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\    \ \_____\  \ \_\ \_\       
    #       \/_/\/_/   \/_/\/_/   \/_____/   \/_/     \/_____/   \/_/ /_/       
    #                                                                           
    #      ______     __     __    __     ______     __   __     ______         
    #     /\  ___\   /\ \   /\ "-./  \   /\  __ \   /\ "-.\ \   /\  ___\        
    #     \ \___  \  \ \ \  \ \ \-./\ \  \ \ \/\ \  \ \ \-.  \  \ \___  \       
    #      \/\_____\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \/\_____\      
    #       \/_____/   \/_/   \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/      
    #                                                                           
    """)

subparsers = print(f"""
You can type these commands to check the options available
<inventory>     Check inventory of products
<buy>           Buy product
<sell>          Sell
<convert>       Convert csv to html or json
<remove>        Remove product from inventory if expired
<eco>           Get the amount in costs, revenue and profit
<advance>       Advance time in days 
<credits>       See who made this
""")

help_inv = print(f"""
<inventory>     INVENTORY
You can type this command:
show        Gives you a list of all products currently in inventory
""")

help_buy = print(f"""
<buy>                   BUY product
You can type these commands to check the options available
-p, --product           Name of product bought
-a, --amount            Amount bought
-b, --buy_price         At which price it was bought
-e, --expiration_date   When does it expire(dd/mm/yyyy)
""")

help_sell = print(f"""
<sell>                  SELL product
You can type these commands to check the options available
-p, --product           Name of product sold
-a, --amount            Amount sold
-b, --buy_price         At which price it was sold
-e, --expiration_date   When it was sold(dd/mm/yyyy)
""")

help_convert = print(f"""
<convert>               Convert csv to html or json
You can type this command to check the options available
-t, --type              json or html, for desired output
""")

help_remove = print(f"""
<remove>               Remove products from inventory if expired
You can type this command to check the options available
-d, --day              Either fill in the date(dd/mm/yyyy) or leave blank for current day
""")

help_eco = print(f"""
<eco>                  Economic values
You can type this command to check the values:
-o, --option           costs, revenue or profit
""")

help_advance = print(f"""
<advance>              Advance in days
You can type this command to change the date:
-d, --days             Days as a number
""")

help_credits = print(f"""
<credits>               Type credits to see who made this
super                   Super!
""")