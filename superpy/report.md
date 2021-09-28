# SUPERPY - Backend Assignment

This is my interpretation of the Superpy assignment. 

I created a CLT for any supermarket to be used.

## Functions
<inventory>     Check inventory of products
<buy>           Buy product
<sell>          Sell
<convert>       Convert csv to html or json
<remove>        Remove product from inventory if expired
<eco>           Get the amount in costs, revenue and profit
<advance>       Advance time in days 
<credits>       See who made this

## Additional features:
I've included a parser for converting the inventory to either html or json.
```python
# example

# in terminal type:
python main.py convert html

```

The program also includes rich coloration in the terminal.

## Usage


```python
# pre requirement:
pip install pandas
pip install rich
cd superpy

# in terminal type:
python main.py
# to see a list of options

# example:
python main.py buy -p Beer -a 12 -b 1.5 -e 28/09/2021
# will add 12 Beers to the buy report

```

# KASPER SIMONS 
