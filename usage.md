# Usage Guide

Everything can also be accessed by writing:
```python
$python main.py 
```
In the CLT. I encourage you to have a look, as there are shorthand versions for each of the options below available.   


## Examples for each section:

### Buy
```python
$python main.py buy --product <PRODUCT> --amount <AMOUNT> --buy_price <PRICE> --expiration_date <dd/mm/yyyy>
```
### Sell
```python
$python main.py sell --product <PRODUCT> --amount <AMOUNT> --sell_price <PRICE> --sell_date <dd/mm/yyyy>
```
### Inventory
```python
$python main.py inventory show
```
### Update
```python
$python main.py update -t buy
$python main.py update -t sell
```
### Remove
```python
$python main.py remove --day <day>
```
### Revenue
```python
$python main.py eco --option revenue
$python main.py eco --option costs
$python main.py eco --option profit
```
### Convert
```python
$python main.py convert --type json
$python main.py convert --type html
```
### Advance
```python
$python main.py advance --days <dd/mm/yyyy>
```
### Credits
```python
$ python main.py credits super
```
