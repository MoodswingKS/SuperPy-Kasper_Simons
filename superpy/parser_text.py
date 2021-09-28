from rich import pretty
from rich.console import Console
console = Console()

def credits():
    console.print("""
    #   ______     __  __     ______   ______     ______     ______   __  __    
    #  /\  ___\   /\ \/\ \   /\  == \ /\  ___\   /\  == \   /\  == \ /\ \_\ \   
    #  \ \___  \  \ \ \_\ \  \ \  _-/ \ \  __\   \ \  __<   \ \  _-/ \ \____ \  
    #   \/\_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\  \ \_\    \/\_____\ 
    #    \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/   \/_/     \/_____/ 
    #                                                                           
    #
    [bold red]#      __  __     ______     ______     ______   ______     ______          
    #     /\ \/ /    /\  __ \   /\  ___\   /\  == \ /\  ___\   /\  == \         
    #     \ \  _"-.  \ \  __ \  \ \___  \  \ \  _-/ \ \  __\   \ \  __<         
    #      \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\    \ \_____\  \ \_\ \_\       
    #       \/_/\/_/   \/_/\/_/   \/_____/   \/_/     \/_____/   \/_/ /_/       
    [/bold red]#                                                                           
    #      ______     __     __    __     ______     __   __     ______         
    #     /\  ___\   /\ \   /\ "-./  \   /\  __ \   /\ "-.\ \   /\  ___\        
    #     \ \___  \  \ \ \  \ \ \-./\ \  \ \ \/\ \  \ \ \-.  \  \ \___  \       
    #      \/\_____\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \/\_____\      
    #       \/_____/   \/_/   \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/      
    #                                                                           
    """)

subparsers = console.print(f"""
You can type these commands to check the options available
<inventory>     [green]Check inventory of products[/green]
<buy>           [green]Buy product[/green]
<sell>          [green]Sell[/green]
<convert>       [green]Convert csv to html or json[/green]
<remove>        [green]Remove product from inventory if expired[/green]
<eco>           [green]Get the amount in costs, revenue and profit[/green]
<advance>       [green]Advance time in days [/green]
<credits>       [green]See who made this[/green]
""")

help_inv = console.print(f"""
<inventory>     [green]INVENTORY[/green]
You can type this command:
[green]show        Gives you a list of all products currently in inventory[/green]
""")

help_buy = console.print(f"""
<buy>                   [green]BUY product[/green]
You can type these commands to check the options available
-p, --product           [green]Name of product bought[/green]
-a, --amount            [green]Amount bought[/green]
-b, --buy_price         [green]At which price it was bought[/green]
-e, --expiration_date   [green]When does it expire(dd/mm/yyyy)[/green]
""")

help_sell = console.print(f"""
<sell>                  [green]SELL product[/green]
You can type these commands to check the options available
-p, --product           [green]Name of product sold[/green]
-a, --amount            [green]Amount sold[/green]
-b, --buy_price         [green]At which price it was sold[/green]
-e, --expiration_date   [green]When it was sold(dd/mm/yyyy)[/green]
""")

help_convert = console.print(f"""
<convert>               [green]Convert csv to html or json[/green]
You can type this command to check the options available
-t, --type              [green]json or html, for desired output[/green]
""")

help_remove = console.print(f"""
<remove>               [green]Remove products from inventory if expired[/green]
You can type this command to check the options available
-d, --day              [green]Either fill in the date(dd/mm/yyyy) or leave blank for current day[/green]
""")

help_eco = console.print(f"""
<eco>                  [green]Economic values[/green]
You can type this command to check the values:
-o, --option           [green]costs, revenue or profit[/green]
""")

help_advance = console.print(f"""
<advance>              [green]Advance in days[/green]
You can type this command to change the date:
-d, --days             [green]Days as a number[/green]
""")

help_credits = console.print(f"""
<credits>               Type credits to see who made this
super                   [red bold]Super![/red bold]
""")