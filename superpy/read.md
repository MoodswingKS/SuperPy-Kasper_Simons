# SUPERPY - Backend Assignment

This is my interpretation of the Superpy assignment. 

I created a CLT for any supermarket to be used.

## Functions
- BUY products
- SELL products
- INVENTORY check
- TIME advance
- REMOVE expired products
- CREDITS to see something great!

## Additional features:
I've included a parser for converting the inventory to either excel, text or json.
```python
# example

# in terminal type:
python main.py convert text

```

The program will auto adjust the inventory on every report made in buy or sell.
```python
# in terminal type:
python main.py auto
```

## Usage


```python
# pre requirement for conversion:
pip install pandas

# in terminal type:
python main.py
# to see a list of options

# example:
python main.py buy -p Bier -a 12 -b 1.5 -e 22-09-2021
# will add 12 Beers to the buy report

```

# KASPER SIMONS 
